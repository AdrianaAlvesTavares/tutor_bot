from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")
BOT_TOPIC      = os.getenv("BOT_TOPIC", "Python Básico")

BLACKLIST_WORDS = [
    "palavra_ruim_1",
    "palavra_ruim_2",
]

MAX_WARNS = 3

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN não encontrado no .env")
if not GEMINI_KEY:
    raise ValueError("GEMINI_KEY não encontrado no .env")
if not BOT_TOPIC:
    raise ValueError("BOT_TOPIC não encontrado no .env")