#!/usr/bin/python
from twitter import *
import random
import os
import json

consumer_key = "u02X6PR1ZKRfdBN10SPNw"
consumer_secret = "amH1GJ7ZQTnUDAbiNebJ4WYtqiXEisAn4BjUUFu0Y"
access_key = "1036139623-bl9oAmOLIiAbeBGtYIXx6kfTrky9yGEfqnLZ9iJ"
access_secret = "D0u7bMwHWa9PVB4OXl3swqn9KffQ7VKr1sTYYuXOM"

auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

if not os.path.exists('saertweets.dump'):
    f = open('saertweets.txt', 'r').read().split('\n\n')
    dump = open('saertweets.dump', 'w+')
    json.dump([x.strip() for x in f if x.strip()], dump)
    dump.close()

dump = open('saertweets.dump', 'r')
tweets = json.load(dump)
dump.close()
if not tweets:
    f = open('saertweets.txt', 'r').read().split('\n\n')
    dump = open('saertweets.dump', 'w+')
    tweets = [x.strip() for x in f if x.strip()]
    json.dump(tweets, dump)
    dump.close()
random.shuffle(tweets)
t = tweets.pop()
dump = open('saertweets.dump', 'w+')
json.dump(tweets, dump)
dump.close()
twitter.statuses.update(status=t)
print "tweets left: ", len(tweets)
print t
