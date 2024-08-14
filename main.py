from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, MessageFilter,Filters
from handlers import (
    start, test_yaratish, bosh_sahifa , oddiy_test , fanli_test, maxsus_test, blok_test, sozlanmalar, javoblar,
    admin, pullik, oddiy_test_tuzish, fan, fanli_test_tuzish,blok_test_tuzish,maxsus_test_tuzish,maxsus_baza,maxsus_baza_kiritish,
    javoblarni_tekshir,tekshirish,ismkiritish,ismnibazaga
)
from settings import TOKEN

def main():
    # Botni yaratamiz
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlerlarni qo'shamiz
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler( Filters.text("✍️ Test yaratish"),test_yaratish))
    dp.add_handler(MessageHandler( Filters.text("♻️ Orqaga"),bosh_sahifa))
    dp.add_handler(MessageHandler( Filters.text("✍️ Oddiy test"),oddiy_test))
    dp.add_handler(MessageHandler( Filters.text("📕 Fanli test"),fanli_test))
    dp.add_handler(MessageHandler( Filters.text("📅 Maxsus test"),maxsus_test))
    dp.add_handler(MessageHandler( Filters.text("📚 Blok test"),blok_test))
    dp.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar"),sozlanmalar))
    dp.add_handler(MessageHandler(Filters.text("✅ Javobni tekshirish"),javoblar))
    dp.add_handler(MessageHandler(Filters.text("👨‍💻 Admin"),admin))
    dp.add_handler(MessageHandler(Filters.text("📟 Pullik kanallar"),pullik))
    dp.add_handler(MessageHandler(Filters.text("✍️ Ism va familiya"),ismkiritish))
    dp.add_handler(MessageHandler(Filters.regex(r'\_'),ismnibazaga))
    dp.add_handler(MessageHandler(Filters.regex(r'\!'),fan))
    dp.add_handler(MessageHandler(Filters.regex(r'\+'),oddiy_test_tuzish))
    dp.add_handler(MessageHandler(Filters.regex(r'\-'),fanli_test_tuzish))
    dp.add_handler(MessageHandler(Filters.regex(r'\*'),maxsus_baza_kiritish))
    dp.add_handler(MessageHandler(Filters.regex(r'\:'),blok_test_tuzish))
    dp.add_handler(MessageHandler(Filters.photo,maxsus_test_tuzish))
    dp.add_handler(MessageHandler(Filters.document,maxsus_test_tuzish))
    dp.add_handler(MessageHandler(Filters.text("✅ Davom etish"),maxsus_baza))
    dp.add_handler(MessageHandler(Filters.regex(r'\.'),javoblarni_tekshir))
    dp.add_handler(MessageHandler(Filters.text,tekshirish))
    # Botni polling yordamida ishga tushiramiz
    updater.start_polling()

    # Botni to'xtatish uchun signal kutamiz
    updater.idle()

if __name__ == "__main__":
    main()
