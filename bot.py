from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,CallbackContext,Filters,MessageHandler,CallbackQueryHandler
import json
import os
# TOKEN=os.environ.get("TOKEN")
TOKEN="5982674757:AAG3Ni9J5Ph1IFEmHjdQLYvhW-IHPIlO-IY"
from db import DB
db=DB("data.json")
from cartdb import Cart
bd=Cart("db.json")
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
    if callback_data=="ortga":
        query=update.callback_query
        shop=InlineKeyboardButton(text="🛍 Shop",callback_data="shop")
        cart=InlineKeyboardButton(text="📦 Cart",callback_data="cart")
        contact=InlineKeyboardButton(text="📞 Contact",callback_data="contact")
        about=InlineKeyboardButton(text="📝 About",callback_data="about")
        keyboard=InlineKeyboardMarkup([[
            shop,cart],[contact,about]
        ],resize_keyboard=True)
        text="Siz Menyuga qaytdingiz. Bulimlardan birini tanlang"
        query.edit_message_text(text=text,reply_markup=keyboard)
    if callback_data=="ortga2":
        chat_id=query.message.chat.id
        l=[]
        for i in db.get_tables():
            i=InlineKeyboardButton(text=i,callback_data="brand,"+i)
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

def get_info(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    callback_data=query.data[4:]
    brand,id=callback_data.split(",")
    dic=db.getPhone(brand,id)
    imj=dic["img_url"]
    k=[]
    id=int(id)
    back=InlineKeyboardButton(text="⏪",callback_data=f"back_{query.data}")
    nextn=InlineKeyboardButton(text="⏩",callback_data=f"nextn_{query.data}")
    lst=db.get_phone_list(brand)
    date=callback_data
    max=len(lst)
    if id>1 and id<max:
        k.append([back,nextn])
    elif id==max:
        k.append([back])
    elif id==1:
        k.append([nextn])
    ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortga2,{callback_data}")
    sotib_olish=InlineKeyboardButton(text="Sotib olish",callback_data="sotib_olish")
    add_cart=InlineKeyboardButton(text="Savatga qo'shish",callback_data=f"add_cart,{brand},{chat_id},{id}")
    k.append([sotib_olish])
    k.append([add_cart])
    k.append([ortga2])
    keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
    text=f'Smartfon nomi  {dic["name"]}\nIshlab chiqargan kompaniya  {dic["company"]}\nRangi  {dic["color"]}\nRAM  {dic["RAM"]}\nXotira  {dic["memory"]}\nprice  {dic["price"]}'
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=imj,caption=text,reply_markup=keyboard)

def back(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    data=query.data[5:]
    callback_data=data[4:]
    brand=callback_data.split(",")[0]
    id=callback_data.split(',')[1]
    id=int(id)
    id=id-1
    dic=db.getPhone(brand,id)
    imj=dic["img_url"]
    k=[]
    back=InlineKeyboardButton(text="⏪",callback_data=f"back_tel {brand},{id}")
    nextn=InlineKeyboardButton(text="⏩",callback_data=f"nextn_tel {brand},{id}")
    lst=db.get_phone_list(brand)
    date=callback_data
    max=len(lst)
    if id>1 and id<max:
        k.append([back,nextn])
    elif id==max:
        k.append([back])
    elif id==1:
        k.append([nextn])
    ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortga2,tel {callback_data}")
    sotib_olish=InlineKeyboardButton(text="Sotib olish",callback_data="sotib_olish")
    add_cart=InlineKeyboardButton(text="Savatga qo'shish",callback_data=f"add_cart,{brand},{chat_id},{id}")
    k.append([sotib_olish])
    k.append([add_cart])
    k.append([ortga2])
    keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
    text=f'Smartfon nomi  {dic["name"]}\nIshlab chiqargan kompaniya  {dic["company"]}\nRangi  {dic["color"]}\nRAM  {dic["RAM"]}\nXotira  {dic["memory"]}\nprice  {dic["price"]}'
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=imj,caption=text,reply_markup=keyboard)

