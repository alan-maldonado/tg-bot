from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

TOKEN = os.getenv("BOT_TOKEN")

# --- HANDLER DEL BOT ---
async def responder_chueco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    texto = update.message.text.lower()
    if "chueco" in texto:
        respuestas = [
            "¿Quisiste decir *chequito bebé*?",
            "Ufff, se te chuequeó 😳",
            "¿Chueco? Yo diría *chequito exquisito* 😌",
            "Aguas… eso sonó bien chueco 🤭",
            "¿Estás hablando del *chuequin bebé*?",
            "Yo solo escuché: chequito bebé 🍼",
        ]
        respuesta = random.choice(respuestas)
        await update.message.reply_text(respuesta, parse_mode="Markdown")


# --- HEALTHCHECK WEB PARA ZIMA ---
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot OK")


def start_health_server():
    server = HTTPServer(("0.0.0.0", 8080), HealthHandler)
    server.serve_forever()


# --- INICIO DEL BOT ---
if __name__ == "__main__":
    # Arranca el servidor HTTP de healthcheck ANTES de run_polling()
    threading.Thread(target=start_health_server, daemon=True).start()

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_chueco))

    # Esto ya bloquea el hilo principal
    app.run_polling()
