import sys
import tweepy
import json
import pymongo
import datetime
from pymongo import MongoClient

print "Start"

name_to_search = sys.argv[1]

#starts mongoDB
client = MongoClient()
db = client[name_to_search + 'tweepy_database']
collection = db[name_to_search + 'tweepy_collections']

#Classe do tweepy responsavel por armazenar os Twittes no mongoDB
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if (status.coordinates):
            what = collection.insert_one(status._json)
            print status.text
            print status.coordinates
            print status.created_at
            print "/***************************************************/"
            variable = 0
            for post in collection.find():
                print post
                print variable
                variable = variable+1


consumer_key = 'x0GzRIsgrn6PiuxmON0qEEVBU'
consumer_secret = 'GApQR5aIeVCXxdV3ZLTdeiA6OGG6UQleHZnD8E2LBCJcdRAKZh'
access_token = '144667001-t3zoMPJOg8d9m0E21ukGsdMSdFPkF04fhu1BaMKO'
access_secret = 'e7VfVWDx6cj9dmMgwzM8mGEyNPNTimvFlE0D22D3fLPoD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track=[name_to_search])
#myStream.filter(track=['python'], async=True)
