import tweepy
from config import *


auth = tweepy.OAuth1UserHandler(
   API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# Get the User object for twitter...
user = api.get_user(screen_name='havni25')
print("user screen name: "+user.screen_name)
print('followers: {0}'.format(user.followers_count))
print('following: {0}'.format(user.friends_count))
for friend in user.friends():
   print(friend.screen_name)