from database.db import upsert_user, get_user, add_warn

def get_or_create(user_id: int, username: str):
    return upsert_user(user_id, username or "anon")

def get_status(user_id: int):
    user = get_user(user_id)
    if not user:
        return "active"
    return user["status"]

def register_infraction(user_id: int):
    new_status = add_warn(user_id)

    messages = {
        "warned": (
            "⚠️ *Aviso 1 de 2*\n\n"
            "Sua mensagem foi identificada como fora do contexto.\n"
            "Por favor, mantenha as interações relacionadas ao tema de estudo.\n\n"
            "_Uma nova infração resultará em restrição de acesso._"
        ),
        "blocked_partial": (
            "🚫 *Aviso 2 de 2 — Restrição Ativada*\n\n"
            "O acesso ao assistente de IA foi bloqueado.\n"
            "Você ainda pode acessar os conteúdos e quizzes.\n\n"
            "_Próxima infração resultará em bloqueio total._"
        ),
        "blocked": (
            "🔒 *Acesso Bloqueado*\n\n"
            "Seu acesso foi bloqueado por infrações repetidas.\n"
            "Entre em contato com o professor para reativação."
        )
    }

    return new_status, messages.get(new_status, "")

def can_use_ai(user_id: int):
    status = get_status(user_id)
    return status in ("active", "warned")

def is_blocked(user_id: int):
    return get_status(user_id) == "blocked"