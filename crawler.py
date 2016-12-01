import sys
import tweepy
import json
import pymongo
import datetime
from pymongo import MongoClient


"""/***********************************************************************/"""

print "\n Starting... \n"
name_to_search = sys.argv[1]

"""/***********************************************************************/"""

#inicia MongoDB e cria-se os bancos necessarios
client = MongoClient()
db = client['tweepy_database']
collection = db[name_to_search + '_tweepy_collections']

"""/***********************************************************************/"""

#Classe do tweepy responsavel por armazenar os Twittes no mongoDB
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if (status.coordinates):
            collection.insert_one(status._json)
            #jsonVar = "{text: \"" + status.text.encode('utf-8') + "\", coordinates: " + str(status.coordinates)+ ", created_at: \"" + str(status.created_at) + "\", word: \"" + str(name_to_search) + "\"}"
            #print jsonVar
            #jsonDump = json.dumps(jsonVar)
            #jsonLoad = json.loads(jsonDump)
            #collection.insert_one(jsonLoad)
            file = open(name_to_search + "_tweepy_collections.txt", "a")
            file.write(status.text.encode('utf-8') + " |_| " + str(status.coordinates))
            file.write("\n")
            variable = 0
            for post in collection.find():
                print post
                print variable
                variable = variable+1


"""/***********************************************************************/"""

consumer_key = 'x0GzRIsgrn6PiuxmON0qEEVBU'
consumer_secret = 'GApQR5aIeVCXxdV3ZLTdeiA6OGG6UQleHZnD8E2LBCJcdRAKZh'
access_token = '144667001-t3zoMPJOg8d9m0E21ukGsdMSdFPkF04fhu1BaMKO'
access_secret = 'e7VfVWDx6cj9dmMgwzM8mGEyNPNTimvFlE0D22D3fLPoD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

"""/***********************************************************************/"""

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track=[name_to_search])
#myStream.filter(track=[name_to_search], async=True)

"""/***********************************************************************/"""

#Referencias:
#https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
#http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/
