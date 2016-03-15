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

user = api.get_user('@Explorers')

print(user.screen_name)
print (user.followers_count)

for friend in user.friends():
    print
    print(friend.screen_name)
    print (friend.followers_count)