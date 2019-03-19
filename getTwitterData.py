import csv
from TwitterSearch import *
import sys #para resolver os emoji's

#para tratar emoji's
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#FUNÇÃO PATA CAPTURA DE DADOS DO Twitter
def getTwitterData(words, arquivo_csv):
    with open(arquivo_csv, encoding="utf-8", mode='w') as csv_file:
        colunas = ['name', 'screen_name', 'location', 'followers_count', 'friends_count',
                   'tweet']
        writer = csv.DictWriter(csv_file, fieldnames=colunas)
        writer.writeheader()

        try:

            ts = TwitterSearch(
                consumer_key = 'mgpSEJ1Fu9le1ND0iulsoWHaM',
                consumer_secret = 'HMvPmooVtTmiJkfwixOORifcUZz1C442AbYz2Nodg8k0kFKjjP',
                access_token = '1086082843476938753-6ax1DxzwPMrMfqmganAcnLJ31amKrI',
                access_token_secret = 'O7IT1RuvhO5KhhAF7Vf5uI5TekF3VaqrYjjosnH3nYwQ2')

            tso=TwitterSearchOrder()
            tso.set_keywords(words)
            tso.set_language('pt')

            #todos os dados enviados pelo Twitter
            result = ts.search_tweets_iterable(tso)

            #armazenar os dados no arquivo csv
            for tweet in result:
                writer.writerow({'name':str(tweet['user']['name']).translate(non_bmp_map), 'screen_name':str(tweet['user']['screen_name']).translate(non_bmp_map),
                                  'location':str(tweet['user']['location']).translate(non_bmp_map),
                                  'followers_count':str(tweet['user']['followers_count']).translate(non_bmp_map),
                                  'friends_count':str(tweet['user']['friends_count']).translate(non_bmp_map),
                                  'tweet':str(tweet['text']).translate(non_bmp_map)})
            return
        except TwitterSearchException as e:
            print(e)
            return
