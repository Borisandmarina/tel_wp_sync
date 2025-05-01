# tel_wp_sync/config.py
import os

# Telegram bot
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ADMIN_IDS = list(map(int, os.environ.get("ADMIN_IDS", "").split(",")))

# WordPress (using Application Passwords)
WP_API_URL = os.environ.get("WP_API_URL")  # e.g., https://your-site.com/wp-json/wp/v2/pages
WP_USERNAME = os.environ.get("WP_USERNAME")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD")
WP_PAGE_ID = int(os.environ.get("WP_PAGE_ID", 0))
MEDIA_BASE_URL = os.environ.get("MEDIA_BASE_URL")