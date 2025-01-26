from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Токен Telegram-бота
TELEGRAM_TOKEN = "ТВОЙ_ТОКЕН"

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот. Вот мои команды:\n"
                              "/help - Показать список команд\n"
                              "/about - Узнать обо мне\n"
                              "/feedback - Оставить отзыв\n"
                              "/reset - Сбросить историю чата\n"
                              "/facts - Узнать интересный факт")

# Команда /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Список доступных команд:\n"
                              "/start - Начать общение с ботом\n"
                              "/help - Показать список команд\n"
                              "/about - Узнать обо мне\n"
                              "/feedback - Оставить отзыв\n"
                              "/reset - Сбросить историю чата\n"
                              "/facts - Узнать интересный факт")

# Команда /about
def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Я Telegram-бот, созданный для помощи. Пишите, если что-то нужно!")

# Команда /feedback
def feedback(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Спасибо за ваш отзыв! Напишите его в следующем сообщении.")

# Команда /reset
def reset(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("История чата сброшена!")

# Команда /facts
def facts(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Интересный факт: Земля вращается вокруг Солнца со скоростью 30 км/с!")

# Обработка текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Я пока не понимаю, что вы хотите. Попробуйте одну из команд: /help")

# Настройка бота
def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # Обработка команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about))
    dispatcher.add_handler(CommandHandler("feedback", feedback))
    dispatcher.add_handler(CommandHandler("reset", reset))
    dispatcher.add_handler(CommandHandler("facts", facts))

    # Обработка обычных сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
