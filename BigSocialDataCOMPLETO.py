import numpy as np
import pandas as pd
from os import path
from PIL import Image
import sys
import csv
from TwitterSearch import *
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import TweetTokenizer

#INSTANCIA UM OBJETO DO TIPO TweetTokenizer
#strip_handles=True -> irá remover mençoes a usuários do tweet
#reduce_len=True -> irá reduzir caracteres duplicados
#preserve_case=False -> irá alterar a forma da escrita, deixando tudo em minúsculo
tweet_tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True, preserve_case=False)


#para tratar emoji's
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#ASSUNTO DESEJADO
word = 'mulher'
arquivo_csv = 'TwitterMulher.csv'
imagem_nuvem = "wordCloud/TweetsMulher.png"

with open(arquivo_csv, encoding="utf-8", mode='w') as csv_file:
    colunas = ['name', 'screen_name', 'location', 'followers_count', 'friends_count',
               'tweet']
    writer = csv.DictWriter(csv_file, fieldnames=colunas)
    writer.writeheader()

    #PEGANDO DADOS DO TWITTER
    try:

        ts = TwitterSearch(
            consumer_key = 'mgpSEJ1Fu9le1ND0iulsoWHaM',
            consumer_secret = 'HMvPmooVtTmiJkfwixOORifcUZz1C442AbYz2Nodg8k0kFKjjP',
            access_token = '1086082843476938753-6ax1DxzwPMrMfqmganAcnLJ31amKrI',
            access_token_secret = 'O7IT1RuvhO5KhhAF7Vf5uI5TekF3VaqrYjjosnH3nYwQ2'
         )

        tso = TwitterSearchOrder()
        tso.set_keywords([word])
        tso.set_language('pt')

        result = ts.search_tweets_iterable(tso)

    #GUARDANDO OS DADOS
        cont = 0
        for tweet in result:
            writer.writerow({'name':str(tweet['user']['name']).translate(non_bmp_map), 'screen_name':str(tweet['user']['screen_name']).translate(non_bmp_map),
                             'location':str(tweet['user']['location']).translate(non_bmp_map),
                             'followers_count':str(tweet['user']['followers_count']).translate(non_bmp_map),
                             'friends_count':str(tweet['user']['friends_count']).translate(non_bmp_map),
                             'tweet':str(tweet['text']).translate(non_bmp_map)})
            print('name: %s \n screen_name: %s \n location: %s \n followers_count: %s \n friends_count: %s \n tweet: %s \n\n' % (str(tweet['user']['name']).translate(non_bmp_map), str(tweet['user']['screen_name']).translate(non_bmp_map), str(tweet['user']['location']).translate(non_bmp_map), str(tweet['user']['followers_count']).translate(non_bmp_map), str(tweet['user']['friends_count']).translate(non_bmp_map), str(tweet['text']).translate(non_bmp_map)))
            #print('%s \n\n' % (str(tweet['user']['friends_count']).translate(non_bmp_map)))
            #print( '@%s tweetou: %s \n' % ( tweet['user']['location'], tweet['text'] ) )
            cont = cont+1

        print('Total de tweets: %s' % (cont))
        print("Fim <3")

    #CRIANDO A NUVEM DE PALAVRAS
        #pega a base de dados e transforma em dataframe
        dt_frame = pd.read_csv(arquivo_csv, encoding='UTF-8')
        #coloca todos os tweets em uma unica variável
        text = ''
        for val in dt_frame.tweet:
            #Tokeniza o tweet
            t = tweet_tokenizer.tokenize(val)
            #Transformar novamente em texto
            tweet = ''
            for tok in t:
                tweet = tweet + tok + ' '

            text = text + tweet + ' '
        # Create and generate a word cloud image:
        wordcloud = WordCloud(max_font_size=60, max_words=100, background_color="white").generate(text)
        wordcloud.to_file(imagem_nuvem)
        # Display the generated image:
        plt.figure()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()


    except TwitterSearchException as e:
        print(e)
