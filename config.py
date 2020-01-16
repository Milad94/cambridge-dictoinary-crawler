from pymongo import MongoClient

from meta import Singleton


class MongoConfig(metaclass=Singleton):
    client = MongoClient()
    db = client.cambirige_crawler
    words_collection = db.words_collection