def nextn(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    data=query.data[6:]
    callback_data=data[4:]
    brand=callback_data.split(",")[0]
    id=callback_data.split(',')[1]
    id=int(id)
    id=id+1
    dic=db.getPhone(brand,id)
    imj=dic["img_url"]
    k=[]
    back=InlineKeyboardButton(text="⏪",callback_data=f"back_tel {brand},{id}")
    nextn=InlineKeyboardButton(text="⏩",callback_data=f"nextn_tel {brand},{id}")
    lst=db.get_phone_list(brand)
    date=callback_data
    max=len(lst)
    if id>1 and id<max:
        k.append([back,nextn])
    elif id==max:
        k.append([back])
    elif id==1:
        k.append([nextn])
    ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortga2,{callback_data}")
    sotib_olish=InlineKeyboardButton(text="Sotib olish",callback_data="sotib_olish")
    add_cart=InlineKeyboardButton(text="Savatga qo'shish",callback_data=f"add_cart,{brand},{chat_id},{id}")
    k.append([sotib_olish])
    k.append([add_cart])
    k.append([ortga2])
    keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
    text=f'Smartfon nomi  {dic["name"]}\nIshlab chiqargan kompaniya  {dic["company"]}\nRangi  {dic["color"]}\nRAM  {dic["RAM"]}\nXotira  {dic["memory"]}\nprice  {dic["price"]}'
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=imj,caption=text,reply_markup=keyboard)

