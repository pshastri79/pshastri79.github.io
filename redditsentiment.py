import openai
import praw
import os


reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     user_agent="sentiment analysis test")
for submission in reddit.subreddit("technology").hot(limit=5):
    print(submission.title)
    
subreddit_stocks = reddit.subreddit("stocks")
subreddit_stocks.accounts_active

for post in subreddit_stocks.hot(limit=5):
    print(post.title)
    stock_sub = reddit.submission(post.id)
    counter = 0
    for subm in stock_sub.comments:
        print(subm)
        counter +=1
        if counter == 2:
            break

        