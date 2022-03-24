import tweepy
from config import *


# auth = tweepy.OAuth1UserHandler(
#    API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
# )

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# Get the User object for twitter...
user = api.get_user(screen_name='havni25')
print(user.screen_name)
print(user.followers_count)
print(user.friends_count)
print("---------------------")
# for friend in user.friends():
#    print(friend.screen_name)

tweet = "#how i met your mother"

api.update_status(tweet)

