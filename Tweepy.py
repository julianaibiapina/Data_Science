from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="mgpSEJ1Fu9le1ND0iulsoWHaM"
consumer_secret="HMvPmooVtTmiJkfwixOORifcUZz1C442AbYz2Nodg8k0kFKjjP"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1086082843476938753-6ax1DxzwPMrMfqmganAcnLJ31amKrI"
access_token_secret="O7IT1RuvhO5KhhAF7Vf5uI5TekF3VaqrYjjosnH3nYwQ2"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
stream.filter(track=['#DireitaUnida'])
