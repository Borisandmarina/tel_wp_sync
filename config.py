# tel_wp_sync/config.py
import os

# Telegram bot
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ADMIN_IDS = list(map(int, os.environ.get("ADMIN_IDS", "").split(",")))

# WordPress
WP_API_URL = os.environ.get("WP_API_URL")
WP_API_TOKEN = os.environ.get("WP_API_TOKEN")
WP_PAGE_ID = int(os.environ.get("WP_PAGE_ID", 0))
MEDIA_BASE_URL = os.environ.get("MEDIA_BASE_URL")