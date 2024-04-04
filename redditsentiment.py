import openai
import praw
import os


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"

OPENAI_MODEL="gpt-3.5-turbo-instruct"



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
title_and_comments = {}
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
title_and_comments = get_titles_and_comments(subreddit="stocks")               
print(title_and_comments)

def create_prompt(title_and_comments):
    task = "Return the stock ticker or comapny name. Return the sentiment as positive negative or neutral"
    return task+title_and_comments
print(create_prompt(title_and_comments[1]))
# pip install openai==0.28
# Need this version of openAI for the coding to work correctly.

for key, title_with_comments in title_and_comments.items():
    prompt = create_prompt(title_with_comments)
    
    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=256,temperature=0, top_p=1.0)
    print(title_with_comments)
    print(f"Sentiment Analysis from openAI: {response['choices'][0]['text']}")
    

