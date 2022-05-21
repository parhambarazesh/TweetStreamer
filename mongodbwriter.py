import pymongo
# connect to mongodb with username and password
# client = pymongo.MongoClient("mongodb://<username>:<password>@localhost:27017/")
def write_to_database(data,rule):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["twitter_stream"]
    collection = db["tweets_"+rule]
    collection.insert_one(data)