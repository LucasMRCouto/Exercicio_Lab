from typing import Collection
import pymongo
import json


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://lucas:012204lmrc@cluster0.u4vucat.mongodb.net/test"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print("Database reseted successfully!")
        except Exception as e:
            print(e)
