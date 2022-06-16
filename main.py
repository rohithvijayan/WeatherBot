from telegram.ext import *

import bot_responses as R
import constants as keys

print("Bot Started..")


def start_command(update, context):
    update.message.reply_text('Hello There!\nThis is Weather Bot\nEnter The City Name To Get Real-Time Weather Updates')


def help_command(update, context):
    update.message.reply_text('Go ask Google!')

def handle_weather(update, context):
    city = str(update.message.text).lower()
    weather_data = R.weather(city)
    if 'Clear' in weather_data:
        update.message.reply_text(weather_data)
        update.message.reply_animation("https://tenor.com/bGZYe.gif", 'Animation')
    elif any(a in weather_data for a in ('Haze','Mist','Fog')):
        update.message.reply_text(weather_data)
        update.message.reply_animation("https://tenor.com/0BRE.gif", 'Animation')
    elif 'Cloud' in  weather_data:
        update.message.reply_text(weather_data)
        update.message.reply_animation("https://tenor.com/bSAfU.gif", 'Animation')
    elif any(c in weather_data for c in ('Rain','Shower','Drizzle')):
        update.message.reply_text(weather_data)
        update.message.reply_animation("https://tenor.com/N2OK.gif", 'Animation')
    elif'Thunderstorm' in weather_data:
        update.message.reply_text(weather_data)
        update.message.reply_animation("https://tenor.com/bdzkS.gif", 'Animation')
    elif any(e in weather_data for e in ('Snow', 'Sleet')):
        update.message.reply_text(weather_data)
        update.message.reply_animation("https://tenor.com/37Ql.gif", 'Animation')
    elif 'Sun' in weather_data:
        update.message.reply_text(weather_data)
        update.message.reply_animation("blob:https://tenor.com/492013a0-e176-4f35-a4f6-fa33dd7bd260", 'Animation')
    elif 'Dust' in weather_data:
        update.message.reply_text(weather_data)
        update.message.reply_animation("https://tenor.com/bKOXg.gif", 'Animation')

def error(update, context):
    print(f"update{update}caused error{context.error}")


def main():
    updater = Updater(keys.api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    # dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text, handle_weather))
    dp.add_error_handler(error)
    updater.start_polling(0)
    updater.idle()


main()
