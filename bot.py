from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
import os

# Получаем токен из переменных окружения с запасным вариантом
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8410381008:AAHXkUJcn8jAtfdzAE8d2zBBPArTOlE0ha4')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🚀 Бот работает на Render! Команды:\n'
        '/start - начать\n'
        '/joke - случайная шутка\n'
        '/info - информация о боте'
    )

async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
        "Как называют программиста, который боится женщин? SQL инъектор!",
        "Почему Python лучше JavaScript? Потому что в Python есть import antigravity!",
        "Сколько программистов нужно, чтобы вкрутить лампочку? Ни одного, это hardware проблема!"
    ]
    random_joke = random.choice(jokes)
    await update.message.reply_text(f"🎭 Шутка:\n{random_joke}")

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Этот бот размещен на Render.com и работает 24/7!")

def main():
    # Создаем приложение
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("joke", joke_command))
    app.add_handler(CommandHandler("info", info_command))
    
    # Запускаем бота
    print("✅ Бот запущен на Render!")
    app.run_polling()

if __name__ == '__main__':
    main()
