import tweepy
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
auth = tweepy.OAuthHandler("5Rd2PZ8KqWuHEuswsFtyQc0ob","ZgpoEHthem7DvbwSeN5U72yqbcIfeQtnIbJGyf3hmmGcK3RaAv")
api = tweepy.API(auth)
    
name_list=["kimkardashian", "khloekardashian", "kanyewest", "kyliejenner", "kendalljenner"]
goodWords = ['like', 'love', 'nice', 'sweet', 'good', 'happy', 'joy', 'yeah', 'awesome', 'wonderful', 'laugh', 'yes']
badWords = ['hate', 'no', 'bad', 'dirty', 'sad', 'nope', 'terrible', 'not', 'horrible', 'sucks', 'awful', 'yuck', 'nah']
with open("tweets.csv", "w", newline="") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["name", "sentiment_score", "vader_score", "retweet_count"])
    for name in name_list:
        tweet_data = api.user_timeline(screen_name=name, tweet_mode="extended",count=100)
        for tweet in tweet_data:
            text = tweet.full_text
            retweet_count = tweet.retweet_count
            split_text=text.split()
            goodcount = 0
            for word in goodWords:
                for tweetword in split_text:
                    if tweetword == word:
                        goodcount = goodcount + 1
            badcount = 0
            for word in badWords:
                for tweetword in split_text:
                    if tweetword == word:
                        badcount = badcount + 1
            sentiment_score=goodcount-badcount
            print(text, sentiment_score)
            analyzer = SentimentIntensityAnalyzer()
            vader_score=analyzer.polarity_scores(text)["compound"]
            print(vader_score)
            writer.writerow([name, sentiment_score, vader_score, retweet_count])
