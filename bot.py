from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
import os

# Получаем токен
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8410381008:AAHXkUJcn8jAtfdzAE8d2zBBPArTOlE0ha4')

def start_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        '🚀 Бот работает на Render! Команды:\n'
        '/start - начать\n'
        '/joke - случайная шутка\n'
        '/info - информация о боте'
    )

def joke_command(update: Update, context: CallbackContext):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
        "Как называют программиста, который боится женщин? SQL инъектор!",
        "Почему Python лучше JavaScript? Потому что в Python есть import antigravity!",
        "Сколько программистов нужно, чтобы вкрутить лампочку? Ни одного, это hardware проблема!"
    ]
    random_joke = random.choice(jokes)
    update.message.reply_text(f"🎭 Шутка:\n{random_joke}")

def info_command(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Этот бот размещен на Render.com и работает 24/7!")

def main():
    # Создаем updater
    updater = Updater(BOT_TOKEN, use_context=True)
    
    # Получаем dispatcher для регистрации обработчиков
    dp = updater.dispatcher
    
    # Добавляем обработчики
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("joke", joke_command))
    dp.add_handler(CommandHandler("info", info_command))
    
    # Запускаем бота
    print("✅ Бот запущен на Render!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
