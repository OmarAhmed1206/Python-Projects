# SFDA Medical Device Registry Scraper

A Python scraper for extracting the complete SFDA (Saudi Food & Drug Authority) medical device registry from the official SFDA Developer API. Covers all three device classifications — **TFA**, **GHTF**, and **Lowrisk** — and outputs clean, analysis-ready CSV files.

---

## 📦 Output

| File | Rows | Columns | Description |
|---|---|---|---|
| `sfda_TFA_final.csv` | ~31,549 | 24 | High-risk medical devices (Third-Party Assessment) |
| `sfda_GHTF_final.csv` | ~98,920 | 26 | Internationally harmonized devices (Global Harmonization Task Force) |
| `sfda_Lowrisk_final.csv` | ~34,194 | 16 | Low-risk medical products |

**Total: ~164,663 device records**

---

## 🗂️ Project Structure

```
SFDA/
│
├── sfda_TFA.py               # Scraper for TFA devices
├── sfda_GHTF.py              # Scraper for GHTF devices
├── sfda_Lowrisk.py           # Scraper for Lowrisk devices
│
├── cleaning.py               # Cleaning script for all 3 datasets
│
├── sfda_TFA_progress.json    # Auto-generated resume state (TFA)
├── sfda_GHTF_progress.json   # Auto-generated resume state (GHTF)
├── sfda_Lowrisk_progress.json# Auto-generated resume state (Lowrisk)
│
├── sfda_TFA.csv              # Raw scraped output
├── sfda_GHTF.csv             # Raw scraped output
├── sfda_Lowrisk.csv          # Raw scraped output
│
├── sfda_TFA_final.csv        # Clean final output
├── sfda_GHTF_final.csv       # Clean final output
└── sfda_Lowrisk_final.csv    # Clean final output
```

---

## ⚙️ How It Works

The scraper hits the official SFDA Developer API:
```
https://apis.sfda.gov.sa:9002/v2/dwh-md
```

Endpoints:
- `/TFA/list/{page}`
- `/GHTF/list/{page}`
- `/Lowrisk/list/{page}`

Authentication is handled via OAuth2 client credentials with automatic token refresh.

### Features
- ✅ OAuth token with auto-refresh on expiry
- ✅ Column headers discovered live from the API response
- ✅ Resume from where it stopped — never loses progress
- ✅ Saves progress after every single page (no duplicate rows on crash)
- ✅ Connection reset recovery with session rebuild
- ✅ Rate limit handling — respects `Retry-After` headers
- ✅ Jumps forward automatically when large 404 blocks are hit
- ✅ Arabic text preserved correctly (UTF-8)
- ✅ All 3 scrapers can run simultaneously in separate terminals

---

## 🚀 Usage

### 1. Install dependencies
```bash
pip install requests urllib3
```

### 2. Run the scrapers
Open 3 terminals and run all at once for maximum speed:
```bash
# Terminal 1
python sfda_TFA.py

# Terminal 2
python sfda_GHTF.py

# Terminal 3
python sfda_Lowrisk.py
```

Each scraper saves progress after every page. If it gets interrupted, just rerun the same script — it will resume exactly where it stopped.

### 3. Clean the output
```bash
python cleaning.py
```

This produces the three `_final.csv` files with duplicates removed and encoding normalized to UTF-8.

---

## 📋 Data Fields

### TFA (24 columns)
`source_type`, `deviceNumber`, `referenceNumber`, `brandName`, `riskClassification`, `expiryDate`, `licenseNumber`, `manufacture_Phone`, `manufacturerName`, `manufacture_CountryAr`, `manufacture_CountryEn`, `manufacture_city`, `isLocalManufacturer`, `modelNumber`, `gmdn`, `isSuspended`, `suspendTFADetails`, `isCanceled`, `cancelTfaDetails`, `singleUse`, `intendedUse`, `intendedUseArabicDescription`, `briefDescription`, `hasAccessories`

### GHTF (26 columns)
`source_type`, `referenceNumber`, `deviceNumber`, `tradeName`, `tradeNameAr`, `genericName`, `expiryDate`, `manufacturerName`, `manufacture_CountryAr`, `manufacture_CountryEn`, `manufacture_city`, `manufacture_Phone`, `isLocalManufacturer`, `modelNumber`, `gmdn`, `classification`, `isSuspended`, `suspendDate`, `suspendDetails`, `isCanceled`, `cancelDetails`, `singleUse`, `descriptionEn`, `descriptionAr`, `hasAccessories`, `intendedUse`

### Lowrisk (16 columns)
`source_type`, `registrationNumber`, `expiryDate`, `is_LRSuspended`, `is_LRCanceled`, `manufactureName`, `manufactureCountryAR`, `manufactureCountry`, `manufactureCity`, `productNumber`, `productName`, `productNameAr`, `genericName`, `description`, `barCodes`, `intendedUse`

---

## ⚠️ Important Notes

- **Do not open the raw CSV files by double-clicking in Excel.** Some fields (e.g. `modelNumber`, `barCodes`) contain embedded newlines which Excel incorrectly explodes into fake rows, inflating the row count. Always import via **Data → Get Data → From Text/CSV** in Excel, or use the cleaning script.
- The `_progress.json` files are auto-generated and track scraping state. Delete them if you want to rescrape from scratch.
- Duplicate `deviceNumber` entries are intentional — the same physical device can hold multiple licenses/registrations simultaneously.

---

## 🔧 Requirements

- Python 3.8+
- `requests`
- `urllib3`
- `pandas` (cleaning script only)

---

## 📊 Data Source

**Saudi Food & Drug Authority (SFDA)**
- Website: [www.sfda.gov.sa](https://www.sfda.gov.sa)
- API: [apis.sfda.gov.sa](https://apis.sfda.gov.sa:9002/v2/dwh-md)

Data is publicly available through the SFDA Developer API and reflects the official Saudi medical device registry.
