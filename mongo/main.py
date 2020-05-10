
from pprint import pprint
from pymongo import MongoClient
import random


client = MongoClient("mongodb://admin:admin@localhost/admin")
db = client.admin

for i in range(100):
    db.users.insert_one(
        {"name": "fedor" + str(i), "age": random.randint(2, 88)})
