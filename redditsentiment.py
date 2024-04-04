import openai
import praw
import os


reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     user_agent="sentiment analysis test")
for submission in reddit.subreddit("technology").hot(limit=5):
    print(submission.title)