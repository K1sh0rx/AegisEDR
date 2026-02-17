from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["aegis_edr"]

def store_event(event):
    db.events.insert_one({"event":event})
