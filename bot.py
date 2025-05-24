from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
from data.leaderboard import save_time

users_timer = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    users_timer[user_id] = time.time()
    await update.message.reply_text("Уровень 1 запущен. Ссылка на игру: https://example.com/play/1")

async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in users_timer:
        elapsed = time.time() - users_timer[user_id]
        save_time(user_id, elapsed)
        await update.message.reply_text(f"Ты прошел за {elapsed:.2f} секунд!")
    else:
        await update.message.reply_text("Сначала начни игру командой /start")

app = ApplicationBuilder().token("8193788323:AAH4S0vOlGQML0ec0PBrYOLAc6yGmbeCl9U").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("finish", finish))

app.run_polling()