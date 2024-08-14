from tinydb import TinyDB,Query
from tinydb.database import Document

class DB:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        self.table = self.db.table('fanlar')
        

    def addfan(self,fan,chat_id,nomer):
        date={"chat_id":chat_id,
              "fan":fan,
              "nomer":nomer
              }
        self.table.insert(date)
    
    def get_fan(self,chat_id):
        user=Query()
        return self.table.search(user.chat_id==chat_id)

    def get_hammasi(self):
        return self.table
    
    def add(self,brand,chat_id,doc_id):
        date={"chat_id":chat_id,
              "brand":brand,
              "doc_id":doc_id}
        self.table.insert(date)

    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==chat_id)

    def addrasm(self, chat_id,photo):
        date={"chat_id":chat_id,
              "photo":photo}
        self.table.insert(date)
    
    def addphoto(self, chat_id,test):
        date={"chat_id":chat_id,
              "test":test}
        self.table.insert(date)