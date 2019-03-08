import numpy as np
import pandas as pd
from os import path
from PIL import Image
import csv
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import TweetTokenizer

#instancia um objeto do tipo TweetTokenizer
#strip_handles=True -> irá remover mençoes a usuários do tweet
#reduce_len=True -> irá reduzir caracteres duplicados
#preserve_case=False -> irá alterar a forma da escrita, deixando tudo em minúsculo
tweet_tokenizer = TweetTokenizer(reduce_len=True, preserve_case=False)

#download da base de dados de léxicos da biblioteca e datasets
#nltk.download()


dt_frame = pd.read_csv('twitterData.csv', encoding='UTF-8')


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
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
wordcloud.to_file("wordCloud/TweetsGoverno.png")
# Display the generated image:
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()









#with open('wordCloud.csv', encoding="utf-8", mode='w') as csv_file:
#    writer = csv.DictWriter(csv_file, fieldnames=['tweets'])
#    writer.writeheader()

    #percorrer o data frame
#    for val in dt_frame.tweet:
#        writer.writerow({'tweets': val})
#        print('Tweet: %s \n\n' % (val))





