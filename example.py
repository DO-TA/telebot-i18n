"""Example Telegram bot using TeleBot-i18n for internationalization."""

import telebot
from telebot_i18n import TeleBotI18n

BOT_TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)
i18n = TeleBotI18n("locales")


def get_lang(message) -> str:
    """Detect user language from Telegram, defaulting to English."""
    lang = message.from_user.language_code or "en"
    # Telegram returns 'fa-IR', 'fa-AF', etc. — extract base code
    return lang.split("-")[0]


@bot.message_handler(commands=["start"])
def handle_start(message):
    lang = get_lang(message)
    name = message.from_user.first_name or "there"
    text = i18n.get_text(lang, "welcome", name=name)
    bot.reply_to(message, text)


@bot.message_handler(commands=["settings"])
def handle_settings(message):
    lang = get_lang(message)
    text = i18n.get_text(lang, "menu_settings")
    bot.reply_to(message, text)


if __name__ == "__main__":
    print("Bot is running…")
    bot.infinity_polling()
