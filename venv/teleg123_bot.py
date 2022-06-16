import pprint

import requests
from telegram.ext import updater,commandhandler
bot_token='5393962909:AAG0QiqMGcoUVISDKkfGvn7_uXkLbRJsyhY'
url=f'https://api.telegram.org/bot5393962909:AAG0QiqMGcoUVISDKkfGvn7_uXkLbRJsyhY/getMe'
res=requests.get(url)
pprint.pprint(res.text)
