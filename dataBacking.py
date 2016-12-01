import sys
import tweepy
import json
import pymongo
import datetime
from pymongo import MongoClient

"""/***********************************************************************/"""

#inicia MongoDB e cria-se os bancos necessarios
client = MongoClient()
db = client['tweepy_database']

"""/***********************************************************************/"""

consumer_key = 'x0GzRIsgrn6PiuxmON0qEEVBU'
consumer_secret = 'GApQR5aIeVCXxdV3ZLTdeiA6OGG6UQleHZnD8E2LBCJcdRAKZh'
access_token = '144667001-t3zoMPJOg8d9m0E21ukGsdMSdFPkF04fhu1BaMKO'
access_secret = 'e7VfVWDx6cj9dmMgwzM8mGEyNPNTimvFlE0D22D3fLPoD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

"""/***********************************************************************/"""

#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

#myStream.filter(track=[name_to_search])
#myStream.filter(track=[name_to_search], async=True)

"""/***********************************************************************/"""

def getDataFromMongo(name_of_collection):
    collection = db[name_of_collection + '_tweepy_collections']
    stringVarialble = " "
    for post in collection.find():
        stringVarialble = stringVarialble + "\n" + str(post)
    return stringVarialble

#Referencias:
#https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
#http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/
