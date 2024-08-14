from tinydb import TinyDB,Query
from tinydb.database import Document

class Ism:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        self.table = self.db.table('ismlar')

    def addism(self,chat_id,ism):
        data={
            "chat_id":chat_id,
            "kod":ism
        }
        self.table.insert(data)

    def get_kod(self,chat_id):
        user=Query()
        return self.table.search(user.chat_id==chat_id)
    
    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==chat_id)