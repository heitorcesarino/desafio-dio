from pymongo import MongoClient
from fastapi import FastAPI
import uvicorn

# client = MongoClient('mongodb://dio:dio@localhost:27017/')

# db = client.my_test

# tweets_collection = db.tweets

# tweets_collection.insert_one({'author':'teste', 'text':'texto qualquer'})

# tweets = tweets_collection.find({})

# print(list(tweets))

BRAZIL_WOE_ID = 23424768

app = FastAPI()

@app.get('/trends')
def  get_trends():
    return {'message': 'Hello World'}

