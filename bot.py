from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,CallbackContext,Filters,MessageHandler,CallbackQueryHandler
import json
import os
TOKEN=os.environ.get("TOKEN")
from db import DB
db=DB("data.json")
updater=Updater(TOKEN)
dp=updater.dispatcher
def start(update,context):
    chat_id=update.message.chat.id
    bot=context.bot
    shop=InlineKeyboardButton(text="🛍 Shop",callback_data="shop")
    cart=InlineKeyboardButton(text="📦 Cart",callback_data="cart")
    contact=InlineKeyboardButton(text="📞 Contact",callback_data="contact")
    about=InlineKeyboardButton(text="📝 About",callback_data="about")
    keyboard=InlineKeyboardMarkup([[
        shop,cart],[contact,about]
    ],resize_keyboard=True)
    text="Assalomu alaykum botimizga xush kelibsiz! \nBu yerda uzingizga yoqan smartphoneni tanlaysiz degan umidaman. Iltimos uzingizga yoqan menyuni tanlang."
    bot.sendMessage(chat_id=chat_id, text=text,reply_markup=keyboard)

def menyu(update:Update,context:CallbackContext):
    query=update.callback_query
    bot = context.bot
    callback_data=query.data
    if callback_data=="shop":
        l=[]
        for i in db.get_tables():
            i=InlineKeyboardButton(text=i,callback_data=i)
            l.append([i])
        ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
        
        l.append([ortga])
        keyboard=InlineKeyboardMarkup(l,resize_keyboard=True)
        text="Siz |🛍 Shop| bulimini tanladingiz.\nIltimos kerakli Smartphone ni tanlang!"
        query.edit_message_text(text=text,reply_markup=keyboard)
    elif callback_data=="about":
        about_us=InlineKeyboardButton(text="About us",callback_data="about_us")
        about_the_bot=InlineKeyboardButton(text="About the bot",callback_data="about_the_bot")
        ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
        keyboard=InlineKeyboardMarkup([
                [about_us,about_the_bot],[ortga]
            ],resize_keyboard=True)
        db.get_tables()
        text="Siz |📝 About| bulimini tanladingiz.\nIltimos kerakli bulimni tanlang!"
        query.edit_message_text(text=text,reply_markup=keyboard)
    elif callback_data=="ortga":
        query=update.callback_query
        shop=InlineKeyboardButton(text="🛍 Shop",callback_data="shop")
        cart=InlineKeyboardButton(text="📦 Cart",callback_data="cart")
        contact=InlineKeyboardButton(text="📞 Contact",callback_data="contact")
        about=InlineKeyboardButton(text="📝 About",callback_data="about")
        keyboard=InlineKeyboardMarkup([[
            shop,cart],[contact,about]
        ],resize_keyboard=True)
        text="Assalomu alaykum botimizga xush kelibsiz! \nBu yerda uzingizga yoqan smartphoneni tanlaysiz degan umidaman. Iltimos uzingizga yoqan menyuni tanlang."
        query.edit_message_text(text=text,reply_markup=keyboard)
    elif callback_data=="ortga1":
        l=[]
        for i in db.get_tables():
            i=InlineKeyboardButton(text=i,callback_data=i)
            l.append([i])
        ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
        
        l.append([ortga])
        keyboard=InlineKeyboardMarkup(l,resize_keyboard=True)
        text="Siz |🛍 Shop| bulimini tanladingiz.\nIltimos kerakli Smartphone ni tanlang!"
        query.edit_message_text(text=text,reply_markup=keyboard)
    a=[]
    if callback_data=="ortga2":
        query=update.callback_query
        bot=context.bot
        chat_id=query.message.chat.id
        l=[]
        for i in db.get_tables():
            i=InlineKeyboardButton(text=i,callback_data=i)
            l.append([i])
        ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
        
        l.append([ortga])
        keyboard=InlineKeyboardMarkup(l,resize_keyboard=True)
        text="Siz |🛍 Shop| bulimini tanladingiz.\nIltimos kerakli Smartphone ni tanlang!"
        query.delete_message()
        bot.sendMessage(chat_id=chat_id,text=text,reply_markup=keyboard)
    a=[]
    for i in db.get_tables():
        a.append(i)
    if callback_data in a:
        brand=callback_data
        brand :locals
        text1="Siz "+callback_data+" telifonini tanladingiz. Biz sizga maslahat beradigan telifonlar quydagilardan ibora "+str(db.get_phone_list(callback_data))+" Iltimos o'zindz istagan telifonni tanlang!"
        k=[]
        x=db.get_phone_list(callback_data)
        for j in range(10):
            a=InlineKeyboardButton(text=x[j].split(',')[0],callback_data=f'tel {callback_data},'+x[j].split(',')[1])
            k.append([a])
        ortga1=InlineKeyboardButton(text="Ortga",callback_data="ortga1")
        k.append([ortga1])
        keyboard1=InlineKeyboardMarkup(k,resize_keyboard=True)
        query.edit_message_text(text=text1,reply_markup=keyboard1)

def get_info(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    callback_data=query.data[4:]
    brand,id=callback_data.split(",")
    dic=db.getPhone(brand,id)
    imj=dic["img_url"]
    ortga2=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[ortga2]],resize_keyboard=True)
    text=f'Smartfon nomi  {dic["name"]}\nIshlab chiqargan kompaniya  {dic["company"]}\nRangi  {dic["color"]}\nRAM  {dic["RAM"]}\nXotira  {dic["memory"]}\nprice  {dic["price"]}'
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=imj,caption=text,reply_markup=keyboard)
    
def contact(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    phone_number=InlineKeyboardButton(text="Phone number",callback_data="phone_number")
    adress=InlineKeyboardButton(text="Adress",callback_data="adress")
    location=InlineKeyboardButton(text="Location",callback_data="location")
    email=InlineKeyboardButton(text="Email",callback_data="email")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    keyboard=InlineKeyboardMarkup([
            [phone_number,adress],[location,email],[ortga]
        ],resize_keyboard=True)
    text="Siz |📞 Contact| bulimini tanladingiz.\nIltimos kerakli bulimni tanlang!"
    query.edit_message_text(text=text,reply_markup=keyboard)

def cart(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot   
    cart1=InlineKeyboardButton(text="Cart",callback_data="cart1")
    order=InlineKeyboardButton(text="Order",callback_data="order")
    clear_cart=InlineKeyboardButton(text="Clear cart",callback_data="clear_cart")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    keyboard=InlineKeyboardMarkup([
            [cart1,order],[clear_cart,ortga]
        ],resize_keyboard=True)
    text="Siz |📦 Cart| bulimini tanladingiz.\nIltimos kerakli bulimni tanlang!"
    query.edit_message_text(text=text,reply_markup=keyboard)    



dp.add_handler(CommandHandler("start",start))
dp.add_handler(CallbackQueryHandler(get_info,pattern="tel"))
dp.add_handler(CallbackQueryHandler(contact,pattern="contact"))
dp.add_handler(CallbackQueryHandler(cart,pattern="cart"))
dp.add_handler(CallbackQueryHandler(menyu))

updater.start_polling()
updater.idle()