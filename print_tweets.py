import tweepy
import sys

bearer = "AAAAAAAAAAAAAAAAAAAAAFbMawEAAAAAajRJCBDGboZZPnCcw7GSPMfODlA%3DdBAufO6Xt8NyNXx4Y2HHGCv2rTutJECFOMcZxaSAvLAEEvnIds"

client = tweepy.Client(bearer_token=bearer, wait_on_rate_limit=True)

for tweet in tweepy.Paginator(client.search_recent_tweets, sys.argv[1],
                              max_results=100).flatten(limit=3000):
    print(tweet.text.replace("\n", " "))

