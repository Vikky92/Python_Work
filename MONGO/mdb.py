from pymongo import MongoClient
from datetime import  datetime

client = MongoClient()
db = client.test
    #Tutorial to make a document in MongoDb
    # Data in MongoDB is represented (and stored)
    # using JSON-style documents.
    # In PyMongo we use dictionaries to represent documents.
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

cursor = db.restaurants.find()

for document in cursor:
    print document