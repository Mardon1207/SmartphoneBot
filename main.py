from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler,Dispatcher
from handlers import (
    start, test_yaratish, bosh_sahifa, oddiy_test, fanli_test, maxsus_test, blok_test, sozlanmalar, javoblar,
    admin, pullik, oddiy_test_tuzish, fan, fanli_test_tuzish, blok_test_tuzish, maxsus_test_tuzish, maxsus_baza, maxsus_baza_kiritish,
    javoblarni_tekshir, tekshirish, ismkiritish, ismnibazaga, cancel,famkiritish,famnibazaga,famqushish,
    manzilniqushish,manzilqushish,raqamqushish
)
from telegram import Bot,Update
from flask import Flask, request
from settings import TOKEN
bot=Bot
FAN, ISMNI_BAZAGA, ISMNI_BAZAGA_QUSH, FAMNI_BAZAGA_QUSH, MANNI_BAZAGA_QUSH, TELNI_BAZAGA_QUSH, FAMNI_BAZAGA, ODDIY_TEST_TUZISH, FANLI_TEST_TUZISH, MAXSUS_BAZA_KIRITISH, BLOK_TEST_TUZISH, MAXSUS_TEST_TUZISH, JAVOBLARNI_TEKSHIRISH, TEKSHIRISH, MAXSUS_BAZA,JAVOBLAR_KODI = range(16)
app = Flask(__name__)
@app.route('/webhook', methods=["POST", "GET"])

def main():
    if request.method == 'GET':
        return 'hi from Python2022I'
    elif request.method == "POST":
        data = request.get_json(force = True)

        dp: Dispatcher = Dispatcher(bot, None, workers=0)
        update:Update = Update.de_json(data, bot)

        
    # Botni yaratamiz
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher
        

        conv_handler0 = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ISMNI_BAZAGA_QUSH: [MessageHandler(Filters.text, famqushish)],
            FAMNI_BAZAGA_QUSH: [MessageHandler(Filters.text, raqamqushish)],
            TELNI_BAZAGA_QUSH: [MessageHandler(Filters.contact, manzilqushish)],
            MANNI_BAZAGA_QUSH: [CallbackQueryHandler(manzilniqushish)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
)   


        conv_handler1 = ConversationHandler(
            entry_points=[MessageHandler(Filters.text("✍️ Oddiy test"), oddiy_test)],
            states={
                ODDIY_TEST_TUZISH: [MessageHandler(Filters.text, oddiy_test_tuzish)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        conv_handler2 = ConversationHandler(
            entry_points=[MessageHandler(Filters.text("📕 Fanli test"), fanli_test)],
            states={
                FAN: [MessageHandler(Filters.text, fan)],
                FANLI_TEST_TUZISH: [MessageHandler(Filters.text, fanli_test_tuzish)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        conv_handler3 = ConversationHandler(
            entry_points=[MessageHandler(Filters.text("📅 Maxsus test"), maxsus_test)],
            states={
                MAXSUS_BAZA: [MessageHandler(Filters.text("✅ Davom etish"), maxsus_baza)],
                MAXSUS_BAZA_KIRITISH: [MessageHandler(Filters.text, maxsus_baza_kiritish)],
                MAXSUS_TEST_TUZISH: [MessageHandler(Filters.photo | Filters.document, maxsus_test_tuzish)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )    

        conv_handler4 = ConversationHandler(
            entry_points=[MessageHandler(Filters.text("📚 Blok test"), blok_test)],
            states={
                BLOK_TEST_TUZISH: [MessageHandler(Filters.text, blok_test_tuzish)],

            },
            fallbacks=[CommandHandler('cancel', cancel)],
        ) 

        conv_handler5 = ConversationHandler(
            entry_points=[MessageHandler(Filters.text("✅ Javobni tekshirish"), javoblar)],
            states={
                JAVOBLAR_KODI: [MessageHandler(Filters.text, javoblarni_tekshir)],
                JAVOBLARNI_TEKSHIRISH: [MessageHandler(Filters.text, tekshirish)],

            },
            fallbacks=[CommandHandler('cancel', cancel)],
        ) 
        conv_handler6 = ConversationHandler(
            entry_points=[MessageHandler(Filters.text("✍️ Ism"), ismkiritish)],
            states={
                ISMNI_BAZAGA: [MessageHandler(Filters.text, ismnibazaga)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        ) 
        conv_handler7 = ConversationHandler(
            entry_points=[MessageHandler(Filters.text("✍️ Familiya"), famkiritish)],
            states={
                FAMNI_BAZAGA: [MessageHandler(Filters.text, famnibazaga)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        ) 




        
        dp.add_handler(MessageHandler(Filters.text("✍️ Test yaratish"), test_yaratish))
        dp.add_handler(MessageHandler(Filters.text("♻️ Orqaga"), bosh_sahifa))
        dp.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar"), sozlanmalar))
        dp.add_handler(MessageHandler(Filters.text("👨‍💻 Admin"), admin))
        dp.add_handler(MessageHandler(Filters.text("📟 Pullik kanallar"), pullik))
        dp.add_handler(conv_handler0)
        dp.add_handler(conv_handler7)
        dp.add_handler(conv_handler6)
        dp.add_handler(conv_handler5)
        dp.add_handler(conv_handler4)
        dp.add_handler(conv_handler3)
        dp.add_handler(conv_handler2)
        dp.add_handler(conv_handler1)
        
        # Botni polling yordamida ishga tushiramiz
        dp.process_update(update)
        return 'ok'

if __name__=='__main__':
    app.run()