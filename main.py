from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler

from random import randint

async def comandoStart(update: Update, context: CallbackContext) -> None:
    
    await context.bot.sendMessage(update.effective_chat.id, f"Bienvenido {update.effective_user.username}.")

async def numeroRandom(update: Update, context: CallbackContext) -> None:

    await context.bot.sendMessage(update.effective_chat.id, f"{randint(0, 4096)}")

if __name__ == "__main__":
    token = "5518571798:AAFypL15foLXfnAdkQhacmlL8ZFSI5tDdlo"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", comandoStart))
    app.add_handler(CommandHandler("random", numeroRandom))
    app.run_polling()

