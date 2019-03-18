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
tweet_tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True, preserve_case=False)


getTwitterData.getTwitterData('governo', 'Governo-03-19.csv')
