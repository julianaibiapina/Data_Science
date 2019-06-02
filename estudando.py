import time
import tweepy
import csv

# Credenciais da API
consumer_key = 'u0W4cRMSNbJEaP2Bs5TWKcP86'
consumer_secret = 'fqAsaJsxiIhSvrnIFXCa7Ro01yAhWW0RIf6uMjv3Bu1nl5UA0v'
access_token = '1086082843476938753-ry4rjhmekNAJPPnYE6mp2D303wm3Yw'
access_token_secret = 'xK4gPSqm0GNhoNpoT6A9Bedlv55w0lOmT9YuycjKHrySN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

users = tweepy.Cursor(api.followers, screen_name="andressa_sdo").items()


HEADER = ['Screenname']


def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)

    while True:
        try:
            user = next(users)
        except tweepy.TweepError:
            time.sleep(60*20)
            user = next(users)
        except StopIteration:
            break
        csv_writer.writerow([user.screen_name])
        csvfile.flush()
        time.sleep(5)

with open('results.csv', 'w') as csvfile:
    processing_loop(csvfile)
