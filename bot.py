from telegram.ext import (
    Updater, 
    MessageHandler, 
    CommandHandler, 
    CallbackQueryHandler, 
    Filters, 
    )

from handlers import (
    start,
    get_info,
    back,
    nextn,
    shop,
    sotib_olish,
    about,
    us_about,
    the_about,
    ortga3,
    contact,
    cart,
    card,
    clear_cart,
    order,
    brand,
    oldin,
    keyin,
    ortga2,
    add_cart,
    menyu,
    phone_number,
    email,
    location,adress,
    clost
    )

import os
from settings import TOKEN

updater = Updater(TOKEN)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CallbackQueryHandler(get_info,pattern="tel"))
dp.add_handler(CallbackQueryHandler(back,pattern="back"))
dp.add_handler(CallbackQueryHandler(nextn,pattern="nextn"))
dp.add_handler(CallbackQueryHandler(shop,pattern="shop"))
dp.add_handler(CallbackQueryHandler(sotib_olish,pattern="sotib_olish"))
dp.add_handler(CallbackQueryHandler(about,pattern="about"))
dp.add_handler(CallbackQueryHandler(us_about,pattern="us_about"))
dp.add_handler(CallbackQueryHandler(the_about,pattern="the_about"))
dp.add_handler(CallbackQueryHandler(ortga3,pattern="ortga3"))
dp.add_handler(CallbackQueryHandler(contact,pattern="contact"))
dp.add_handler(CallbackQueryHandler(cart,pattern="cart"))
dp.add_handler(CallbackQueryHandler(card,pattern="card"))
dp.add_handler(CallbackQueryHandler(clear_cart,pattern="clear_cart"))
dp.add_handler(CallbackQueryHandler(order,pattern="order"))
dp.add_handler(CallbackQueryHandler(brand,pattern="brand"))
dp.add_handler(CallbackQueryHandler(oldin,pattern="oldin"))
dp.add_handler(CallbackQueryHandler(keyin,pattern="keyin"))
dp.add_handler(CallbackQueryHandler(ortga2,pattern="ortga2"))
dp.add_handler(CallbackQueryHandler(add_cart,pattern="add_cart"))
dp.add_handler(CallbackQueryHandler(phone_number,pattern="phone_number"))
dp.add_handler(CallbackQueryHandler(email,pattern="email"))
dp.add_handler(CallbackQueryHandler(adress,pattern="adress"))
dp.add_handler(CallbackQueryHandler(location,pattern="location"))
dp.add_handler(CallbackQueryHandler(clost,pattern="clost"))
dp.add_handler(CallbackQueryHandler(menyu))


updater.start_polling()
updater.idle()