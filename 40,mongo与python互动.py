from pymongo import MongoClient
import time


class PymongoTest(object):
    def __init__(self):
        client = MongoClient()
        self.collection = client['t1']['t1']

    def insert_data(self):
        self.collection.insert_one({'_id': 9, 'name': '陈紫函', 'age': 29, 'gender': False})

    def insert_many(self):
        data = [{'_id': 10, 'name': '张钧甯', 'age': 28, 'gender': False},
                {'_id': 11, 'name': '朱茵', 'age': 37, 'gender': False}]
        self.collection.insert_many(data)

    def find_one(self):
        data = self.collection.find_one()
        print(data)
        print("-" * 50)

    def update_one(self):
        self.collection.update_one({'name': '刘亦菲'}, {'$set': {'age': 18}})

    def find_data(self):
        cursor = self.collection.find()
        for data in cursor:
            print(data)


if __name__ == '__main__':
    pt = PymongoTest()
    # pt.insert_data()
    pt.insert_many()
    pt.find_one()
    print('&'*30)
    pt.find_data()
    pt.update_one()
    print('$'*50)
    pt.find_data()