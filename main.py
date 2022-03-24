import tweepy
from config import *


# auth = tweepy.OAuth1UserHandler(
#    API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
# )

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

username = "havni25"


# Get the User object for twitter...
user = api.get_user(screen_name = username)
print(user.screen_name)
print(user.followers_count)
print(user.friends_count)
print("---------------------")
# for friend in user.friends():
#    print(friend.screen_name)


def get_followingList():
   for friend in user.friends():
      print(friend.screen_name)
       

def post_tweet(tweet_text):
   api.update_status(tweet_text)

def get_user_tweets():
   user_tweets = api.user_timeline()
   tweetList = []
   for tweet in user_tweets:
      print(tweet.id_str)
      print(tweet.text)
      tweetList.append({
         "id": tweet.id,
         "text": tweet.text
      })
   
   return tweetList

      
def delete_tweet(id):
   api.destroy_status(id)
   


print(get_user_tweets())


