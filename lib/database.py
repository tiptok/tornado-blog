import peewee

class Database(object):

    def __init__(self, kw):
        self.config = kw
        self.load_database()
        self.Model = self.get_model_class()

    def load_database(self):
        # try:
        #     self.db = self.config.pop('db')
        #     self.engine = self.config.pop('engine')
        # except KeyError:
        #     raise Exception(
        #         'Please specify a "db" and "engine" for your database')
        try:
            self.database = peewee.MySQLDatabase('blog',user='root',password='123456',host='127.0.0.1',port=3306) 
        except ImportError:
            raise Exception('Unable to import: "%s"' % self.engine)
        
    def get_model_class(self):
        class BaseModel(peewee.Model):
            class Meta:
                database = self.database
        return BaseModel

    def connect(self):
        self.database.connect()

    def close(self):
        try:
            self.database.close()
        except:
            pass

db = Database({'db':"MYSQL"})