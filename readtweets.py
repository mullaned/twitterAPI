import tweepy
from tweepy import OAuthHandler
import twitterKey

CONSUMER_KEY = twitterKey.CONSUMER_KEY
CONSUMER_SECRET = twitterKey.CONSUMER_SECRET
OAUTH_TOKEN = twitterKey.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = twitterKey.OAUTH_TOKEN_SECRET

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline).items(10):
    print(status.text)