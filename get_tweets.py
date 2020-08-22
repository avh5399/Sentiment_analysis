###############################################################
# imports
###############################################################
import config
import tweepy
import pandas as pd 

###############################################################
# authorize twitter
###############################################################
def auth_init(consumer_key,
              consumer_secret,
              access_token_key,
              access_token_secret
              ):
    #Twitter API Oatuh           
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #replace with your own consumer key and consumer secret key
    auth.set_access_token(access_token_key, access_token_secret) #replace with your own access tokey key and acccess toke nsecret key 

    api = tweepy.API(auth)
    return api

###############################################################
# get tweets of user
###############################################################
def get_tweets(userID):
    tweets_data = []
    api = auth_init(config.consumer_key, config.consumer_secret, config.access_token_key, config.access_token_secret) #pass your won twiiter api credentials 
    
    tweets = api.user_timeline(screen_name=userID,
                               count=10,
                               include_rts=False,
                               tweet_mode='extended'
                               )
    tweets_data.extend(tweets)
    oldest_tweet = tweets_data[-1].id-1

    while(len(tweets) > 0):
        tweets = api.user_timeline(screen_name=userID,
                                   count=200,
                                   include_rts=False,
                                   max_id=oldest_tweet,
                                   tweet_mode='extended'
                                   )
        tweets_data.extend(tweets)
        oldest_tweet = tweets_data[-1].id-1
        print('tweets downloaded till now {}'.format(len(tweets_data)))

    return tweets_data

###############################################################
# get tweets of user
###############################################################
def get_tweets_text(tweets_data):
    tweets_text = []
    tweets_text.extend([str(tweet.full_text)] for tweet in tweets_data) #store only the text of the tweets 
    return tweets_text

###############################################################
# convert list of tweets to csv file 
###############################################################
def tweets_csv(tweets):
    tw_df = pd.DataFrame(tweets, columns=["tweet"])
    tw_df.to_csv('tweets.csv', index = False, encoding='utf-8') #create 'tweets.csv' to store tweets 

###############################################################
# main
###############################################################
def main():
    user_entry = input('Enter twitter handle: ')
    tweets_arr = get_tweets(user_entry)
    tweet_text_data = get_tweets_text(tweets_arr)
    print('latest tweet:\n{}'.format(tweet_text_data[0]))
    tweets_csv(tweet_text_data)

###############################################################
# driver code
###############################################################
if __name__ == '__main__': 
    main()
