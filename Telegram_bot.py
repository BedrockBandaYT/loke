import logging
import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_BOT_TOKEN = '6871811896:AAEdMOsg6-B5DqikpWuS2LCEqvwKOweX1z8'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define command handler for the start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a command and I will execute it on the server.')

# Define a function to handle the incoming messages
def handle_message(update: Update, context: CallbackContext) -> None:
    command = update.message.text
    try:
        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        response = result.stdout if result.stdout else result.stderr
    except Exception as e:
        response = str(e)

    # Send the result back to the user
    update.message.reply_text(response)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on noncommand i.e. message - execute the c
