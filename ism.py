from tinydb import TinyDB,Query
from tinydb.database import Document

class Ism:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        self.table = self.db.table('ismlar')

    def addism(self,chat_id,ism):
        data={
            "chat_id":chat_id,
            "ism":ism
        }
        self.table.insert(data)

    def adduser(self,chat_id,user):
        data={
            "chat_id":chat_id,
            "user":user
        }
        self.table.insert(data)

    def get_user(self,chat_id):
        user=Query()
        return self.table.search(user.chat_id==chat_id)

    def update_ism(self, chat_id, new_ism):
        User = Query()
        self.table.update({"ism": new_ism}, User.chat_id == chat_id)

    def update_fam(self, chat_id, new_fam):
        User = Query()
        self.table.update({"fam": new_fam}, User.chat_id == chat_id)
    
    def update_tel(self, chat_id, new_tel):
        User = Query()
        self.table.update({"tel": new_tel}, User.chat_id == chat_id)

    def update_manzil(self, chat_id, new_man):
        User = Query()
        self.table.update({"manzil": new_man}, User.chat_id == chat_id)


    def get_kod(self,chat_id):
        user=Query()
        return self.table.search(user.chat_id==chat_id)
    
    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==chat_id)
    def add_test_code(self,chat_id, test_code):
        user = Query()
        user_data = self.table.get(user.chat_id == chat_id)
        kodlar = user_data.get('kodlar', [])
        kodlar.append(test_code)
        self.table.update({'kodlar': kodlar}, user.chat_id == chat_id)