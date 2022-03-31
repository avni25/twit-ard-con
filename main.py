import tweepy
import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()


class TwitterAccount():
   def __init__(self, username="havni25"):
      auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
      auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
      self.api = tweepy.API(auth)
      self.user = self.api.get_user(screen_name = username)
      
   def followings(self):
      for friend in self.user.friends():
         print(friend.screen_name)

   def post(self, tweet_text):
      self.api.update_status(tweet_text)

   def get_tweets(self):
      user_tweets = self.api.user_timeline(count=100)
      tweetList = []
      for tweet in user_tweets:
         print(tweet.id_str)
         print(tweet.text)
         print(tweet.created_at)
         tweetList.append({
            "id": tweet.id,
            "created_at": tweet.created_at,
            "text": tweet.text
         })
      
      return tweetList

         
   def delete_tweet(self, id):
      self.api.destroy_status(id)
   
   def info(self):       
      print('User name: {0}'.format(self.user.screen_name))
      print('Followers: {0}'.format(self.user.followers_count))
      print('Following: {0}'.format(self.user.friends_count))
      print('Tweets: {0}'.format(self.user.statuses_count))

      print("---------------------")


def getWeatherData(cityname):
   res = requests.get('https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric'.format(cityname, os.getenv("WEATHER_API_KEY")));
   pprint(res.json()["main"]["temp"])
   return res.json()




# c = TwitterAccount("elonmusk")
# pprint(c.get_tweets())

