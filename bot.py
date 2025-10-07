import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🎉 Бот работает на актуальной версии PTB!')

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN не установлен!")
        return

    # Создаем приложение с использованием современного API
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    
    print("✅ Бот запущен!")
    application.run_polling()

if __name__ == '__main__':
    main()
