from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    Bot
    )
import logging
from telegram.ext import (
    CallbackContext
    )
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

def start(update: Update, context: CallbackContext):
    user_first_name = update.message.from_user.first_name
    user = update.message.from_user.username
    profile_url = f"https://t.me/{update.message.from_user.username}" 
    keyboard = [
        [KeyboardButton("✍️ Test yaratish", callback_data='test_yaratish'),
        KeyboardButton("✅ Javobni tekshirish", callback_data='javobni_tekshirish')],
        [KeyboardButton("🎉 Sertifikatlar", callback_data='sertifikatlar'),
        KeyboardButton("⚙️ Sozlamalar", callback_data='sozlamalar')],
        [KeyboardButton("📟 Pullik kanallar", callback_data='pullik_kanallar'),
        KeyboardButton("👨‍💻 Admin", callback_data='admin')],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text = f"Assalomu alaykum @{user}, botimizga xush kelibsiz."
    update.message.reply_text(text=text, reply_markup=reply_markup)

def test_yaratish(update:Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("✍️ Oddiy test"), KeyboardButton("📕 Fanli test")],
        [KeyboardButton("📅 Maxsus test"), KeyboardButton("📚 Blok test")],
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("❕ Kerakli bo'limni tanlang.", reply_markup=reply_markup)

def oddiy_test(update:Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Test javoblarini yuboring va javoblarning oxiriga + qo`yishni unutmang!!!\nM-n: abcd...+ yoki 1a2b3c4d...+\n\n❕ Javoblar faqat lotin alifbosida bo'lishi shart", reply_markup=reply_markup)

def fanli_test(update:Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Fan nomini yuboring va javoblarning oxiriga ! qo`yishni unutmang!!!.\nM-n: Matematika!", reply_markup=reply_markup)

def maxsus_test(update:Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Faylni yuboring.\n\n❗️ Rasm yoki fayl bo'lishi mumkun.", reply_markup=reply_markup)

def blok_test(update:Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Blok test ma'lumotlarini quyidagi ko'rinishda yuboring va javoblarning oxiriga : qo`yishni unutmang!!!.\n\nfan nomi 1/javoblar 1/ball 1\nfan nomi 2/javoblar 2/ball 2\n...\n\nM-n:\nMatematika/acbdabcdba/3.1\nFizika/bacdbcbcbcd/2.1\nOna tili/abcdbadbadbc/1.1:\n\n❗️ Fan nomi 20 ta belgidan oshmasligi shart, ball haqiqiy musbat son bo'lishi shart, javoblar soni 100 dan oshmasligi zarur. Fan va javoblar lotin alifbosida bo'lishi shart.", reply_markup=reply_markup)

def bosh_sahifa(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    keyboard = [
        [KeyboardButton("✍️ Test yaratish", callback_data='test_yaratish'),
        KeyboardButton("✅ Javobni tekshirish", callback_data='javobni_tekshirish')],
        [KeyboardButton("🎉 Sertifikatlar", callback_data='sertifikatlar'),
        KeyboardButton("⚙️ Sozlamalar", callback_data='sozlamalar')],
        [KeyboardButton("📟 Pullik kanallar", callback_data='pullik_kanallar'),
        KeyboardButton("👨‍💻 Admin", callback_data='admin')],
    ]
    db.remove(chat_id=chat_id)
    kode.remove(chat_id=chat_id)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text = f"Bosh sahifaga qaytdingiz!"
    update.message.reply_text(text=text, reply_markup=reply_markup)

def javoblar(update:Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Test kodini yuboring.", reply_markup=reply_markup)

def sozlanmalar(update:Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("🎉 Sertifikat tanlash"),
        KeyboardButton("✍️ Ism va familiya")],
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("🛠️ Kerakli bo'limni tanlang.", reply_markup=reply_markup)

def ismkiritish(update: Update,context:CallbackContext):
    keyboard = [
        [KeyboardButton("♻️ Orqaga")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("✍️ Ismingizni va Familyangizni yuboring va oxiriga _ qo`yishni unutmang!!!\nMasalan:\nMardon_  yoki Sultonov Mardon_", reply_markup=reply_markup)

def ismnibazaga(update: Update, context: CallbackContext):
    messege=update.message.text[0:-1]
    chat_id=update.message.chat_id
    ism.remove(chat_id=chat_id)
    ism.addism(chat_id=chat_id, ism=messege)
    keyboard = [
        [KeyboardButton("✍️ Test yaratish", callback_data='test_yaratish'),
        KeyboardButton("✅ Javobni tekshirish", callback_data='javobni_tekshirish')],
        [KeyboardButton("🎉 Sertifikatlar", callback_data='sertifikatlar'),
        KeyboardButton("⚙️ Sozlamalar", callback_data='sozlamalar')],
        [KeyboardButton("📟 Pullik kanallar", callback_data='pullik_kanallar'),
        KeyboardButton("👨‍💻 Admin", callback_data='admin')],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text=f"✅ {messege} muvaqiyatli bazaga qushildi!"
    update.message.reply_text(text, reply_markup=reply_markup)

def pullik(update: Update, context: CallbackContext) -> None:
    keyboard = [[
        InlineKeyboardButton("Kanalga qo`shilish", url='https://t.me/S_M_M_1207')
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Kanalimiz: @pullikkanaltavsifi", reply_markup=reply_markup)

def admin(update:Update,context:CallbackContext):
    update.message.reply_text(f"Admin: @S_M_M_1207")

def oddiy_test_tuzish(update: Update, context: CallbackContext):
    user_answer = update.message.text[0:-1]
    nomer=len(bd.get_cart().all())+1
    chat_id=update.message.chat_id
    user = update.message.from_user.username
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    kun,soat=current_time.split()
    bd.add(chat_id=chat_id,nomer=nomer,test=user_answer)
    text=f"✅ Test bazaga qo'shildi.\n👨‍🏫 Muallif: @{user}\n✍️ Test kodi: {nomer}\n🔹 Savollar: {len(user_answer)} ta\n📆 {kun} ⏰ {soat}"
    update.message.reply_text(text)

def fan(update: Update, context: CallbackContext):
    nomer=len(db.get_hammasi().all())+1
    chat_id=update.message.chat_id
    message = update.message.text[0:-1]
    db.addfan(chat_id=chat_id,nomer=nomer,fan=message)
    text=f"📕 Fan: {message}\n\n✍️ Test javoblarini yuboring va javoblarning oxiriga - qo`yishni unutmang!!!\nM-n: abcd...- yoki 1a2b3c4d...-\n\n❕ Javoblar faqat lotin alifbosida bo'lishi shart."
    update.message.reply_text(text)

def fanli_test_tuzish(update: Update, context: CallbackContext):
    user_answer = update.message.text[0:-1]
    chat_id=update.message.chat_id
    message = db.get_fan(chat_id=chat_id)[0]['fan']
    nomer=len(bd.get_cart().all())+1
    user = update.message.from_user.username
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    kun,soat=current_time.split()
    bd.addfan(chat_id=chat_id,nomer=nomer,test=user_answer,fan=message)
    text=f"✅ Test bazaga qo'shildi.\n👨‍🏫 Muallif: @{user}\n📕 Fan: {message}\n✍️ Test kodi: {nomer}\n🔹 Savollar: {len(user_answer)} ta\n📆 {kun} ⏰ {soat}"
    db.remove(chat_id=chat_id)
    update.message.reply_text(text)

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

def maxsus_baza(update: Update, context: CallbackContext):
    chat_id=update.message.chat_id
    photo = db.get_fan(chat_id=chat_id)
    print(photo)
    text=f"🗂 Fayllar: {len(photo)} ta\n\n✍️ Test javoblarini yuboring va javoblarning oxiriga * qo`yishni unutmang!!!:\nM-n: abcd...* yoki 1a2b3c4d...*\n❕ Javoblar faqat lotin alifbosida bo'lishi shart."
    update.message.reply_text(text)

def maxsus_baza_kiritish(update: Update, context: CallbackContext):
    chat_id=update.message.chat_id
    photo = db.get_fan(chat_id=chat_id)
    message = update.message.text[0:-1]
    nomer=len(bd.get_cart().all())+1
    user = update.message.from_user.username
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    kun,soat=current_time.split()
    bd.addmaxsus(chat_id=chat_id,nomer=nomer,photo=photo ,test=message)
    text=f"✅ Test bazaga qo'shildi.\n👨‍🏫 Muallif: @{user}\n📕 fayllar: {len(photo)}\n✍️ Test kodi: {nomer}\n📆 {kun} ⏰ {soat}"
    db.remove(chat_id=chat_id)
    update.message.reply_text(text)

def blok_test_tuzish(update: Update, context: CallbackContext):
    user_answer = update.message.text[0:-1]
    if user_answer.find("\n") > 0:
        l = user_answer.split("\n")  # Yangi qator bo'yicha ajratamiz
        print(l)
    elif user_answer.find(" ") >0:
        l = user_answer.split() 
        print(l)
    else:
        l=[user_answer]
    nomer = len(bd.get_cart().all()) + 1
    
    chat_id = update.message.chat_id
    
    try:
        bd.addblok(chat_id=chat_id, nomer=nomer, blok=user_answer)
        print(chat_id)
        # To'liq matnni tayyorlash
        text = ""
        for i in range(len(l)):
            item = l[i].split('/')
            text += f"❕ Blok {i+1}:\n📚 Fan: {item[0]}\n✅ Javob: {item[1]}\n📊 Ball: {item[2]}\n\n"
        text += "✅ Test bazaga qo'shildi."
        update.message.reply_text(text)
    except:
        text = f"❕ Xatolik:\n📚 Ma'lumot to`g`ri emas.\nBazaga qo`shilmadi!!!"
        update.message.reply_text(text)

def javoblarni_tekshir(update: Update, context: CallbackContext):
    kod = update.message.text[0:-1]
    chat_id = update.message.chat_id
    kode.addkod(kod=kod,chat_id=chat_id)
    test = bd.get_test(nomer=kod)[0]
    bot=Bot(TOKEN)
    if "blok" in test:
        
        natija = test["blok"]
        if natija.find("\n") > 0:
            l = natija.split("\n")  # Yangi qator bo'yicha ajratamiz
            print(l)
        elif natija.find(" ") >0:
            l = natija.split() 
            print(l)
        else:
            l=[natija]
        text ="Blok test ma'lumotlari:\n"
        for i in range(len(l)):
            item = l[i].split('/')
            print(item)
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
    

import logging
from datetime import datetime

def tekshirish(update: Update, context: CallbackContext):
    try:
        chat_id = update.message.chat_id
        ismi=ism.get_kod(chat_id=chat_id)
        user = update.message.from_user.username
        if len(ismi)==0:
            ismi=user
        else:
            ismi=ismi[0]["kod"]
        
        javoblar = update.message.text
        nomer = kode.get_kod(chat_id)[0]["kod"]
        
        fan = []
        ball = []
        l = []
        k = []
        m = []

        kode.remove(chat_id=chat_id)

        # Yangi qator bilan bo'sh joylarni almashtirish
        if "\n" in javoblar or " " in javoblar:
            if " " in javoblar:
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
                m.append(item[1])

            # Javoblar sonini tekshirish
            if len(l) != len(m):
                text = (f"❗️ Kechirasiz javob yuborishda xatolik, "
                        f"javobingiz to'liq emas, {nomer} kodli blok testda {len(m)} ta blok mavjud, "
                        f"sizning javoblaringiz soni {len(l)} ta, tekshirib qaytadan yuboring.\n"
                        f"M-n: \nabcdbdcbcbdbdbcb\nabcbdbdbbcbcbcbc\nadbabdbaadbcdabd")
                update.message.reply_text(text)
            else:
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
        else:
            test = bd.get_test(nomer=nomer)[0]["test"]
            if len(javoblar) == len(test):
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
                
                with open('certificate.jpg', 'rb') as photo:
                    context.bot.send_photo(chat_id=chat_id, photo=photo)
            else:
                text = (f"❗️ Kechirasiz {nomer} kodli testda {len(test)} ta kalit bor, "
                        f"sizning javoblaringiz soni esa {len(javoblar)} ta, "
                        f"tekshirib qaytadan yuboring.")
                
                update.message.reply_text(text)

    except Exception as e:
        logging.error(f"Xatolik yuz berdi: {e}")
        text = "❌ Avval test kodini kiriting...\n❗️ Test kodidan keyin . belgisini qo`shini unutmang!!!"
        update.message.reply_text(text)

    

    



# def sertifikat(update: Update, context: CallbackContext):
#     create_certificate("Ali", "Matematika", "95%")

#     # Chat ID olish
#     chat_id = update.message.chat_id
    
#     # Sertifikatni yuborish
#     with open('sertifikat_yangi.png', 'rb') as photo:
#         context.bot.send_photo(chat_id=chat_id, photo=photo)