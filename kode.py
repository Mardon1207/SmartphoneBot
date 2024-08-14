from tinydb import TinyDB,Query
from tinydb.database import Document

class Data:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        self.table = self.db.table('kodlar')

    def addkod(self,chat_id,kod):
        data={
            "chat_id":chat_id,
            "kod":kod
        }
        self.table.insert(data)

    def get_kod(self,chat_id):
        user=Query()
        return self.table.search(user.chat_id==chat_id)
    
    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==chat_id)