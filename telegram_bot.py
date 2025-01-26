from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Токен Telegram-бота
TELEGRAM_TOKEN = "7630248463:AAFglqL49RCV1YGrWlDJoQJQyOFfo7Sy1Xw"

# Твой Telegram ID (администратор)
ADMIN_ID = 7408403903

# Словарь для хранения истории чата
chat_history = {}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    chat_history[user_id] = []  # Инициализируем историю чата для пользователя
    await update.message.reply_text(
        "Привет! Я ваш бот. Напишите /help, чтобы узнать, что я умею, "
        "или используйте одну из команд для начала общения."
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = (
        "Вот список доступных команд:\n"
        "/start - Начать общение с ботом\n"
        "/help - Узнать, что я умею\n"
        "/ask - Задать вопрос боту\n"
        "/about - Узнать больше о боте\n"
        "/feedback - Отправить отзыв\n"
        "/cancel - Выйти из режима отправки отзыва\n"
        "/reset - Сбросить текущую историю\n"
        "/facts - Узнать интересный факт"
    )
    await update.message.reply_text(commands)

# Команда /reset
async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id in chat_history:
        chat_history[user_id] = []  # Очищаем историю чата
        await update.message.reply_text("История общения сброшена. Теперь мы можем начать с чистого листа!")
    else:
        await update.message.reply_text("У вас ещё нет истории общения. Напишите что-нибудь!")

# Команда /ask
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    chat_history.setdefault(user_id, [])  # Инициализируем историю, если её нет
    chat_history[user_id].append(update.message.text)  # Сохраняем сообщение только по команде /ask
    await update.message.reply_text("Ваш вопрос записан. В будущем я научусь на него отвечать!")

# Команда /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Я бот, созданный для общения и помощи. В будущем я смогу выполнять ещё больше задач, "
        "включая поиск информации, подсказки по учёбе и многое другое!"
    )

# Команда /feedback
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Напишите ваш отзыв, и я отправлю его разработчику. Чтобы выйти из режима отправки отзыва, напишите /cancel."
    )

# Команда /facts
async def facts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    fact = (
        "Знаете ли вы, что у осьминогов три сердца? "
        "Два из них перекачивают кровь через жабры, а третье — по всему телу!"
    )
    await update.message.reply_text(f"Интересный факт: {fact}")

# Обработка текстовых сообщений
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Я не понимаю этого сообщения. Напишите /help, чтобы узнать, что я умею.")

# Настройка бота
def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ask", ask))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("feedback", feedback))
    application.add_handler(CommandHandler("reset", reset))
    application.add_handler(CommandHandler("facts", facts))

    # Обработчик текстовых сообщений (не записываем в историю)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
