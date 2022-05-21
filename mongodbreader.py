import pymongo

def read_from_database(rule):
    if rule!="User has connected":
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["twitter_stream"]
        collection = db["tweets_"+rule]
        # TODO: change to pending
        data=collection.find_one({"status":"pending"})
        print("DATA:",rule,data)
        if data!=None:
            collection.update_one({"_id":data["_id"]},{"$set":{"status":"published"}})
        if data:
            print(data["tweet"])
            return data["tweet"]