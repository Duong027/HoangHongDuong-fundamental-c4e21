# 1. Connect to database
from pymongo import MongoClient
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e' # DÙng uri để connect
client = MongoClient(uri)
db = client.get_default_database()

#2. Select collection
tests = db["posts"]            

#3. Create document

post = {
    "title": "C4e21 ",
    "content": "Anh nhớ sẽ đưa em đi hết cuộc đời. Mà sao không đưa được đoạn đường em đi...",
    "author" : "Hoàng Dương"
    }

#4. Insert document

tests.insert_one(post)

print("Done")

test_list = tests.find()

for post in test_list:
    print(post)


