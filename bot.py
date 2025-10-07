import os
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.environ.get('8410381008:AAHXkUJcn8jAtfdzAE8d2zBBPArTOlE0ha4')

def start(update, context):
    update.message.reply_text('🎉 Бот работает!')

def main():
    if not BOT_TOKEN:
        print("❌ Ошибка: BOT_TOKEN не установлен!")
        return
        
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    print("✅ Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
