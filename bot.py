import os
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def start(update, context):
    await update.message.reply_text('🎉 Бот работает на Render!')

def main():
    if not BOT_TOKEN:
        print("❌ Ошибка: BOT_TOKEN не установлен!")
        return
        
    # Современный способ для новых версий
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    
    print("✅ Бот запущен!")
    
    # Запускаем опрос
    application.run_polling()

if __name__ == '__main__':
    main()
