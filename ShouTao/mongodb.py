import pymongo
from utils.config import *

class MongoDB():

    def __init__(self):
        self.client = pymongo.MongoClient(host=MONGO_URI, port=MONGO_PORT)
        self.db = self.client.taobao

    def save(self, item):
        try:
            if self.db.goods.insert(dict(item)):
                print('成功插入数据库')
        except Exception as e:
            print('插入数据库失败：', e.args)

if __name__ == '__main__':
    pass