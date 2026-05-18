"""
SFDA — GHTF Scraper
====================
Scrapes all GHTF medical device records from the SFDA API.
Run alongside sfda_TFA.py and sfda_Lowrisk.py in separate terminals.

Output : sfda_GHTF.csv
State  : sfda_GHTF_progress.json   ← resumes if script is closed
Log    : sfda_GHTF.log
"""

import csv, json, logging, sys, time
from pathlib import Path
import requests, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ── Config ────────────────────────────────────────────────────────────────────
DEVICE_TYPE   = "GHTF"
CLIENT_ID     = "Cw02uSPQR1BAC9Ceil850U3pIRkRmAZSfeafdMVfkFsHA3aG"
CLIENT_SECRET = "HYyyGi8Dj5G8VP3AaOHNfm5it2EhDfbQOXdIGfOtHx6LhtcHg1Gqiv1MqEXYWKSY"
TOKEN_URL     = "https://apis.sfda.gov.sa:9002/v2/oauth/accesstoken"
BASE_URL      = "https://apis.sfda.gov.sa:9002/v2/dwh-md"

REQUEST_DELAY = 0.5
MAX_RETRIES   = 6
RETRY_DELAY   = 5
TIMEOUT       = 30
RESET_BACKOFF = 15
JUMP_AFTER    = 30
JUMP_SIZE     = 200
SAVE_EVERY    = 50

OUT_DIR    = Path(__file__).parent
CSV_PATH   = OUT_DIR / f"sfda_{DEVICE_TYPE}.csv"
STATE_FILE = OUT_DIR / f"sfda_{DEVICE_TYPE}_progress.json"
LOG_FILE   = OUT_DIR / f"sfda_{DEVICE_TYPE}.log"

# ── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
log = logging.getLogger(DEVICE_TYPE)


# ── Helpers ───────────────────────────────────────────────────────────────────
def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

def save_state(state: dict):
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
    tmp.replace(STATE_FILE)

def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    return s

def rebuild_session(session: requests.Session):
    try:
        session.close()
    except Exception:
        pass
    fresh = make_session()
    session.headers.update(fresh.headers)
    session.mount("http://",  fresh.get_adapter("http://"))
    session.mount("https://", fresh.get_adapter("https://"))

def get_token(session: requests.Session) -> str:
    log.info("Requesting OAuth token...")
    strategies = [
        {"params": {"grant_type": "client_credentials"}, "data": None,
         "auth": (CLIENT_ID, CLIENT_SECRET), "label": "BasicAuth"},
        {"params": {"grant_type": "client_credentials", "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET}, "data": None, "auth": None, "label": "AllQP"},
        {"params": {"grant_type": "client_credentials"},
         "data": {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET},
         "auth": None, "label": "QP+Body"},
    ]
    for s in strategies:
        try:
            r = session.post(TOKEN_URL, params=s["params"], data=s["data"], auth=s["auth"],
                             headers={"Content-Type": "application/x-www-form-urlencoded"},
                             timeout=20, verify=False)
            if r.status_code == 200:
                token = r.json().get("access_token") or r.json().get("token")
                if token:
                    log.info("  ✓ Token OK (%s)", s["label"])
                    return token
        except Exception as e:
            log.warning("  Strategy %s failed: %r", s["label"], e)
        time.sleep(1.5)
    raise RuntimeError("Cannot obtain OAuth token.")

def fetch_page(session, token_holder, page):
    url = f"{BASE_URL}/{DEVICE_TYPE}/list/{page}"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.get(url, headers={"Authorization": f"Bearer {token_holder[0]}"},
                            timeout=TIMEOUT, verify=False)
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 401:
                log.warning("p%s: 401 — refreshing token", page)
                token_holder[0] = get_token(session)
                continue
            elif r.status_code == 404:
                return None
            elif r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 45))
                log.warning("p%s: rate-limited — sleeping %ss", page, wait)
                time.sleep(wait)
            else:
                log.warning("p%s attempt %s: HTTP %s", page, attempt, r.status_code)
                time.sleep(RETRY_DELAY * attempt)

        except requests.exceptions.ConnectionError:
            log.warning("p%s attempt %s: connection reset — rebuilding session", page, attempt)
            rebuild_session(session)
            time.sleep(RESET_BACKOFF + attempt * 5)
        except requests.exceptions.Timeout:
            log.warning("p%s attempt %s: timeout", page, attempt)
            time.sleep(RETRY_DELAY * attempt)
        except Exception as exc:
            log.warning("p%s attempt %s: %r", page, attempt, exc)
            time.sleep(RETRY_DELAY * attempt)

    log.error("p%s: failed after %s attempts — skipping", page, MAX_RETRIES)
    return None

