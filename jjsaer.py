#!/usr/bin/python
from twitter import *
import random

consumer_key = "u02X6PR1ZKRfdBN10SPNw"
consumer_secret = "amH1GJ7ZQTnUDAbiNebJ4WYtqiXEisAn4BjUUFu0Y"
access_key = "1036139623-bl9oAmOLIiAbeBGtYIXx6kfTrky9yGEfqnLZ9iJ"
access_secret = "D0u7bMwHWa9PVB4OXl3swqn9KffQ7VKr1sTYYuXOM"

auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

f = open('saertweets.txt', 'r').read().split('\n\n')
tweets = [x.strip() for x in f if x.strip()]
t = random.choice(tweets)
twitter.statuses.update(status=t)
