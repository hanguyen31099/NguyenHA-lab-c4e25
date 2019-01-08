from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
#1 connect to mlap sever
client = MongoClient(uri)
#2 get to database
db = client.get_database()
#3 get a collection
post_collection = db["posts"]
#4 create a document
import datetime
new_post = {
    "title" :"Hà Nguyễn",
    "author": "chuyện đêm",
    "text": "2h đêm rồi vẫn chưa xong bài tập :(((",
    }
#5 Insert Document
post_collection.insert_one(new_post)
#6. close connection
client.close()
# ObjectId('...')
# for post in post_collection.find():
#     print(post)
pos_list = post_collection.find()
frist_post=pos_list[0]
print(frist_post)