import os
import logging
import signal
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🎉 Бот работает на актуальной версии PTB!')

def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN не установлен!")
        return

    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    
    # Функция для корректного завершения работы
    def signal_handler(signum, frame):
        logger.info("Получен сигнал остановки...")
        application.stop_running()

    # Регистрируем обработчик сигналов
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    logger.info("✅ Бот запущен!")
    application.run_polling()

if __name__ == '__main__':
    main()
