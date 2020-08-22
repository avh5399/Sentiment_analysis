import tweepy
import config


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret) #replace with your own consumer key and consumer secret key
auth.set_access_token(config.access_token_key, config.access_token_secret) #replace with your own access tokey key and acccess toke nsecret key 

api = tweepy.API(auth)

user_name = 'KingJames' # use the twiiter handle of the desired user 
user = api.get_user(user_name)
print(user.screen_name)
print('------------------------------------')

print(user.followers_count)
print('------------------------------------')

#get the 'count' number of tweets from the user's twitter handle 
tweets = api.user_timeline(user.screen_name, count=10)
for tweet in tweets:
    print(tweet.text)
print('------------------------------------')

print(tweets[0].text)
print('------------------------------------')

import json

# view tweet object in json form for easier data handling 
status = tweets[0]

#convert to string
json_str = json.dumps(status._json)

#deserialise string into python object
parsed = json.loads(json_str)

print(json.dumps(parsed, indent=4, sort_keys=True))
