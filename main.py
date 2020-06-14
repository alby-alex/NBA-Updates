import twitter
import praw
import time
import re
import sys
def post_reddit(tweet, link):

    content = name + tweet.text
    index = content.index('http')
    content = content[0:index]
    z = open('success.txt', 'w+')
    z.write(content)
    print(content)
    # r = praw.Reddit('bot1')
    # to_submit = r.subreddit("nba")
    # to_submit.submit(title = content, url = link)


f = open('config.ini', 'r+')
k = f.readlines()
api = twitter.Api(consumer_key=k[0][:-1],
                  consumer_secret=k[1][:-1],
                  access_token_key=k[2][:-1],
                  access_token_secret=nek[3][:-1], 
                  tweet_mode = 'extended')
tweet_id = int(re.findall(r'\d+', sys.argv[1])[0])
x = api.GetStatus(status_id = tweet_id)
post_reddit(x, sys.argv[1])
    