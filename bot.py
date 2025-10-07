import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# Создаем Flask-приложение для работы с портом
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    # Сервер запускается на порте, который предоставляет Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

def start_flask():
    t = Thread(target=run_flask)
    t.daemon = True  # Поток будет завершен вместе с основным
    t.start()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🎉 Бот работает!')

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN не установлен!")
        return

    # Запускаем HTTP-сервер в фоне
    start_flask()

    # Запускаем Telegram-бота
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    
    print("✅ Бот запущен!")
    application.run_polling()

if __name__ == '__main__':
    main()
