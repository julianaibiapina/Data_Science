# # # # REFERENCES # # # #
# https://www.youtube.com/watch?v=wlnx-7cm4Gg

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv


# # # # CREDENCIAIS # # # #
ACCESS_TOKEN = "1086082843476938753-6ax1DxzwPMrMfqmganAcnLJ31amKrI"
ACCESS_TOKEN_SECRET = "O7IT1RuvhO5KhhAF7Vf5uI5TekF3VaqrYjjosnH3nYwQ2"
CONSUMER_KEY = "mgpSEJ1Fu9le1ND0iulsoWHaM"
CONSUMER_SECRET = "HMvPmooVtTmiJkfwixOORifcUZz1C442AbYz2Nodg8k0kFKjjP"

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():

    # Class for streaming and processing live tweets.

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)

# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    #This is a basic listener that just prints received tweets to stdout.

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True


    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["donal trump", "hillary clinton", "barack obama", "bernie sanders"]
    fetched_tweets_filename = "tweeeeets.csv"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
