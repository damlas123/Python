import tweepy
import pandas as pd


API_KEY = 'xnYNRziIS8eauwgynyCjkXObS'
API_SECRET_KEY = "yEBNKVZ9tSZtyzMyi7pBy39oB3m5K587JaI4DnE2GbV6daDQfM"
ACCESS_TOKEN = '1841415404197134336-gD02JTPdqNN5O1o0XyZoHTgBOaoNdE'
ACCESS_TOKEN_SECRET = 'dDgplfbbvotKEIqJry5wjAquUlKkqqsshLxS7gTDC0TLl'


auth = tweepy.OAuthHandler('xnYNRziIS8eauwgynyCjkXObS','yEBNKVZ9tSZtyzMyi7pBy39oB3m5K587JaI4DnE2GbV6daDQfM')
auth.set_access_token('1841415404197134336-gD02JTPdqNN5O1o0XyZoHTgBOaoNdE','dDgplfbbvotKEIqJry5wjAquUlKkqqsshLxS7gTDC0TLl')
api = tweepy.API(auth)

query = 'Matrix'
tweets = api.search_tweets(q=query, count=100, lang='en', tweet_mode='extended')

tweet_data = []

for tweet in tweets:
    tweet_data.append(tweet.full_text)


df = pd.DataFrame(tweet_data, columns=['Tweet'])


df.to_csv('matrix_tweets.csv', index=False)

print("Tweetler başarıyla toplandı ve 'matrix_tweets.csv' dosyasına kaydedildi.")