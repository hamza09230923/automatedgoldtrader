import asyncio
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- Configuration ---
# IMPORTANT: Replace 'YOUR_API_TOKEN_HERE' with the actual API token you got from BotFather.
TELEGRAM_TOKEN = '8160503700:AAHp1lEw27l2Yaug18flKVCKb87rqAg3tVc'


# --- Bot Functions ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message when the /start command is issued."""
    await update.message.reply_text('Hi! I am your trading bot. I am now listening for signals.')
    print("Received /start command")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Prints any message the bot receives. This is where we will parse signals later."""
    # Get the text of the message
    message_text = update.message.text

    # Print it to your PyCharm console
    print(f"Received Message: \n---\n{message_text}\n---")

    # In the future, we will add signal parsing logic here.
    # For now, we just acknowledge the message.
    await update.message.reply_text(f"Message received.")


def main() -> None:
    """Start the bot."""
    print("Starting bot...")

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non-command i.e message - echo the message on Telegram
    # We use filters.TEXT and not filters.COMMAND to make sure we only handle text messages.
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    print("Bot is running. Press Ctrl+C to stop.")
    application.run_polling()


if __name__ == '__main__':
    main()