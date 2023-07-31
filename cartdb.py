from tinydb import TinyDB, Query
from tinydb.database import Document
from tinydb.operations import delete
class Cart:
    def __init__(self,cart_path:str):
        self.db = TinyDB(cart_path, indent=4)
        self.table = self.db.table('cart')

    def add(self,brand,chat_id,doc_id):
        """
        add card

        data = {
            'brand':brand,
            'doc_id': doc_id,
            chat_id: chat_id
            }
        """
        date={"chat_id":chat_id,
              "brand":brand,
              "doc_id":doc_id}
        self.table.insert(date)

    def get_cart(self, chat_id):
        user=Query()
        dic=self.table
        return dic.search(user.chat_id==chat_id)

    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==str(chat_id))