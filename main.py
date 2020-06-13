import twitter
import praw
import time
def post_reddit(tweet):
    if "Woj" in tweet.user.name:
        name = "[Wojnarowski] "
        link = "https://twitter.com/wojespn/status/{}".format(tweet.id)
    else:
        name = "[Charania] "
        link = "https://twitter.com/ShamsCharania/status/{}".format(tweet.id)
    content = name + tweet.text

    r = praw.Reddit('bot1')
    to_submit = r.subreddit("nba")
    to_submit.submit(title = content, url = link)


f = open('config.ini', 'r+')
k = f.readlines()
api = twitter.Api(consumer_key=k[0][:-1],
                  consumer_secret=k[1][:-1],
                  access_token_key=k[2][:-1],
                  access_token_secret=k[3][:-1])
x = api.GetListTimeline(list_id=1271124228469907456, include_rts=False)
last_tweet = set()
last_tweet.add(x[0].text)
count = 0
while True: 
    x = api.GetListTimeline(list_id=1271124228469907456, include_rts=False)
    if count % 100 == 0:
        print(str(count) + ": "+ str(x))
    if x[0].text not in last_tweet:
        if "ESPN story" not in x[0].text and "@TheAthleticNBA:" not in x[0].text and "The Woj Pod" not in x[0].text and "@SportsCenter" not in x[0].text:
            post_reddit(x[0])
        last_tweet.add(x[0].text)
        print("{}: {}".format(x[0].user.name, x[0].text))
    count += 1 
    time.sleep(1)
    