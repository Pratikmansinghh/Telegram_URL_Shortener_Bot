import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pyshorteners

# Define the token for your Telegram bot
TOKEN = '6156081055:AAGUOremQXc2fmxI2FZGgfQBB2ooRB4P4EQ'

# Create an instance of the Bot object
bot = telegram.Bot(token=TOKEN)

# Function to handle /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to URL Shortener Bot!")

# Function to handle incoming messages
def handle_message(update, context):
    # Extract the URL from the message text
    url = update.message.text

    # Shorten the URL using pyshorteners
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)

    # Reply with the shortened URL
    context.bot.send_message(chat_id=update.effective_chat.id, text=shortened_url)

def main():
    # Create an instance of the Updater class
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
