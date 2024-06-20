import telebot
import subprocess

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_BOT_TOKEN = '6871811896:AAEdMOsg6-B5DqikpWuS2LCEqvwKOweX1z8'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a command and I will execute it on the server.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    command = message.text
    try:
        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        response = result.stdout if result.stdout else result.stderr
    except Exception as e:
        response = str(e)

    # Send the result back to the user
    bot.reply_to(message, response)

if __name__ == '__main__':
    bot.polling()
