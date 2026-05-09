from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from database.db import upsert_user
from data.content import MODULES

ABOUT_TEXT = (
    "🤖 *Tutor de Banco de Dados*\n\n"
    "Sou um bot educacional para te ajudar a aprender BD do zero!\n\n"
    "O que posso fazer:\n"
    "📚 *Módulos* — conteúdo explicado em texto sobre BD e SQL\n"
    "🎯 *Quiz* — questões por módulo para testar seu conhecimento\n"
    "💬 *IA* — tire dúvidas com inteligência artificial\n\n"
    "Use o menu abaixo para começar!"
)


def _build_main_menu():
    keyboard = [
        [InlineKeyboardButton("📚 Ver Módulos", callback_data="menu_modules")],
        [InlineKeyboardButton("🎯 Quiz Rápido", callback_data="menu_modules")],
        [InlineKeyboardButton("ℹ️ Sobre", callback_data="menu_about")],
    ]
    return InlineKeyboardMarkup(keyboard)


def _build_modules_menu():
    sorted_modules = sorted(MODULES.items(), key=lambda item: item[1]["order"])
    keyboard = [
        [InlineKeyboardButton(data["title"], callback_data="content_" + module_id)]
        for module_id, data in sorted_modules
    ]
    keyboard.append([InlineKeyboardButton("⬅️ Voltar", callback_data="menu_main")])
    return InlineKeyboardMarkup(keyboard)


async def start_command(update, context):
    # type: (Update, ContextTypes.DEFAULT_TYPE) -> None
    user = update.effective_user
    upsert_user(user.id, user.username or "")

    await update.message.reply_text(
        "👋 Olá, {}! Bem-vindo ao Tutor de Banco de Dados.".format(user.first_name),
        reply_markup=_build_main_menu(),
    )


async def menu_callback(update, context):
    # type: (Update, ContextTypes.DEFAULT_TYPE) -> None
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "menu_main":
        await query.edit_message_text(
            "🏠 Menu principal:",
            reply_markup=_build_main_menu(),
        )
    elif data == "menu_modules":
        await query.edit_message_text(
            "📚 Escolha um módulo:",
            reply_markup=_build_modules_menu(),
        )
    elif data == "menu_about":
        await query.edit_message_text(
            ABOUT_TEXT,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Voltar", callback_data="menu_main")]]
            ),
        )
