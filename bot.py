from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from handlers import (
    start, test_yaratish, bosh_sahifa, oddiy_test, fanli_test, maxsus_test, blok_test, sozlanmalar, javoblar,
    admin, pullik, oddiy_test_tuzish, fan, fanli_test_tuzish, blok_test_tuzish, maxsus_test_tuzish, maxsus_baza, maxsus_baza_kiritish,
    javoblarni_tekshir, tekshirish, ismkiritish, ismnibazaga, cancel,famkiritish,famnibazaga,famqushish,
    manzilniqushish,manzilqushish,raqamqushish
)
from settings import TOKEN

FAN, ISMNI_BAZAGA, ISMNI_BAZAGA_QUSH, FAMNI_BAZAGA_QUSH, MANNI_BAZAGA_QUSH, TELNI_BAZAGA_QUSH, FAMNI_BAZAGA, ODDIY_TEST_TUZISH, FANLI_TEST_TUZISH, MAXSUS_BAZA_KIRITISH, BLOK_TEST_TUZISH, MAXSUS_TEST_TUZISH, JAVOBLARNI_TEKSHIRISH, TEKSHIRISH, MAXSUS_BAZA,JAVOBLAR_KODI = range(16)


import os
from settings import TOKEN

updater = Updater(TOKEN)

dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text("✍️ Test yaratish"), test_yaratish))
dp.add_handler(MessageHandler(Filters.text("♻️ Orqaga"), bosh_sahifa))
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
        ODDIY_TEST_TUZISH: [MessageHandler(Filters.text & ~Filters.command, oddiy_test_tuzish)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
conv_handler2 = ConversationHandler(
    entry_points=[MessageHandler(Filters.text("📕 Fanli test"), fanli_test)],
    states={
        FAN: [MessageHandler(Filters.text & ~Filters.command, fan)],
        FANLI_TEST_TUZISH: [MessageHandler(Filters.text & ~Filters.command, fanli_test_tuzish)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
conv_handler3 = ConversationHandler(
    entry_points=[MessageHandler(Filters.text("📅 Maxsus test"), maxsus_test)],
    states={
        MAXSUS_BAZA: [MessageHandler(Filters.text("✅ Davom etish"), maxsus_baza)],
        MAXSUS_BAZA_KIRITISH: [MessageHandler(Filters.text & ~Filters.command, maxsus_baza_kiritish)],
        MAXSUS_TEST_TUZISH: [MessageHandler(Filters.photo | Filters.document, maxsus_test_tuzish)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)    
conv_handler4 = ConversationHandler(
    entry_points=[MessageHandler(Filters.text("📚 Blok test"), blok_test)],
    states={
        BLOK_TEST_TUZISH: [MessageHandler(Filters.text & ~Filters.command, blok_test_tuzish)],
        
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

dp.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar"), sozlanmalar))
dp.add_handler(MessageHandler(Filters.text("👨‍💻 Admin"), admin))
dp.add_handler(MessageHandler(Filters.text("📟 Pullik kanallar"), pullik))
dp.add_handler(conv_handler7)
dp.add_handler(conv_handler6)
dp.add_handler(conv_handler5)
dp.add_handler(conv_handler4)
dp.add_handler(conv_handler3)
dp.add_handler(conv_handler2)
dp.add_handler(conv_handler1)
dp.add_handler(conv_handler0)


updater.start_polling()
updater.idle()