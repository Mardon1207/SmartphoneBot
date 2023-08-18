import telegram

import os 
from settings import token
url = "https://backend2023f.pythonanywhere.com/setwebhook/"


bot = telegram.Bot(token)


# bot.delete_webhook()
bot.set_webhook(url)
print(bot.get_webhook_info())