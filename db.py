from pymongo import MongoClient

class db:
    
    #self.status = ""

    @staticmethod
    def start(self):
        client = MongoClient('localhost', 27017)
        db = client.clinic
        self.status = db.command("serverStatus")
        print(self.status)

    @staticmethod
    def hello(self):
        print(self.status)