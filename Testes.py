import numpy as np
import pandas as pd
import sys #para resolver os emoji's
import csv
import nltk
from nltk.tokenize import TweetTokenizer
from wordcloud import WordCloud

#INSTANCIA UM OBJETO DO TIPO TweetTokenizer
#strip_handles=True -> irá remover mençoes a usuários do tweet
#reduce_len=True -> irá reduzir caracteres duplicados
#preserve_case=False -> irá alterar a forma da escrita, deixando tudo em minúsculo
tweet_tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True, preserve_case=False)
