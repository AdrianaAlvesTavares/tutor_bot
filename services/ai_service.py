import asyncio
import requests
from config import GEMINI_KEY, BOT_TOPIC

SYSTEM_PROMPT = (
    f"Você é um tutor virtual especializado em {BOT_TOPIC}. "
    f"Responda APENAS perguntas sobre {BOT_TOPIC}. "
    f"Se a pergunta for fora do tema, diga: 'Só posso ajudar com dúvidas sobre {BOT_TOPIC}.' "
    f"Máximo de 200 palavras. Use linguagem clara para iniciantes. "
    f"Use SQL correto e funcional nos exemplos. "
    f"NUNCA invente comandos que não existem em SQL."
)

async def ask_tutor(question: str) -> str:
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": GEMINI_KEY
        }

        payload = {
            "contents": [
                {
                    "parts": [{
                        "text": f"{SYSTEM_PROMPT}\n\nPergunta do aluno: {question}"
                    }]
                }
            ],
            "generationConfig": {
                "maxOutputTokens": 400
            }
        }

        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: requests.post(url, headers=headers, json=payload, timeout=15)
        )

        if response.status_code != 200:
            return f"❌ Erro ao consultar o tutor (código {response.status_code})."

        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except requests.Timeout:
        return "⏳ O servidor demorou demais. Tente novamente."
    except requests.ConnectionError:
        return "❌ Sem conexão. Verifique sua internet."
    except Exception as e:
        return f"❌ Erro inesperado: {str(e)[:100]}"