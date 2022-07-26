import pymongo
from pymongo import MongoClient

cluster = pymongo.MongoClient("mongodb://localhost/ProjectDB", connect=False)
db = cluster["ProjectDB"]
collection = db["events"]
post = {
        "topic": "دورة الفضاء",
        "instructor": "مهنا الفنان",
        "day": "الثلاثاء",
        "date": "12/11/2020",
        "starting": "15:00",
        "ending": "16:00",
        "link": "https://translate.google.com/",
        "category":"computer"
    }
collection.insert_one(post)
print('======================')
print('record has been added!')
print('======================')