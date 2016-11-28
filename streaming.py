from slistener import SListener
import time, tweepy, sys

## authentication
username = '' ## put a valid Twitter username here
password = '' ## put a valid Twitter password here

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#auth     = tweepy.auth.BasicAuthHandler(username, password)
api      = tweepy.API(auth)

consumer_key = 'x0GzRIsgrn6PiuxmON0qEEVBU'
consumer_secret = 'GApQR5aIeVCXxdV3ZLTdeiA6OGG6UQleHZnD8E2LBCJcdRAKZh'
access_token = '144667001-t3zoMPJOg8d9m0E21ukGsdMSdFPkF04fhu1BaMKO'
access_secret = 'e7VfVWDx6cj9dmMgwzM8mGEyNPNTimvFlE0D22D3fLPoD'

def main():
    track = ['obama', 'romney']

    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try:
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
