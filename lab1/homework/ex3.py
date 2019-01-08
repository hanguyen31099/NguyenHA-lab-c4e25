from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
post_collection = db["posts"]
import datetime
new_post = {
    "title" :"Hà Nguyễn",
    "author": "chuyện đêm",
    "text": "2h đêm rồi vẫn chưa xong bài tập :(((",
    }
post_collection.insert_one(new_post)
client.close()
