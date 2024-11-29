# utils.py
import praw
from nltk.corpus import stopwords
import re
from textblob import TextBlob

def preprocessPosts(original_post):
    stop_words = set(stopwords.words('english'))
    post = " ".join([word for word in original_post.split() if word.lower() not in stop_words])
    post = re.sub(r"http\S+", "", post)
    post = re.sub(r'[^\w\s#@/:%.,_-]', '', post)
    return post

def findPosts(topic, client_id, client_secret, user_agent):
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    posts = [submission.title + " " + submission.selftext for submission in reddit.subreddit("all").search(topic, limit=100)]
    return posts

def sentimentAnalysis(text):
    return TextBlob(text).sentiment.polarity