import numpy as np
import pandas as pd
import csv
import nltk
from nltk.tokenize import TweetTokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from TwitterSearch import *

try:
    tuo = TwitterUserOrder('Ju_Ibiapina') # create a TwitterUserOrder

    # it's about time to create TwitterSearch object again
    ts = TwitterSearch(
        consumer_key = 'mgpSEJ1Fu9le1ND0iulsoWHaM',
        consumer_secret = 'HMvPmooVtTmiJkfwixOORifcUZz1C442AbYz2Nodg8k0kFKjjP',
        access_token = '1086082843476938753-6ax1DxzwPMrMfqmganAcnLJ31amKrI',
        access_token_secret = 'O7IT1RuvhO5KhhAF7Vf5uI5TekF3VaqrYjjosnH3nYwQ2'
    )

    # start asking Twitter about the timeline
    for tweet in ts.search_tweets_iterable(tuo):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # catch all those ugly errors
    print(e)
