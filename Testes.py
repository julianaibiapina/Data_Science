import numpy as np
import pandas as pd
import sys #para resolver os emoji's
import csv
from TwitterSearch import *
import nltk
from nltk.tokenize import TweetTokenizer
from wordcloud import WordCloud

import getTwitterData

#INSTANCIA UM OBJETO DO TIPO TweetTokenizer
#strip_handles=True -> irá remover mençoes a usuários do tweet
#reduce_len=True -> irá reduzir caracteres duplicados
#preserve_case=False -> irá alterar a forma da escrita, deixando tudo em minúsculo
tweet_tokenizer = TweetTokenizer()

list_words = ['governo']
arquivo_csv = 'Governo02-Março-2019.csv'

#pega os dados do Twitter e salva no .csv
#getTwitterData.getTwitterData(list_words, arquivo_csv)

#transforma o csv em dataframe
dt_frame = pd.read_csv(arquivo_csv, encoding='UTF-8')

#LIMPEZA DE DADOS
#https://medium.com/data-hackers/dicas-de-data-cleaning-44d050e712bc
#https://medium.com/lucas-oliveira/limpeza-e-prepara%C3%A7%C3%A3o-dos-dados-com-pandas-856e844abfbb
#http://felipegalvao.com.br/blog/2016/02/29/manipulacao-de-dados-com-python-pandas/

#REMOVE TODAS AS LINHAS QUE POSSUEM TWEETS DUPLICADOS
dt_frame = dt_frame.drop_duplicates('tweet')


dt_frame['hashtags'] = 'null'
#coloca todas as hashtags em uma nova coluna e as remove do tweet
for index, row in dt_frame.iterrows():
    tweet_tokens = tweet_tokenizer.tokenize(row['tweet'])
    hashtags = list() #guarda todos as hashtags de um tweet em uma lista
    for token in tweet_tokens:
        if(token[0] == '#'):
            hashtags.append(token)
    #------------------------------------------> PAREI AQUI!!!! <-----------------------------------------
    # COMO ATRIBUIR O VALOR REFERENTE A ESSA COLUNA NESSA LINHAS ESPECÍFICA.
    # IDEIA: CRIAR UMA series E POVOAR ELA COM AS hashtags E DEPOIS CRIAR A COLUNA E ATRIBUIR ESSA series
    #  dt_frame.loc[:, 'hashtags'] = seriesCriada.loc[:, 'A']
    #Fonte: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
    dt_frame.iloc[index]['hashtags'] = hashtags

    print(dt_frame.loc[index]['hashtags'])
print('\n\n------------------------>Exclusão feita\n\n')



#for index, row in dt_frame.iterrows():
#    print(row['hashtags'])

# transformar o DataFrame em .csv
#dt_frame.to_csv('dadosLimpos.csv', encoding='utf-8', index=False)

# apagar linha do dataframe
#dt_frame.drop(labels=index, inplace=True)

#percorre cada linha do DataFrame, podendo fazer operações em cada elemento da linha
#for index, row in dt_frame.iterrows() :
    #print('nome: %s \nscreen_name: %s' % (row['name'], row['screen_name']))
    #row['tweet'].replace('RT', '')
