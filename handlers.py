# tel_wp_sync/handlers.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import state
import wordpress
import config

ADMIN_IDS = config.ADMIN_IDS

menu_keyboard = [
    [InlineKeyboardButton("🟢 Показать зелёный", callback_data='show_green')],
    [InlineKeyboardButton("🔴 Показать красный", callback_data='show_red')],
    [InlineKeyboardButton("✏️ Редактировать текст", callback_data='edit_text')],
    [InlineKeyboardButton("🕒 Назначить таймер", callback_data='set_timer')],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        return
    await update.message.reply_text("Выберите действие:", reply_markup=InlineKeyboardMarkup(menu_keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    if user_id not in ADMIN_IDS:
        return

    data = query.data
    if data == 'show_green':
        state.set_state("green")
        wordpress.update_wp()
        await query.edit_message_text("Установлен режим 🟢 Зелёный")
    elif data == 'show_red':
        state.set_state("red")
        wordpress.update_wp()
        await query.edit_message_text("Установлен режим 🔴 Красный")
    elif data == 'edit_text':
        await query.edit_message_text("Введите текст в формате: green|Текст для зелёного\nred|Текст для красного")
        context.user_data['awaiting_text_edit'] = True
    elif data == 'set_timer':
        await query.edit_message_text("Введите время в формате YYYY-MM-DD HH:MM")
        context.user_data['awaiting_timer'] = True

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        return
    text = update.message.text

    if context.user_data.get('awaiting_text_edit'):
        parts = text.strip().split('\n')
        for line in parts:
            try:
                key, val = line.split('|', 1)
                state.set_text(key.strip(), val.strip())
            except:
                continue
        wordpress.update_wp()
        await update.message.reply_text("Тексты обновлены.")
        context.user_data['awaiting_text_edit'] = False

    elif context.user_data.get('awaiting_timer'):
        state.set_timer(text.strip())
        await update.message.reply_text("Таймер установлен.")
        context.user_data['awaiting_timer'] = False


def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
