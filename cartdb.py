from tinydb import TinyDB, Query
from tinydb.database import Document
from tinydb.operations import delete
class Cart:
    def __init__(self,cart_path:str):
        self.db = TinyDB(cart_path, indent=4)
        self.table = self.db.table('cart')

    def add(self,nomer,chat_id,test):
        date={"chat_id":chat_id,
              "nomer":nomer,
              "test":test}
        self.table.insert(date)

    def addblok(self,nomer,chat_id,blok):
        date={"chat_id":chat_id,
              "nomer":nomer,
              "blok":blok}
        self.table.insert(date)

    def addfan(self,fan,chat_id,nomer,test):
        date={"chat_id":chat_id,
              "fan":fan,
              "nomer":nomer,
              "test":test
              }
              
        self.table.insert(date)

    def addmaxsus(self,chat_id,nomer,photo,test):
        date={"chat_id":chat_id,
              "photo":photo,
              "nomer":nomer,
              "test":test
              }
              
        self.table.insert(date)

    def get_cart(self):
        return self.table

    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==str(chat_id))

    def get_test(self,nomer):
        user=Query()
        return self.table.search(user.nomer==int(nomer))