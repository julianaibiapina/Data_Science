# Objetivo: armazenar em um .csv os usuários e os seus respectivos seguidores.
import csv
import pandas as pd
import tweepy
import time

#ASSUNTO DESEJADO
arquivo_csv = 'Data_30Abril-a-03Maio.csv'

#pega a base de dados e transforma em dataframe
dt_frame = pd.read_csv(arquivo_csv, encoding='ISO-8859-1')
print(dt_frame.info())

# Usuários que comentaram sobre política durante o período de coleta
users = dt_frame['user_screen_name'].drop_duplicates()


# Armazena todos os seguidores de um usuário pertencente a base de dados

consumer_key = 'u0W4cRMSNbJEaP2Bs5TWKcP86'
consumer_secret = 'fqAsaJsxiIhSvrnIFXCa7Ro01yAhWW0RIf6uMjv3Bu1nl5UA0v'
access_token = '1086082843476938753-ry4rjhmekNAJPPnYE6mp2D303wm3Yw'
access_token_secret = 'xK4gPSqm0GNhoNpoT6A9Bedlv55w0lOmT9YuycjKHrySN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Nome do arquivo onde os dados serão armazenados
file_name = 'Usuario-Seguidores.csv'

#cria o arquivo
csvData = open(file_name, 'w')

#cria csv writer
writer = csv.writer(csvData)

#cria uma linha com os nomes de cada coluna
writer.writerow(['usuário', 'seguidores'])

# Esse processo demora devido ao limite imposto pela API do Twitter
# https://developer.twitter.com/en/docs/basics/rate-limiting
for user in users:
    #ids = list()
    seguidores = ''
    print('Usuário atual: %s' % (user))
    for page in tweepy.Cursor(api.followers, screen_name=user).pages():
        status = page[0]
        print(status.screen_name)
        print('\n')
        seguidores = seguidores + status.screen_name + "/"
        #ids.append(status.screen_name)
    writer.writerow([user, seguidores])

print("Dados coletados com sucesso.")
# Fecha o arquivo
csvData.close()
