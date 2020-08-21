import tweepy
import config


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token_key, config.access_token_secret)

api = tweepy.API(auth)

user_name = 'KingJames'
user = api.get_user(user_name)
print(user.screen_name)
print('------------------------------------')
print(user.followers_count)
print('------------------------------------')

tweets = api.user_timeline(user.screen_name, count=10)
for tweet in tweets:
    print(tweet.text)



print('------------------------------------')
print(tweets[0].text)

'''public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)'''

'''user = api.get_user('MKBHD')'''

'''print(user.screen_name)
print(user.followers_count)'''


'''for friend in user.friends():
   print(friend.screen_name)
'''


#print(tweets[0])

import json

status = tweets[0]

#convert to string
json_str = json.dumps(status._json)

#deserialise string into python object
parsed = json.loads(json_str)

print(json.dumps(parsed, indent=4, sort_keys=True))
