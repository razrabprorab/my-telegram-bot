from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN', '8410381008:AAHXkUJcn8jAtfdzAE8d2zBBPArTOlE0ha4')

def start(update, context):
    update.message.reply_text('✅ Бот работает на Render! Используй /joke')

def joke(update, context):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Oct 31 == Dec 25!",
        "Сколько программистов нужно для лампочки? Ни одного - это hardware проблема!"
    ]
    import random
    update.message.reply_text(random.choice(jokes))

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("joke", joke))
    
    print("✅ Бот запущен на Render!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
