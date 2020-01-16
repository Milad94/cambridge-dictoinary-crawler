from pymongo import MongoClient

client = MongoClient()
db = client.cambirige_crawler
words_collection = db.words_collection
