# tel_wp_sync/bot.py

from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
import config
import scheduler

if __name__ == '__main__':
    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()
    setup_handlers(app)
    scheduler.start_timer_check(app)
    print("Bot started...")
    app.run_polling()
