from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")

async def responder_chueco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return  # ignora si no hay texto

    texto = update.message.text.lower()
    if "chueco" in texto:
        await update.message.reply_text("¿Quisiste decir *chequito bebé*?", parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_chueco))

app.run_polling()
