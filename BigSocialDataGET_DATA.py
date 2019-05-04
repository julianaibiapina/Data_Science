#REFERÊNCIAS:
#http://minerandodados.com.br/index.php/2018/03/20/twitter-com-python/

import pandas as pd
import sys
import csv
from TwitterSearch import *
import tweepy

#para tratar emoji's
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


with open('twitterData.csv', encoding="utf-8", mode='w') as csv_file:
    colunas = ['created_at', 'tweet', 'user_name', 'user_screen_name', 'user_location',
               'user_description', 'user_followers_count', 'user_friends_count', 'user_created_at', 'coordinates', 'place']
    writer = csv.DictWriter(csv_file, fieldnames=colunas)
    writer.writeheader()

    #PEGANDO DADOS DO TWITTER
    try:

        ts = TwitterSearch(
            consumer_key = '8QtmEE1HWvcFlp5WoU7i5MNfk',
            consumer_secret = 'QCh2qo9ZW2p4lbTwjnjDpHUbmPPgk2Mi2aFpzeegVZH3PRZPPX',
            access_token = '1086082843476938753-cgDTEfWt3GxXJ2OtSvwOtS4DQ1GxeD',
            access_token_secret = 'KCUZvATUr1yibFVh8iaC0QWr5UKMbQnAWOGkzGBxRBV1U'
         )

        # # # # DOCUMENTAÇÃO:
        # # # # https://twittersearch.readthedocs.io/en/latest/advanced_usage_tso.html
        tso = TwitterSearchOrder()
        tso.set_geocode(-3.71839,-38.5434,300,imperial_metric=True)
        tso.set_keywords(['governo']) #esse parâmetro é obrigatório
        #tso.set_language('pt')

        result = ts.search_tweets_iterable(tso)

    #GUARDANDO OS DADOS
        cont = 0
        for tweet in result:
            writer.writerow({'created_at':str(tweet['created_at']).translate(non_bmp_map),
                             'tweet':str(tweet['text']).translate(non_bmp_map),
                             'user_name':str(tweet['user']['name']).translate(non_bmp_map),
                             'user_screen_name':str(tweet['user']['screen_name']).translate(non_bmp_map),
                             'user_location':str(tweet['user']['location']).translate(non_bmp_map),
                             'user_description':str(tweet['user']['description']).translate(non_bmp_map),
                             'user_followers_count':str(tweet['user']['followers_count']).translate(non_bmp_map),
                             'user_friends_count':str(tweet['user']['friends_count']).translate(non_bmp_map),
                             'user_created_at':str(tweet['user']['created_at']).translate(non_bmp_map),
                             'coordinates':str(tweet['coordinates']).translate(non_bmp_map),
                             'place':str(tweet['place']).translate(non_bmp_map)})

            #print('name: %s \n screen_name: %s \n location: %s \n followers_count: %s \n friends_count: %s \n tweet: %s \n\n' % (str(tweet['user']['name']).translate(non_bmp_map), str(tweet['user']['screen_name']).translate(non_bmp_map), str(tweet['user']['location']).translate(non_bmp_map), str(tweet['user']['followers_count']).translate(non_bmp_map), str(tweet['user']['friends_count']).translate(non_bmp_map), str(tweet['text']).translate(non_bmp_map)))
            print('Location: %s \n' % (str(tweet['text']).translate(non_bmp_map)))
            #print( '@%s tweetou: %s \n' % ( tweet['user']['location'], tweet['text'] ) )
            cont = cont+1

        print('Total de tweets: %s' % (cont))
        print("Fim <3")


    except TwitterSearchException as e:
        print(e)
