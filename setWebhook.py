from settings import TOKEN
from telegram import Bot
bot = Bot(token=TOKEN)

def get_info():
    print(bot.get_webhook_info())


def delete():
    print(bot.delete_webhook())


def set():
    url = 'https://smm.pythonanywhere.com/setwebhook/'
    print(bot.set_webhook(url=url))

delete()