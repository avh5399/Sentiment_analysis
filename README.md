# Sentiment_analysis

## Sentiment Analysis of a user's tweets using tweepy and nltk
The aim of this project is to use Python's nltk library to perform natural language processing in order to detect the emotions in the user's tweets and generate a sentiment score. This project uses tweepy for handling Twitter API calls get a particular user's tweets. 

---
## get_tweets.py 
Uses Twitter's API through tweepy to get tweets of a particular twitter handle. The user can input the the desired twitter handle and a 'tweets.csv' file is generated containing the tweets of the entered twitter handle. 

---
## sentiment_analysis.py 
Uses Python's nltk library to output a sentiment score of the tweets. Preprocessing is done using the nltk.corpus stopwords and nltk.word_tokenize followed by emotion detection for the tweets. The 'emotions_count.png' is a graph showing the prominent emotions present in the user's tweets. Finally the sentiment score is calculated with nltk's SentimentIntensityAnalyzer module.

For this example I have used Lebron James' latest tweets (as of 20 August 2020)
https://twitter.com/KingJames?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor

![alt text](https://github.com/avh5399/Sentiment_analysis/blob/master/emotions_count.png)
