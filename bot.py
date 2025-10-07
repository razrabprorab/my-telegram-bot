import os
import logging
from telegram.ext import Updater, CommandHandler

# Включаем логирование
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text('🎉 Наконец-то работает!')

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN не установлен!")
        return
    
    try:
        # Старая стабильная версия
        updater = Updater(BOT_TOKEN, use_context=True)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        
        print("✅ Бот ЗАПУЩЕН!")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == '__main__':
    main()