def sotib_olish(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    query.answer("Mahsulotni sotib olish uchun so'rov yuborildi!!!")

def shop(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    l=[]
    for i in db.get_tables():
        i=InlineKeyboardButton(text=i,callback_data="brand,"+i)
        l.append([i])
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    l.append([ortga])
    keyboard=InlineKeyboardMarkup(l,resize_keyboard=True)
    text="Siz |🛍 Shop| bulimini tanladingiz.\nIltimos kerakli Smartphone ni tanlang!"
    query.edit_message_text(text=text,reply_markup=keyboard)

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

def about(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    about_us=InlineKeyboardButton(text="About us",callback_data="us_about")
    about_the_bot=InlineKeyboardButton(text="About the bot",callback_data="the_about")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    keyboard=InlineKeyboardMarkup([
            [about_us,about_the_bot],[ortga]
        ],resize_keyboard=True)
    db.get_tables()
    text="Siz |📝 About| bulimini tanladingiz.\nIltimos kerakli bulimni tanlang!"
    query.edit_message_text(text=text,reply_markup=keyboard)

def us_about(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    ortga3=InlineKeyboardButton(text="Ortga",callback_data="ortga3")
    keyboard=InlineKeyboardMarkup([
            [ortga3]
        ],resize_keyboard=True)
    photo="https://thumbs.dreamstime.com/b/ic%C3%B4ne-du-logo-telegram-voronezh-russie-novembre-ronde-en-couleur-bleue-164586026.jpg"
    text="Assalomu alaykum! Bu bot men ya'ni Mardon Sultonov tomonidan tayorlandi.\nMen hozirda TATU talabasiman. Men backend sohasiga qiziqaman va bu botni ishlab chiqdim.\nBotimiz sizga manzur buladi degan umiddaman!"
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=photo,caption=text,reply_markup=keyboard)

def the_about(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    ortga3=InlineKeyboardButton(text="Ortga",callback_data="ortga3")
    keyboard=InlineKeyboardMarkup([
            [ortga3]
        ],resize_keyboard=True)
    photo="https://avatars.githubusercontent.com/u/12576027?v=4.jpg"
    text="Bu bot BotFather tomonidan tayorlandi.\nBu bot orqali siz 100 dan ortiq smartfonlar haqida malumotlarni olishingiz va ularning narxlari bilan tanishingiz mumkun.\nBotimiz sizga manzur buladi degan umiddaman!"
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=photo,caption=text,reply_markup=keyboard)

def ortga3(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    about_us=InlineKeyboardButton(text="About us",callback_data="us_about")
    about_the_bot=InlineKeyboardButton(text="About the bot",callback_data="about_the_bot")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    keyboard=InlineKeyboardMarkup([
            [about_us,about_the_bot],[ortga]
        ],resize_keyboard=True)
    db.get_tables()
    text="Siz |📝 About| bulimini tanladingiz.\nIltimos kerakli bulimni tanlang!"
    query.delete_message()
    bot.sendMessage(chat_id=chat_id,text=text,reply_markup=keyboard)

def cart(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot   
    cart1=InlineKeyboardButton(text="Cart",callback_data="card")
    order=InlineKeyboardButton(text="Order",callback_data="order")
    clear_cart=InlineKeyboardButton(text="Clear cart",callback_data="clear_cart")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    keyboard=InlineKeyboardMarkup([
            [cart1,order],[clear_cart,ortga]
        ],resize_keyboard=True)
    text="Siz |📦 Cart| bulimini tanladingiz.\nIltimos kerakli bulimni tanlang!"
    query.edit_message_text(text=text,reply_markup=keyboard)  

def card(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot 
    data=bd.get_cart(str(chat_id))
    max=len(data)
    text0="Savatga qo'shgan smatfonlaringiz!"
    text1=""
    for i in range(max):
       db_data=db.getPhone(data[i]["brand"],data[i]["doc_id"])
       text1+=f"\n{i+1}.  Smartfon nomi { db_data['name']}  Ishlab chiqargan kompanya {db_data['company']}  rangi {db_data['color']}  xotira {db_data['RAM']}/{db_data['memory']}  narxi {db_data['price']} $" 
    text=text0+text1
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    keyboard=InlineKeyboardMarkup([[ortga]],resize_keyboard=True)
    query.delete_message()
    bot.sendMessage(chat_id=chat_id,text=text,reply_markup=keyboard)
    
def clear_cart(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bd.remove(chat_id)
    query.answer("Savat tozalandi!!!")

def order(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    data=bd.get_cart(str(chat_id))
    max=len(data)
    if max==0:
        query.answer("Sotib olish uchun mahsulotlar yuq!!!")
    else:
        query.answer("Mahsulotlarni sotib olish uchun surov yuborildi!!!")

def brand(update:Update,context:CallbackContext):
    query=update.callback_query
    callback_data=query.data.split(',')[1]
    text1="Siz "+callback_data+" telifonini tanladingiz. Biz sizga maslahat beradigan telifonlar quydagilardan ibora. Iltimos o'zindz istagan telifonni tanlang!"
    k=[]
    x=db.get_phone_list(callback_data)
    b=0
    d=10
    date=callback_data
    m=len(x)
    if m-b-10>=0:
        d=b+10
    elif m-b-10<0:
        d=m
    for j in range(b,d):
        data=db.getPhone(date,j+1)
        a=InlineKeyboardButton(text=f"{x[j].split(',')[0]} {data['color']} {data['RAM']}/{data['memory']}",callback_data=f'tel {callback_data},'+x[j].split(',')[1])
        k.append([a])
    ortga1=InlineKeyboardButton(text="Ortga",callback_data="shop")
    oldin=InlineKeyboardButton(text="⏪",callback_data=f"oldin,{b},{m},{date}")
    keyin=InlineKeyboardButton(text="⏩",callback_data=f"keyin,{b},{m},{date}")
    if b>0 and d<m:
        k.append([oldin,keyin])
    elif b>0 and d>=m:
        k.append([oldin])
    elif b<=0 and d<m:
        k.append([keyin])
    k.append([ortga1])
    keyboard1=InlineKeyboardMarkup(k,resize_keyboard=True)
    query.edit_message_text(text=text1,reply_markup=keyboard1)

def oldin(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot 
    callback_data=query.data.split(',')[3]
    date=callback_data
    x=db.get_phone_list(callback_data)
    k=[]
    b=int(query.data.split(',')[1])
    b=b-10
    m=int(query.data.split(',')[2])
    if m-b-10>=0:
        d=b+10
    elif m-b-10<0:
        d=m
    for j in range(b,d):
        data=db.getPhone(date,j+1)
        a=InlineKeyboardButton(text=f"{x[j].split(',')[0]} {data['color']} {data['RAM']}/{data['memory']}",callback_data=f'tel {callback_data},'+x[j].split(',')[1])
        k.append([a])
    ortga1=InlineKeyboardButton(text="Ortga",callback_data="shop")
    oldin=InlineKeyboardButton(text="⏪",callback_data=f"oldin,{b},{m},{date}")
    keyin=InlineKeyboardButton(text="⏩",callback_data=f"keyin,{b},{m},{date}")
    if b>0 and d<m:
        k.append([oldin,keyin])
    elif b>0 and d>=m:
        k.append([oldin])
    elif b<=0 and d<m:
        k.append([keyin])
    k.append([ortga1])
    text1="Siz "+callback_data+" telifonini tanladingiz. Biz sizga maslahat beradigan telifonlar quydagilardan ibora. Iltimos o'zindz istagan telifonni tanlang!"
    keyboard1=InlineKeyboardMarkup(k,resize_keyboard=True)
    query.edit_message_text(text=text1,reply_markup=keyboard1)

def keyin(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot 
    callback_data=query.data.split(',')[3]
    date=callback_data
    x=db.get_phone_list(callback_data)
    k=[]
    b=int(query.data.split(',')[1])
    b=b+10
    m=int(query.data.split(',')[2])
    if m-b-10>=0:
        d=b+10
    elif m-b-10<0:
        d=m
    for j in range(b,d):
        data=db.getPhone(date,j+1)
        a=InlineKeyboardButton(text=f"{x[j].split(',')[0]} {data['color']} {data['RAM']}/{data['memory']}",callback_data=f'tel {callback_data},'+x[j].split(',')[1])
        k.append([a])
    ortga1=InlineKeyboardButton(text="Ortga",callback_data="shop")
    oldin=InlineKeyboardButton(text="⏪",callback_data=f"oldin,{b},{m},{date}")
    keyin=InlineKeyboardButton(text="⏩",callback_data=f"keyin,{b},{m},{date}")
    if b>0 and d<m:
        k.append([oldin,keyin])
    elif b>0 and d>=m:
        k.append([oldin])
    elif b<=0 and d<m:
        k.append([keyin])
    k.append([ortga1])
    text1="Siz "+callback_data+" telifonini tanladingiz. Biz sizga maslahat beradigan telifonlar quydagilardan ibora. Iltimos o'zindz istagan telifonni tanlang!"
    keyboard1=InlineKeyboardMarkup(k,resize_keyboard=True)
    query.edit_message_text(text=text1,reply_markup=keyboard1)

def ortga2(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot = context.bot 
    chat_id=query.message.chat.id
    l=[]
    for i in db.get_tables():
        i=InlineKeyboardButton(text=i,callback_data="brand,"+i)
        l.append([i])
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga")
    l.append([ortga])
    keyboard=InlineKeyboardMarkup(l,resize_keyboard=True)
    text="Siz |🛍 Shop| bulimini tanladingiz.\nIltimos kerakli Smartphone ni tanlang!"
    query.delete_message()
    bot.sendMessage(chat_id=chat_id,text=text,reply_markup=keyboard)

def add_cart(update:Update,context:CallbackContext):
    query=update.callback_query
    bot = context.bot
    callback_data=query.data
    brand= callback_data.split(',')[1]
    chat_id=callback_data.split(',')[2]
    doc_id=callback_data.split(',')[3]
    bd.add(brand,chat_id,doc_id)
    query.answer("Savatga qo'shildi")

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
dp.add_handler(CallbackQueryHandler(menyu))


updater.start_polling()
updater.idle()