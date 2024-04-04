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

def get_titles_and_comments(subreddit="stocks",limit=5,skip_rate=2):
    subreddit_out = reddit.subreddit(subreddit)
    
    title_and_comments = {}
    counter = 0
    
    for counter, post in enumerate(subreddit_out.hot(limit=limit)):
        if counter < skip_rate:
            continue
        counter += (1-skip_rate)
        title_and_comments[counter] = ""
        submission = reddit.submission(post.id)
        
        title = post.title
        title_and_comments[counter] = "Title:" +title+ "\n\n"
        title_and_comments[counter]  = "Comments" +"\n\n"
        comment_counter = 0
        for comment in submission.comments:
            if not comment.body == "[deleted]":
                title_and_comments[counter] += comment.body
                comment_counter += 1
            if comment_counter > 3:
                break
    return(title_and_comments)
                
print(get_titles_and_comments(subreddit="stocks"))