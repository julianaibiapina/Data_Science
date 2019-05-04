# Objetivo: armazenar em um dataframe os usuários e os seus respectivos seguidores.
import csv
import pandas as pd
import tweepy

#ASSUNTO DESEJADO
arquivo_csv = 'Data_30Abril-a-03Maio.csv'

#pega a base de dados e transforma em dataframe
dt_frame = pd.read_csv(arquivo_csv, encoding='ISO-8859-1')
#print(dt_frame.info())

# Usuários que comentaram sobre política durante o período de coleta
users = dt_frame['user_screen_name'].drop_duplicates()
print(type(users))

# Armazena todos os amigos(aqueles a quem ele segue) de um usuário
consumer_key = '8QtmEE1HWvcFlp5WoU7i5MNfk'
consumer_secret = 'QCh2qo9ZW2p4lbTwjnjDpHUbmPPgk2Mi2aFpzeegVZH3PRZPPX'
access_token = '1086082843476938753-cgDTEfWt3GxXJ2OtSvwOtS4DQ1GxeD'
access_token_secret = 'KCUZvATUr1yibFVh8iaC0QWr5UKMbQnAWOGkzGBxRBV1U'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Esse processo demora devido ao litite imposto pela API do Twitter
for user in users:
    print('Usuário atual: %s' % (user))
    user = api.get_user(screen_name=user)
    print('Amigos:')
    for friend in tweepy.Cursor(api.friends).items():
        print('\t %s' % (friend.screen_name))
# Deve estar dentro do laço para
# user = api.get_user(screen_name='Ju_Ibiapina')
# print ("My Twitter Handle: " +  str(user.screen_name))
# ct = 0
#
# for friend in tweepy.Cursor(api.friends).items():
#     # Process the friend here
#     print(friend.screen_name)
#     ct += 1
#
# print ("\n\nFinal Count: " + str(ct))
