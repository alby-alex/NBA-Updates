import twitter
f = open('config.ini', 'r+')
k = f.readlines()
print(k)
api = twitter.Api(consumer_key=k[0][:-1],
                  consumer_secret=k[1][:-1],
                  access_token_key=k[2][:-1],
                  access_token_secret=k[3][:-1])
x = api.GetListTimeline(list_id=1271124228469907456, include_rts=False)
print(x)