def discover_columns(records: list) -> list:
    seen, cols = {"source_type"}, ["source_type"]
    for rec in records:
        if isinstance(rec, dict):
            for k in rec:
                if k not in seen:
                    seen.add(k)
                    cols.append(k)
    return cols

def flatten(raw, columns) -> dict:
    if not isinstance(raw, dict):
        return {col: "" for col in columns}
    row = {"source_type": DEVICE_TYPE}
    for col in columns:
        if col == "source_type":
            continue
        val = raw.get(col, "")
        row[col] = "" if val is None else str(val).strip()
    return row


# ── Main ──────────────────────────────────────────────────────────────────────
def run():
    log.info("=" * 60)
    log.info("SFDA %s Scraper", DEVICE_TYPE)
    log.info("=" * 60)

    state        = load_state()
    session      = make_session()
    token_holder = [get_token(session)]

    log.info("Fetching page 1 for metadata...")
    p1 = fetch_page(session, token_holder, 1)
    if p1 is None:
        log.error("Cannot fetch page 1 — aborting.")
        sys.exit(1)

    meta        = p1.get("metadata", {}) or {}
    total_pages = meta.get("pageCount", 0)
    total_rec   = meta.get("rowCount",  0)
    page_size   = meta.get("pageSize",  10)
    if not total_pages and total_rec:
        total_pages = (total_rec + page_size - 1) // page_size

    log.info("%s records across %s pages", f"{total_rec:,}", f"{total_pages:,}")

    p1_records = p1.get("data", [])
    if isinstance(p1_records, dict):
        p1_records = [p1_records]

    is_resume = bool(state)
    if is_resume and state.get("columns"):
        columns = state["columns"]
        log.info("Resuming — using %s saved columns", len(columns))
    else:
        columns = discover_columns(p1_records)
        log.info("Discovered %s columns: %s%s",
                 len(columns), ", ".join(columns[:8]), " …" if len(columns) > 8 else "")

    start_page = state.get("next_page", 1)
    written    = state.get("written", 0)

    if start_page > total_pages:
        log.info("Already complete (%s records). Delete %s to re-run.",
                 f"{written:,}", STATE_FILE.name)
        return

    log.info("Starting from page %s (written so far: %s)", start_page, f"{written:,}")

    file_mode = "a" if is_resume else "w"
    with CSV_PATH.open(file_mode, newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore", restval="")

        if not is_resume:
            writer.writeheader()
            log.info("Wrote CSV header (%s columns)", len(columns))

        if start_page == 1 and p1_records:
            for raw in p1_records:
                writer.writerow(flatten(raw, columns))
                written += 1
            fh.flush()
            start_page = 2
            state = {"next_page": start_page, "written": written, "columns": columns}
            save_state(state)

        page            = start_page
        consecutive_err = 0

        while page <= total_pages:
            time.sleep(REQUEST_DELAY)
            data = fetch_page(session, token_holder, page)

            if data is None:
                consecutive_err += 1
                log.warning("Skip p%s (%s consecutive)", page, consecutive_err)

                if consecutive_err >= JUMP_AFTER:
                    jump_to = min(page + JUMP_SIZE, total_pages)
                    log.warning("JUMP p%s → p%s after %s consecutive misses",
                                page, jump_to, consecutive_err)
                    page            = jump_to
                    consecutive_err = 0
                else:
                    page += 1
                continue

            consecutive_err = 0
            records = data.get("data", [])
            if isinstance(records, dict):
                records = [records]
            if not records:
                log.info("Empty page %s — end of data", page)
                break

            for raw in records:
                writer.writerow(flatten(raw, columns))
                written += 1
            fh.flush()

            if page % SAVE_EVERY == 0:
                state = {"next_page": page + 1, "written": written, "columns": columns}
                save_state(state)
                log.info("p%s/%s — %s records", page, total_pages, f"{written:,}")

            page += 1

    state = {"next_page": total_pages + 1, "written": written, "columns": columns, "done": True}
    save_state(state)
    log.info("DONE — %s records → %s", f"{written:,}", CSV_PATH.name)
    log.info("=" * 60)


if __name__ == "__main__":
    run()
