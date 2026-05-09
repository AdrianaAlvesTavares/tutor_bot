from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from config import TELEGRAM_TOKEN
from database.db import init_db
from handlers.menu_handler       import start_command, menu_callback
from handlers.content_handler    import content_callback
from handlers.quiz_handler       import quiz_callback
from handlers.moderation_handler import handle_message, ai_ask_callback


def main():
    init_db()

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(menu_callback,    pattern="^menu_"))
    app.add_handler(CallbackQueryHandler(content_callback, pattern="^content_"))
    app.add_handler(CallbackQueryHandler(quiz_callback,    pattern="^quiz_"))
    app.add_handler(CallbackQueryHandler(ai_ask_callback,  pattern="^ai_ask_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()


if __name__ == "__main__":
    main()
