import numpy as np
import pandas as pd
from os import path
from PIL import Image
import sys
import csv
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#INSTANCIA UM OBJETO DO TIPO TweetTokenizer
#strip_handles=True -> irá remover mençoes a usuários do tweet
#reduce_len=True -> irá reduzir caracteres duplicados
#preserve_case=False -> irá alterar a forma da escrita, deixando tudo em minúsculo
tweet_tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True, preserve_case=False)

#para tratar emoji's
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#ASSUNTO DESEJADO
arquivo_csv = 'TwitterGoverno.csv'

#pega a base de dados e transforma em dataframe
dt_frame = pd.read_csv(arquivo_csv, encoding='UTF-8')

#coloca todos os tweets em uma única variável de texto
text = ''
for val in dt_frame.tweet:
    text = text + val + ' '

#Tokeniza os tweets
tokens = tweet_tokenizer.tokenize(text)

#Palavras que não agregam informações para serem tiradas
stopwords = nltk.corpus.stopwords.words('portuguese')
descarte = ['.', ':', '...', '!', ';', 'rt', ',', 'é', '?','"', 'https']
stopwords = stopwords + descarte

print('stopwords: %s \n' % (stopwords))

print('Antes da limpeza: %s \n' % (len(tokens)))

#Processo de limpeza de dados
for token in tokens:
    if (token[:8] == 'https://'):
        tokens.remove(token)
    else:
        for x in stopwords:
            if(x == token):
                tokens.remove(token)

            
        #if token in stopwords:
        #    tokens.remove(token)

print('Depois da limpeza: %s \n' % (len(tokens)))

#transforma a list de tokens em uma grande string que será a entrada para a geração da WordCloud
tokens_str = ' '.join(tokens)

#Criação da nuvem de palavras
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tokens_str)
wordcloud.to_file("wordCloud/TweetsGoverno3.png")


