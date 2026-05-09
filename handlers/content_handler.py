from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from data.content import MODULES


async def content_callback(update, context):
    # type: (Update, ContextTypes.DEFAULT_TYPE) -> None
    query = update.callback_query
    await query.answer()

    module_id = query.data[len("content_"):]
    module = MODULES.get(module_id)

    if not module:
        await query.edit_message_text("❌ Módulo não encontrado.")
        return

    text = (
        "*{}*\n\n"
        "{}\n\n"
        "📌 *Exemplo:*\n"
        "```\n{}\n```"
    ).format(module["title"], module["text"], module["example"])

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "🎯 Fazer Quiz deste módulo",
            callback_data="quiz_start_{}".format(module_id),
        )],
        [InlineKeyboardButton("⬅️ Voltar aos Módulos", callback_data="menu_modules")],
    ])

    await query.edit_message_text(
        text,
        parse_mode="Markdown",
        reply_markup=keyboard,
    )
