from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")
BOT_TOPIC      = os.getenv("BOT_TOPIC", "Python Básico")

BLACKLIST_WORDS = [

    # Palavrões
    "porra",
    "caralho",
    "merda",
    "puta",
    "puto",
    "bosta",
    "cacete",
    "desgraça",
    "fdp",
    "filho da puta",
    "arrombado",
    "vsf",
    "vtnc",
    "vai tomar no cu",
    "vai se ferrar",

    # Ofensas
    "idiota",
    "burro",
    "imbecil",
    "retardado",
    "otário",
    "otario",
    "babaca",
    "lixo",
    "anta",
    "nojento",
    "escroto",
    "ridículo",
    "ridiculo",
    "palhaço",
    "palhaco",
    "inútil",
    "inutil",

    # Bullying / preconceito
    "racista",
    "nazista",
    "homofóbico",
    "homofobico",
    "preconceituoso",
    "racismo",
    "homofobia",

    # Conteúdo impróprio
    "pornografia",
    "sexo",
    "nudez",
    "nudes",
    "erótico",
    "erotico",
    "conteúdo adulto",
    "conteudo adulto",

    # Violência
    "matar",
    "assassinar",
    "espancar",
    "ameaça",
    "arma",
    "explosivo",

    # Drogas
    "maconha",
    "cocaína",
    "cocaina",
    "crack",
    "heroína",
    "heroina",
    "tráfico",
    "trafico",

    # Spam / golpes
    "hack",
    "phishing",
    "clique aqui",
    "ganhe dinheiro",
    "link suspeito",

    # Inglês
    "fuck",
    "shit",
    "bitch",
    "asshole",
    "bastard",
    "motherfucker"
]

MAX_WARNS = 3

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN não encontrado no .env")
if not GEMINI_KEY:
    raise ValueError("GEMINI_KEY não encontrado no .env")
if not BOT_TOPIC:
    raise ValueError("BOT_TOPIC não encontrado no .env")
