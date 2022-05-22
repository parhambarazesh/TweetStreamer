import pymongo
def write_to_database(data,rule):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["twitter_stream"]
    collection=db["tweets"]
    collection.insert_one(data)