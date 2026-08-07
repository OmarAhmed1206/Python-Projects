import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ChatAction
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

from Gemini import ask_gemini
from memory import (
    ensure_user,
    save_user_message,
    save_assistant_message,
    load_history,
    clear_user_history,
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is missing")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name or "friend"
    username = message.from_user.username

    user, created = ensure_user(telegram_id, first_name, username)

    if created:
        await message.answer(
            f"Hello, {first_name} 👋\n"
            "Your account has been created."
            "Please use /help for more functions."
        )

    else:
        await message.answer(
            f"Welcome back, {first_name} 👋\n"
            "How can I help you?"
        )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "/start - create or open your account\n"
        "/help - show commands\n"
        "/about - what this bot does\n"
        "/ping - test if the bot is alive\n"
        "/history - show the last messages\n"
        "/clear - erase your chat memory"
    )


@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer(
        "I am Omni, a Telegram AI assistant backed by Gemini and SQL memory."
    )


@dp.message(Command("ping"))
async def ping_command(message: Message):
    await message.answer("Pong! ✅")


@dp.message(Command("history"))
async def history_command(message: Message):
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name or "friend"
    username = message.from_user.username

    user, _ = ensure_user(telegram_id, first_name, username)
    user_id = user[0]

    history = load_history(user_id)

    if not history:
        await message.answer("No history yet.")
        return

    lines = []
    for role, text in history[-10:]:
        who = "You" if role == "user" else "Omni"
        lines.append(f"{who}: {text}")

    await message.answer("\n".join(lines))


@dp.message(Command("clear"))
async def clear_command(message: Message):
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name or "friend"
    username = message.from_user.username

    user, _ = ensure_user(telegram_id, first_name, username)
    user_id = user[0]

    clear_user_history(user_id)
    await message.answer("Your chat memory has been cleared.")


@dp.message()
async def ai_message(message: Message):
    if not message.text:
        await message.answer("Please send text only.")
        return

    telegram_id = message.from_user.id
    first_name = message.from_user.first_name or "friend"
    username = message.from_user.username

    user, _ = ensure_user(telegram_id, first_name, username)
    user_id = user[0]

    save_user_message(user_id, message.text)

    history = load_history(user_id)

    try:
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            response = ask_gemini(history)
    except Exception as e:
        print("Gemini error:", e)
        await message.answer("Sorry, I hit a problem while thinking.")
        return

    save_assistant_message(user_id, response)
    await message.answer(response)


async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())