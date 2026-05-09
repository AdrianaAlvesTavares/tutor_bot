from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.user_service import get_or_create, is_blocked, can_use_ai, register_infraction
from services.moderation_service import is_inappropriate
from services.ai_service import ask_tutor

BACK_BUTTON = InlineKeyboardMarkup([[
    InlineKeyboardButton("⬅️ Menu", callback_data="menu_main")
]])

_AI_BLOCKED_TEXT = (
    "🚫 *Acesso à IA bloqueado.*\n\n"
    "Você ainda pode usar os módulos de conteúdo e os quizzes."
)


async def handle_message(update, context):
    # type: (Update, ContextTypes.DEFAULT_TYPE) -> None
    user = update.effective_user
    text = update.message.text

    get_or_create(user.id, user.username or "")

    if is_blocked(user.id):
        await update.message.reply_text(
            "🔒 Acesso bloqueado.",
            reply_markup=BACK_BUTTON,
        )
        return

    if is_inappropriate(text):
        _, warn_text = register_infraction(user.id)
        await update.message.reply_text(
            warn_text,
            parse_mode="Markdown",
            reply_markup=BACK_BUTTON,
        )
        return

    if not can_use_ai(user.id):
        await update.message.reply_text(
            _AI_BLOCKED_TEXT,
            parse_mode="Markdown",
            reply_markup=BACK_BUTTON,
        )
        return

    thinking = await update.message.reply_text("🤖 Consultando o tutor...")
    answer = await ask_tutor(text)
    await thinking.edit_text(answer)


async def ai_ask_callback(update, context):
    # type: (Update, ContextTypes.DEFAULT_TYPE) -> None
    query = update.callback_query
    await query.answer()

    user = update.effective_user

    if not can_use_ai(user.id):
        await query.edit_message_text(
            _AI_BLOCKED_TEXT,
            parse_mode="Markdown",
            reply_markup=BACK_BUTTON,
        )
        return

    await query.edit_message_text(
        "💬 Digite sua dúvida sobre Banco de Dados e eu respondo!",
        reply_markup=BACK_BUTTON,
    )
