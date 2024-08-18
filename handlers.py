from telegram import Update, KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,Bot
from telegram.ext import  ConversationHandler, CallbackContext
import logging
from cartdb import Cart
from datetime import datetime
import os
from kode import Data
from db import DB
from ism import Ism
ism=Ism("ism.json")
kode=Data("kode.json")
db = DB("data.json")
bd =Cart("db.json")
from settings import TOKEN
from datetime import datetime
import sertifikat
import re
FAN, ISMNI_BAZAGA, ISMNI_BAZAGA_QUSH, FAMNI_BAZAGA_QUSH, MANNI_BAZAGA_QUSH, TELNI_BAZAGA_QUSH, FAMNI_BAZAGA, ODDIY_TEST_TUZISH, FANLI_TEST_TUZISH, MAXSUS_BAZA_KIRITISH, BLOK_TEST_TUZISH, MAXSUS_TEST_TUZISH, JAVOBLARNI_TEKSHIRISH, TEKSHIRISH, MAXSUS_BAZA,JAVOBLAR_KODI = range(16)

def start(update: Update, context: CallbackContext):
    user = update.message.from_user.username
    chat_id=update.message.chat_id
    l=ism.get_kod(chat_id=chat_id)
    if len(l)==0:
        ism.adduser(chat_id=chat_id, user=user)
        update.message.reply_text("✍️ Ismingizni kiriting.\n\n❗️ Ism faqat lotin alifbosida bo'lishi shart")
        return ISMNI_BAZAGA_QUSH
    else:
        context.user_data['started'] = True
        keyboard = [
            [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
            [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
            [KeyboardButton("📟 Pullik kanallar")],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        text = f"Assalomu alaykum @{user}, botimizga xush kelibsiz."
        update.message.reply_text(text=text, reply_markup=reply_markup)

def famqushish(update: Update, context: CallbackContext):
    messege=update.message.text
    chat_id=update.message.chat_id
    ism.update_ism(chat_id=chat_id, new_ism=messege)
    update.message.reply_text("✍️ Familiyangizni kiriting.\n\n❗️ Familiya faqat lotin alifbosida bo'lishi shart")
    return FAMNI_BAZAGA_QUSH

def raqamqushish(update: Update, context: CallbackContext):
    messege = update.message.text
    chat_id = update.message.chat_id
    ism.update_fam(chat_id=chat_id, new_fam=messege)
    
    keyboard = [[KeyboardButton("📱 Telefon raqamni yuborish", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    update.message.reply_text("📱 Telefon raqamingizni yuboring.", reply_markup=reply_markup)
    return TELNI_BAZAGA_QUSH

def manzilqushish(update: Update, context: CallbackContext):
    messege=update.message.contact.phone_number
    chat_id=update.message.chat_id
    ism.update_tel(chat_id=chat_id, new_tel=messege)
    keyboard = [
        [InlineKeyboardButton("Qoraqalpog‘iston Respublikasi", callback_data='Qoraqalpog`iston')],
        [InlineKeyboardButton("Andijon", callback_data='Andijon'),
         InlineKeyboardButton("Buxoro", callback_data='Buxoro')],
        [InlineKeyboardButton("Farg‘ona", callback_data='Fargona'),
         InlineKeyboardButton("Jizzax", callback_data='Jizzax')],
        [InlineKeyboardButton("Xorazm", callback_data='Xorazm'),
         InlineKeyboardButton("Namangan", callback_data='Namangan')],
        [InlineKeyboardButton("Navoiy", callback_data='Navoiy'),
         InlineKeyboardButton("Qashqadaryo", callback_data='Qashqadaryo')],
        [InlineKeyboardButton("Samarqand", callback_data='Samarqand'),
         InlineKeyboardButton("Sirdaryo", callback_data='Sirdaryo')],
        [InlineKeyboardButton("Surxondaryo", callback_data='Surxondaryo'),
         InlineKeyboardButton("Toshkent", callback_data='Toshkent')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Viloyatni tanlang!!!",reply_markup=reply_markup)
    return MANNI_BAZAGA_QUSH

def manzilniqushish(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id=query.message.chat_id
    bot=Bot(TOKEN)
    user = ism.get_kod(chat_id=chat_id)[0]['user']
    query.answer()
    ism.update_manzil(chat_id=chat_id, new_man=query.data)
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text = f"Assalomu alaykum @{user}, botimizga xush kelibsiz."
    query.delete_message()
    bot.send_message(chat_id=chat_id,text=text, reply_markup=reply_markup)
    return ConversationHandler.END

def test_yaratish(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("✍️ Oddiy test"), KeyboardButton("📕 Fanli test")],
        [KeyboardButton("📅 Maxsus test"), KeyboardButton("📚 Blok test")],
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("❕ Kerakli bo'limni tanlang.", reply_markup=reply_markup)
    return ConversationHandler.END

def oddiy_test(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("♻️ Orqaga")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Test javoblarini yuboring\nM-n: abcd... yoki 1a2b3c4d...\n\n❕ Javoblar faqat lotin alifbosida bo'lishi shart", reply_markup=reply_markup)
    return ODDIY_TEST_TUZISH

def fanli_test(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("♻️ Orqaga")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Fan nomini yuboring.\nM-n: Matematika", reply_markup=reply_markup)
    return FAN

def maxsus_test(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("♻️ Orqaga")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Faylni yuboring.\n\n❗️ Rasm yoki fayl bo'lishi mumkun.", reply_markup=reply_markup)
    return MAXSUS_TEST_TUZISH

def blok_test(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("♻️ Orqaga")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Blok test ma'lumotlarini quyidagi ko'rinishda yuboring.\n\nfan nomi 1/javoblar 1/ball 1\nfan nomi 2/javoblar 2/ball 2\n...\n\nM-n:\nMatematika/acbdabcdba/3.1\nFizika/bacdbcbcbcd/2.1\nOna tili/abcdbadbadbc/1.1\n\n❗️ Fan nomi 20 ta belgidan oshmasligi shart, ball haqiqiy musbat son bo'lishi shart, javoblar soni 100 dan oshmasligi zarur. Fan va javoblar lotin alifbosida bo'lishi shart.", reply_markup=reply_markup)
    return BLOK_TEST_TUZISH

def bosh_sahifa(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    for handler in context.dispatcher.handlers.get(0, []):
        if isinstance(handler, ConversationHandler):
            handler.conversations.clear()
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    db.remove(chat_id=chat_id)
    kode.remove(chat_id=chat_id)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text = f"Bosh sahifaga qaytdingiz!"
    update.message.reply_text(text=text, reply_markup=reply_markup)
    return ConversationHandler.END

def javoblar(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("♻️ Orqaga")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Test kodini yuboring.", reply_markup=reply_markup)
    return JAVOBLAR_KODI

def sozlanmalar(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("✍️ Ism"), KeyboardButton("✍️ Familiya")],
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("🛠️ Kerakli bo'limni tanlang.", reply_markup=reply_markup)

def ismkiritish(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("♻️ Orqaga")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Ismingizni kiriting.\n\n❗️ Ism faqat lotin alifbosida bo'lishi shart", reply_markup=reply_markup)
    return ISMNI_BAZAGA

def famkiritish(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("♻️ Orqaga")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Familiyangizni kiriting.\n\n❗️ Familiya faqat lotin alifbosida bo'lishi shart", reply_markup=reply_markup)
    return FAMNI_BAZAGA

def ismnibazaga(update: Update, context: CallbackContext):
    messege=update.message.text
    chat_id=update.message.chat_id
    ism.update_ism(chat_id=chat_id, new_ism=messege)
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text=f"✅ {messege} muvaqiyatli bazaga qushildi!"
    update.message.reply_text(text, reply_markup=reply_markup)
    return ConversationHandler.END

def famnibazaga(update: Update, context: CallbackContext):
    messege=update.message.text
    chat_id=update.message.chat_id
    ism.update_fam(chat_id=chat_id, new_fam=messege)
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text=f"✅ {messege} muvaqiyatli bazaga qushildi!"
    update.message.reply_text(text, reply_markup=reply_markup)
    return ConversationHandler.END

def pullik(update: Update, context: CallbackContext) -> None:
    keyboard = [[
        InlineKeyboardButton("Kanalga qo`shilish", url='https://t.me/S_M_M_1207')
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Kanalimiz: @pullikkanaltavsifi", reply_markup=reply_markup)
    return ConversationHandler.END

def admin(update:Update,context:CallbackContext):
    update.message.reply_text(f"Admin: @S_M_M_1207")
    return ConversationHandler.END

def oddiy_test_tuzish(update: Update, context: CallbackContext):
    user_answer = update.message.text
    user_answer = re.sub(r'\d+', '', user_answer)
    nomer=len(bd.get_cart().all())+1
    chat_id=update.message.chat_id
    user = update.message.from_user.username
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    kun,soat=current_time.split()
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    bd.add(chat_id=chat_id,nomer=nomer,test=user_answer)
    text=f"✅ Test bazaga qo'shildi.\n👨‍🏫 Muallif: @{user}\n✍️ Test kodi: {nomer}\n🔹 Savollar: {len(user_answer)} ta\n📆 {kun} ⏰ {soat}"
    update.message.reply_text(text,reply_markup=reply_markup)
    return ConversationHandler.END


def fan(update: Update, context: CallbackContext):
    nomer=len(db.get_hammasi().all())+1
    chat_id=update.message.chat_id
    message = update.message.text
    db.addfan(chat_id=chat_id,nomer=nomer,fan=message)
    text=f"📕 Fan: {message}\n\n✍️ Test javoblarini yuboring\nM-n: abcd... yoki 1a2b3c4d...\n\n❕ Javoblar faqat lotin alifbosida bo'lishi shart."
    update.message.reply_text(text)
    return FANLI_TEST_TUZISH

def fanli_test_tuzish(update: Update, context: CallbackContext):
    user_answer = update.message.text
    user_answer = re.sub(r'\d+', '', user_answer)
    chat_id=update.message.chat_id
    message = db.get_fan(chat_id=chat_id)[0]['fan']
    nomer=len(bd.get_cart().all())+1
    user = update.message.from_user.username
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    kun,soat=current_time.split()
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    bd.addfan(chat_id=chat_id,nomer=nomer,test=user_answer,fan=message)
    text=f"✅ Test bazaga qo'shildi.\n👨‍🏫 Muallif: @{user}\n📕 Fan: {message}\n✍️ Test kodi: {nomer}\n🔹 Savollar: {len(user_answer)} ta\n📆 {kun} ⏰ {soat}"
    db.remove(chat_id=chat_id)
    update.message.reply_text(text,reply_markup=reply_markup)
    return ConversationHandler.END

def maxsus_test_tuzish(update: Update, context: CallbackContext):
    if update.message.document is not None:
        photo = update.message.document
    else:
        
        photo = update.message.photo[-1]
    l=[]
    l.append(photo["file_id"])
    nomer=len(bd.get_cart().all())+1
    chat_id=update.message.chat_id
    bot=Bot(TOKEN)
    db.addrasm(chat_id=chat_id,photo=photo["file_id"])
    keyboard = [
        [KeyboardButton("✅ Davom etish"),
        KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    photo = db.get_fan(chat_id=chat_id)
    text=f"✍️ Fayl yuborishda davom etishingiz mumkin yoki keyingi bosqichga o'tish uchun ✅ Davom etish tugmasini bosing.\n\n🗂 Fayllar soni: {len(photo)}  ta"
    update.message.reply_text(text,reply_markup=reply_markup)
    return MAXSUS_BAZA

def maxsus_baza(update: Update, context: CallbackContext):
    chat_id=update.message.chat_id
    photo = db.get_fan(chat_id=chat_id)
    text=f"🗂 Fayllar: {len(photo)} ta\n\n✍️ Test javoblarini yuboring:\nM-n: abcd... yoki 1a2b3c4d...\n❕ Javoblar faqat lotin alifbosida bo'lishi shart."
    update.message.reply_text(text)
    return MAXSUS_BAZA_KIRITISH

def maxsus_baza_kiritish(update: Update, context: CallbackContext):
    chat_id=update.message.chat_id
    photo = db.get_fan(chat_id=chat_id)
    message = update.message.text
    message = re.sub(r'\d+', '', message)
    nomer=len(bd.get_cart().all())+1
    user = update.message.from_user.username
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    kun,soat=current_time.split()
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    bd.addmaxsus(chat_id=chat_id,nomer=nomer,photo=photo ,test=message)
    text=f"✅ Test bazaga qo'shildi.\n👨‍🏫 Muallif: @{user}\n📕 fayllar: {len(photo)}\n✍️ Test kodi: {nomer}\n📆 {kun} ⏰ {soat}"
    db.remove(chat_id=chat_id)
    update.message.reply_text(text,reply_markup=reply_markup)
    return ConversationHandler.END

def blok_test_tuzish(update: Update, context: CallbackContext):
    user_answer = update.message.text
    if user_answer.find("\n") > 0:
        l = user_answer.split("\n")  # Yangi qator bo'yicha ajratamiz
    elif user_answer.find(" ") >0:
        l = user_answer.split() 
    else:
        l=[user_answer]
    nomer = len(bd.get_cart().all()) + 1
    chat_id = update.message.chat_id
    
    try:
        bd.addblok(chat_id=chat_id, nomer=nomer, blok=user_answer)
        # To'liq matnni tayyorlash
        text = ""
        keyboard = [
            [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
            [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
            [KeyboardButton("📟 Pullik kanallar")],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        for i in range(len(l)):
            item = l[i].split('/')
            text += f"❕ Blok {i+1}:\n📚 Fan: {item[0]}\n✅ Javob: {item[1]}\n📊 Ball: {item[2]}\n\n"
        text += "✅ Test bazaga qo'shildi."
        update.message.reply_text(text,reply_markup=reply_markup)
        return ConversationHandler.END
    except:
        text = f"❕ Xatolik:\n📚 Ma'lumot to`g`ri emas.\nBazaga qo`shilmadi!!!"
        keyboard = [
            [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
            [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
            [KeyboardButton("📟 Pullik kanallar")],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text(text,reply_markup=reply_markup)
        return ConversationHandler.END

def javoblarni_tekshir(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    kod = str(update.message.text)
    print(kod)
    kodlar = ism.get_kod(chat_id)
    if kodlar and "kodlar" in kodlar[0]:
        kodlar = kodlar[0]["kodlar"]
    else:
        kodlar = []

    print(kodlar)
    ism.add_test_code(chat_id=chat_id, test_code=kod)

    if kod not in kodlar:
        kode.addkod(kod=kod, chat_id=chat_id)
        test = bd.get_test(nomer=kod)[0]
        bot=Bot(TOKEN)
        if "blok" in test:

            natija = test["blok"]
            if natija.find("\n") > 0:
                l = natija.split("\n")  # Yangi qator bo'yicha ajratamiz
            elif natija.find(" ") >0:
                l = natija.split() 

            else:
                l=[natija]
            text ="Blok test ma'lumotlari:\n"
            for i in range(len(l)):
                item = l[i].split('/')
                s=0
                s+=len(item[1])
                text += f"❕ Blok {i+1}:\n📚 Fan: {item[0]}\n❔  Savollar: {len(item[1])} ta\n📊 Ball: {item[2]}\n\n"
            text +="\n✍️ Yuqorida blok test ma'lumotlari bilan tanishishingiz mumkin va o'z javoblaringizni quyidagicha yuborishingiz zarur.\n1-fan javoblari\n2-fan javoblari\n3-fan javoblari \n...\nM-n: \nabcdbdcbcbdbdbcb\nabcbdbdbbcbcbcbc\nadbabdbaadbcdabd"
            update.message.reply_text(text=text)
        elif "photo" in test:
            natija=test["test"]
            for i in range(len(test["photo"])):
                try:
                    bot.send_document(chat_id=chat_id,document=test["photo"][i]["photo"])
                except:
                    bot.send_photo(chat_id=chat_id,photo=test["photo"][i]["photo"])
            text=f"✍️ {test['nomer']} kodli testda {len(natija)} ta kalit mavjud. Marhamat o'z javoblaringizni yuboring.\n\nM-n: abcd... yoki 1a2b3c4d..."    
            update.message.reply_text(text=text)
        elif "fan" in test:
            natija = test["test"]
            text = f"✍️ {test['nomer']} kodli test, Fan {test['fan']}da {len(natija)} ta kalit mavjud. Marhamat o'z javoblaringizni yuboring.\n\nM-n: abcd.. yoki 1a2b3c4d..."
            update.message.reply_text(text=text)
        else:
            natija=test["test"]
            text=f"✍️ {test['nomer']} kodli testda {len(natija)} ta kalit mavjud. Marhamat o'z javoblaringizni yuboring.\n\nM-n: abcd... yoki 1a2b3c4d..."
            update.message.reply_text(text=text)
        return JAVOBLARNI_TEKSHIRISH
    else:
        text=f"❗️ Kechirasiz siz avval {kod} sonli testga ishtirok etgansiz!\nIltimos boshqa kod yuboring."
        update.message.reply_text(text=text)
    

def tekshirish(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    nomer = kode.get_kod(chat_id)[0]["kod"]
    
    keyboard = [
        [KeyboardButton("✍️ Test yaratish"), KeyboardButton("✅ Javobni tekshirish")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("👨‍💻 Admin")],
        [KeyboardButton("📟 Pullik kanallar")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    
    ismi=ism.get_kod(chat_id=chat_id)[0]['ism']+' '+ism.get_kod(chat_id=chat_id)[0]['fam']
    user = update.message.from_user.username
    
    javoblar = update.message.text
    javoblar = re.sub(r'\d+', '', javoblar)
    
    
    
    fan = []
    ball = []
    l = []
    k = []
    m = []
    
    # Yangi qator bilan bo'sh joylarni almashtirish
    if "\n" in javoblar or " " in javoblar:
        
        javoblar = javoblar.replace(" ", "\n")
        l = javoblar.split("\n")
        # Test bloklarini olish
        test = bd.get_test(nomer=nomer)[0]["blok"]
        k = test.split("\n")
        # Fan va ball ro'yxatlarini yaratish
        for i in range(len(k)):
            item = k[i].split('/')
            fan.append(item[0])
            ball.append(item[2])
            raqamsiz = re.sub(r'\d+', '', item[1])
            m.append(raqamsiz)
        # Javoblar sonini tekshirish
        if len(l) != len(m):
            text = (f"❗️ Kechirasiz javob yuborishda xatolik, "
                    f"javobingiz to'liq emas, {nomer} kodli blok testda {len(m)} ta blok mavjud, "
                    f"sizning javoblaringiz soni {len(l)} ta, tekshirib qaytadan yuboring.\n"
                    f"M-n: \nabcdbdcbcbdbdbcb\nabcbdbdbbcbcbcbc\nadbabdbaadbcdabd")
            update.message.reply_text(text)
            return JAVOBLARNI_TEKSHIRISH
        else:
            kode.remove(chat_id=chat_id)
            z = []
            for i in range(len(l)):
                mismatches = 0
                for char1, char2 in zip(l[i], m[i]):
                    if char1 != char2:
                        mismatches += 1
                correct_answers = len(l[i]) - mismatches
                total_questions = len(l[i])
                quality_percentage = (correct_answers * 100) / total_questions
                text = (f"💡 Blok: {i+1}\n"
                        f"📚 Fan: {fan[i]}\n"
                        f"✅ To'gri javoblar: {correct_answers} ta\n"
                        f"❌ Noto'g'ri javoblar: {mismatches} ta\n"
                        f"📊 Sifat: {quality_percentage:.2f}%")
                update.message.reply_text(text)
                z.append(correct_answers)  # to'g'ri javoblar sonini qo'shish
            current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
            kun, soat = current_time.split()
            text = (f"💡 Umumiy natija:\n💻 Test kodi: {nomer}\n\n")
            jami = 0
            tupladi = 0
            for i in range(len(l)):
                text += f"Blok {i+1}: {z[i] * float(ball[i]):.2f}\n"
                tupladi += z[i] * float(ball[i])
                jami += len(l[i]) * float(ball[i])
            text += (f"\n\nJami ball: {jami}\nTo'plangan ball: {tupladi}\n\n"
                     f"📆 {kun} ⏰ {soat}\n\n"
                     f"--------------------------\n"
                     f"☝️ Natijangizni yaxshilash uchun REPETITSION TESTLAR va "
                     f"Prezident maktabiga tayyorlash kanallariga a'zo bo'ling!!\n"
                     f"Ma'lumot uchun: @pullikkanaltavsifi")
            update.message.reply_text(text)
            if (len(javoblar) - mismatches) * 100 / len(javoblar)>=80:
                with open('certificate.jpg', 'rb') as photo:
                    context.bot.send_photo(chat_id=chat_id, photo=photo,caption=text,reply_markup=reply_markup)
    else:
        try:
            test = bd.get_test(nomer=nomer)[0]["test"]
        except:
            try:
                test =bd.get_test(nomer=nomer)[0]["blok"]
            except:
                text = "❌ Noto'g'ri Talablar bajarilmagan!!!"
                update.message.reply_text(text)
                return
        if len(javoblar) == len(test):
            kode.remove(chat_id=chat_id)
            mismatches = 0
            z = []
            current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
            kun, soat = current_time.split()
            for char1, char2 in zip(javoblar, test):
                if char1 != char2:
                    mismatches += 1
                    z.append(len(javoblar) - mismatches)
            text = (f"💡 Natijangiz:\n🙎🏻‍♂️ Foydalanuvchi: @{user}\n"
                    f"💻 Test kodi: {nomer}\n"
                    f"✅ To'gri javoblar: {len(javoblar) - mismatches} ta\n"
                    f"❌ Noto'g'ri javoblar: {mismatches} ta\n"
                    f"📊 Sifat: {(len(javoblar) - mismatches) * 100 / len(javoblar):.2f}%\n"
                    f"📆 {kun} ⏰ {soat}\n"
                    f"--------------------------\n"
                    f"☝️ Natijangizni yaxshilash uchun REPETITSION TESTLAR va "
                    f"Prezident maktabiga tayyorlash kanallariga a'zo bo'ling!!\n"
                    f"Ma'lumot uchun: @pullikkanaltavsifi")
            foiz=str(int((len(javoblar) - mismatches) * 100 / len(javoblar)))+' %'
            
            update.message.reply_text(text)
            sertifikat.create_certificate(user_name=ismi,result=foiz,vaqt=kun,ismi="Mardon")
            text =(f"💡 Natijangiz:\n🙎🏻‍♂️ Foydalanuvchi: @{user}\n"
                    f"💻 Test kodi: {nomer}\n"
                    f"✅ To'gri javoblar: {len(javoblar) - mismatches} ta\n"
                    f"❌ Noto'g'ri javoblar: {mismatches} ta\n"
                    f"📊 Sifat: {(len(javoblar) - mismatches) * 100 / len(javoblar):.2f}%\n"
                    f"📆 {kun} ⏰ {soat}\n"
                    )
            if (len(javoblar) - mismatches) * 100 / len(javoblar)>=80:
                with open('certificate.jpg', 'rb') as photo:
                    context.bot.send_photo(chat_id=chat_id, photo=photo,caption=text,reply_markup=reply_markup)
            return ConversationHandler.END
        else:
            text = (f"❗️ Kechirasiz {nomer} kodli testda {len(test)} ta kalit bor, "
                    f"sizning javoblaringiz soni esa {len(javoblar)} ta, "
                    f"tekshirib qaytadan yuboring.")
            
            update.message.reply_text(text)
            return JAVOBLARNI_TEKSHIRISH
                
    
def cancel(update:Update, context:CallbackContext):
    update.message.reply_text("Suhbat bekor qilindi.")
    return ConversationHandler.END


    

    



# def sertifikat(update: Update, context: CallbackContext):
#     create_certificate("Ali", "Matematika", "95%")

#     # Chat ID olish
#     chat_id = update.message.chat_id
    
#     # Sertifikatni yuborish
#     with open('sertifikat_yangi.png', 'rb') as photo:
#         context.bot.send_photo(chat_id=chat_id, photo=photo)