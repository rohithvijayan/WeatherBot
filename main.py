from telegram.ext import *

import bot_responses as R
import constants as keys

print("Bot Started..")


def start_command(update, context):
    update.message.reply_text('Hello There!\nThis is Weather Bot\nEnter The City Name To Get Real-Time Weather Updates')


def help_command(update, context):
    update.message.reply_text('Go ask Google!')


# def handle_message(update, context):
#     text = str(update.message.text).lower()
#     response = R.response(text)
#     update.message.reply_text(response)

def handle_weather(update,context):
    city=str(update.message.text).lower()
    weather_data=R.weather(city)
    update.message.reply_text(weather_data)

def error(update, context):
    print(f"update{update}caused error{context.error}")


def main():
    updater = Updater(keys.api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    # dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text,handle_weather))
    dp.add_error_handler(error)
    updater.start_polling(0)
    updater.idle()


main()
