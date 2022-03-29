import tweepy
import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()




# username = "havni25"


# Get the User object for twitter...
# user = api.get_user(screen_name = username)

class TwitterAccount():
   def __init__(self, username="havni25"):
      auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
      auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
      self.api = tweepy.API(auth)
      self.user = self.api.get_user(screen_name = username)
      
   def get_followingList(self):
      for friend in self.user.friends():
         print(friend.screen_name)

   def post_tweet(self, tweet_text):
      self.api.update_status(tweet_text)

   def get_user_tweets(self):
      user_tweets = self.api.user_timeline(count=100)
      tweetList = []
      for tweet in user_tweets:
         # print(tweet.id_str)
         # print(tweet.text)
         tweetList.append({
            "id": tweet.id,
            "text": tweet.text
         })
      
      return tweetList

         
   def delete_tweet(self, id):
      self.api.destroy_status(id)
   
   def getUserBasicInfo(self): 
      
      print('Account user name: {0}'.format(self.user.screen_name))
      print('Followers: {0}'.format(self.user.followers_count))
      print('Following: {0}'.format(self.user.friends_count))
      print('Tweets: {0}'.format(self.user.statuses_count))

      print("---------------------")


def getWeatherData(cityname):
   res = requests.get('https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric'.format(cityname, os.getenv("WEATHER_API_KEY")));
   pprint(res.json()["main"]["temp"])
   return res.json()

# post the given city's temperature in a tweet
def postTemp(cityname):
   t = getWeatherData(cityname)["main"]["temp"]
   if t is not None:
      post_tweet('temp in Berlin is {0} C. '.format(t))
      pprint("tweet posted!!")
   else:
      print("can not post tweet. no data!!!")



c = TwitterAccount("elonmusk")
c.getUserBasicInfo()


