import os
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text('🎉 Бот работает!')

def main():
    if not BOT_TOKEN:
        print("❌ Ошибка: BOT_TOKEN не установлен!")
        return
        
    # Убираем use_context - он больше не нужен
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    print("✅ Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
