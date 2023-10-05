from tinydb import TinyDB
from tinydb.database import Document

class DB:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        

    def get_tables(self):
        """
        To get the list of all the tables in the database
        """
        tables = self.db.tables()
        t=list(tables)
        return t
        
        
    def getPhone(self,brand,idx):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """
        d=self.db.table(brand).get(doc_id=idx)
        return d

    def get_phone_list(self,brand):
        """
        Return phone list
        """
        l=[]
        s=1
        for i in self.db.table(str(brand)):
            m=self.db.table(str(brand)).get(doc_id=s)["name"]+f',{s}'
            s+=1
            l.append(m)
        return l