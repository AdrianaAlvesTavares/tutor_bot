from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from data.quizzes import QUIZZES
from data.content import MODULES
from database.db import save_quiz_session

LETTERS = ["A", "B", "C", "D"]


async def _send_question(query, context, module_id, q_index, questions):
    question = questions[q_index]
    total = len(questions)

    options_text = "\n".join(
        "{}) {}".format(LETTERS[i], opt)
        for i, opt in enumerate(question["options"])
    )
    text = "🎯 Questão {} de {}\n\n{}\n\n{}".format(
        q_index + 1, total, question["question"], options_text
    )

    keyboard = [
        [InlineKeyboardButton(
            "{}) {}".format(LETTERS[i], opt),
            callback_data="quiz_answer_{}_{}_{}" .format(module_id, q_index, i),
        )]
        for i, opt in enumerate(question["options"])
    ]

    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))


async def quiz_callback(update, context):
    # type: (Update, ContextTypes.DEFAULT_TYPE) -> None
    query = update.callback_query
    await query.answer()

    data = query.data  # e.g. "quiz_start_sql_basico"

    # ── quiz_start_{module_id} ──────────────────────────────────────────────
    if data.startswith("quiz_start_"):
        module_id = data[len("quiz_start_"):]
        questions = QUIZZES[module_id]
        context.user_data["quiz"] = {
            "module_id": module_id,
            "questions": questions,
            "current": 0,
            "score": 0,
        }
        await _send_question(query, context, module_id, 0, questions)
        return

    # ── quiz_next_{module_id}_{q_index} ────────────────────────────────────
    if data.startswith("quiz_next_"):
        # strip prefix then split from the right to get q_index
        rest = data[len("quiz_next_"):]          # "sql_basico_1"
        module_id, q_str = rest.rsplit("_", 1)
        q_index = int(q_str)
        questions = context.user_data["quiz"]["questions"]
        await _send_question(query, context, module_id, q_index, questions)
        return

    # ── quiz_answer_{module_id}_{q_index}_{answer_index} ───────────────────
    if data.startswith("quiz_answer_"):
        rest = data[len("quiz_answer_"):]        # "sql_basico_1_2"
        parts = rest.rsplit("_", 2)              # ["sql_basico", "1", "2"]
        module_id = parts[0]
        q_index = int(parts[1])
        chosen = int(parts[2])

        quiz = context.user_data["quiz"]
        questions = quiz["questions"]
        question = questions[q_index]
        total = len(questions)
        correct = question["answer"]

        if chosen == correct:
            quiz["score"] += 1
            feedback = "✅ *Correto!*\n\n{}".format(question["explanation"])
        else:
            feedback = "❌ *Errado.* A resposta correta era *{})*\n\n{}".format(
                LETTERS[correct], question["explanation"]
            )

        next_index = q_index + 1
        is_last = next_index >= total

        if not is_last:
            keyboard = InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "➡️ Próxima",
                    callback_data="quiz_next_{}_{}".format(module_id, next_index),
                )
            ]])
            await query.edit_message_text(
                feedback, parse_mode="Markdown", reply_markup=keyboard
            )
        else:
            score = quiz["score"]
            user_id = update.effective_user.id
            save_quiz_session(user_id, module_id, total, score)

            trophy = "🏆" if score == total else "📊"
            module_title = MODULES[module_id]["title"]
            result_text = (
                "{} *Quiz finalizado — {}*\n\n"
                "Você acertou *{} de {}* questões."
            ).format(trophy, module_title, score, total)

            keyboard = InlineKeyboardMarkup([[
                InlineKeyboardButton("⬅️ Menu Principal", callback_data="menu_main")
            ]])
            await query.edit_message_text(
                result_text, parse_mode="Markdown", reply_markup=keyboard
            )
