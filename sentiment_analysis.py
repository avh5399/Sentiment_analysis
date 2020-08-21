###############################################################
# imports
###############################################################
import pandas as pd 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string 
from collections import Counter
import matplotlib.pyplot as plt 
import get_tweets

###############################################################
# read csv and create a list of tweets 
###############################################################
def tweets_csv_to_list(file):
    tweets_list = []
    tweets = pd.read_csv(str(file))
    tweets_df = pd.DataFrame(tweets, columns=['tweet'])
    print(type(tweets_df['tweet'][0]))
    tweets_list.extend(tweet for tweet in tweets_df['tweet'])
        
    return tweets_list

###############################################################
# transfer tweets to text file 
###############################################################
def tweets_file(tweets_list):
    tweets_file = open("text.txt", "w")
    for line in tweets_list:
        tweets_file.write(line.encode('unicode-escape').decode('utf-8'))
    
    tweets_file.close()

###############################################################
# transfer tweets to text file 
###############################################################
def tweets_read_file():
    text = open('text.txt', encoding= 'utf-8').read()
    return text 

###############################################################
# convert text to lowercase and remove punctuation
###############################################################
def tweets_lower(text):
    lower = text.lower()
    clean_text = lower.translate(str.maketrans('','',string.punctuation))
    return clean_text

###############################################################
# preprocessing for tweets using nltk stopwords
###############################################################
def tweets_preprocessing(clean_text):
    tokenized = word_tokenize(clean_text, "english")

    final_text = []
    for word in tokenized:
        if word not in stopwords.words('english'):
            final_text.append(word)
    
    return final_text

###############################################################
# find the emotions in the tweets
###############################################################

def tweets_emotion(final_text):
    emotions_list =[]
    with open('emotions.txt', 'r') as file: 
        for line in file:
            final_line = line.replace('\n', '').replace(',','').replace("'",'').strip()
            word, emotion = final_line.split(':')
        
            if word in final_text:
                emotions_list.append(emotion)

    emotions_count = Counter(emotions_list)
    print(emotions_count)
    return emotions_count

###############################################################
# find sentiment score of the users tweets 
###############################################################
def tweets_sentiment_score(sentiment_text):
    sentiment_score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(sentiment_score)

###############################################################
# plot the graph of the different emotions 
###############################################################
def tweets_emotion_graph(emotions_count):
    fig, ax = plt.subplots()
    ax.bar(emotions_count.keys(), emotions_count.values())
    fig.autofmt_xdate()
    plt.title(str('Emotion Analysis of '))
    plt.savefig('emotions_count.png')
    plt.show()

###############################################################
# main
###############################################################
def main():
    tweets_list = tweets_csv_to_list('tweets.csv')
    tweets_file(tweets_list)
    text = tweets_read_file()
    clean_text = tweets_lower(text)
    final_text = tweets_preprocessing(clean_text)
    emotions_count = tweets_emotion(final_text)
    tweets_sentiment_score(clean_text)
    tweets_emotion_graph(emotions_count)

###############################################################
# driver code
###############################################################
if __name__ == '__main__': 
    main()
