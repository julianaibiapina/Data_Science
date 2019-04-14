#ANTIGO: https://github.com/tweepy/tweepy/blob/master/examples/streaming.py
#ATUAL: https://chrisalbon.com/python/other/mine_a_twitter_hashtags_and_words/
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv
import sys

#para tratar emoji's
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# Classe que pega os dados do Twitter e armazena no arquivo cvs
class StdOutListener(StreamListener):
    """docstring for StdOutListener."""

    def __init__(self, api= None):
        self.api = api
        self.filename = 'Data_14-04-TodasHashtags.csv'

        #cria a novo arquivo
        csvData = open(self.filename, 'w')

        #cria csv writer
        writer = csv.writer(csvData)

        #cria uma linha com os nomes de cada coluna
        writer.writerow([   'text',
                            'created_at',
                            'geo',
                            'lang',
                            'place',
                            'coordinates',
                            'user.favourites_count',
                            'user.statuses_count',
                            'user.description',
                            'user.location',
                            'user.id',
                            'user.created_at',
                            'user.verified',
                            'user.following',
                            'user.url',
                            'user.listed_count',
                            'user.followers_count',
                            'user.default_profile_image',
                            'user.utc_offset',
                            'user.friends_count',
                            'user.default_profile',
                            'user.name',
                            'user.lang',
                            'user.screen_name',
                            'user.geo_enabled',
                            'user.profile_background_color',
                            'user.profile_image_url',
                            'user.time_zone',
                            'id',
                            'favorite_count',
                            'retweeted',
                            'source',
                            'favorited',
                            'retweet_count'])
    # Quando aparece um tweet
    def on_status(self, status):

        #abre o csv
        csvData = open(self.filename, 'a')
        #cria csv writer
        writer = csv.writer(csvData)

        # Se o Tweet não for um RT
        if not 'RT @' in status.text:
            try:
                # Escreve as informações no csv
                writer.writerow([str(status.text).encode('ascii',errors='ignore'),
                                    status.created_at,
                                    status.geo,
                                    status.lang,
                                    str(status.place).encode('ascii',errors='ignore'),
                                    status.coordinates,
                                    status.user.favourites_count,
                                    status.user.statuses_count,
                                    str(status.user.description).encode('ascii',errors='ignore'),
                                    status.user.location,
                                    status.user.id,
                                    status.user.created_at,
                                    status.user.verified,
                                    status.user.following,
                                    status.user.url,
                                    status.user.listed_count,
                                    status.user.followers_count,
                                    status.user.default_profile_image,
                                    status.user.utc_offset,
                                    status.user.friends_count,
                                    status.user.default_profile,
                                    str(status.user.name).encode('ascii',errors='ignore'),
                                    status.user.lang,
                                    status.user.screen_name,
                                    status.user.geo_enabled,
                                    status.user.profile_background_color,
                                    status.user.profile_image_url,
                                    status.user.time_zone,
                                    status.id,
                                    status.favorite_count,
                                    status.retweeted,
                                    status.source,
                                    status.favorited,
                                    status.retweet_count])
                print(str(status.text).encode('ascii',errors='ignore'))

            except Exception as e:
                # Exibe o código do erro
                print(e)
                # e continua
                pass

        # Fecha o arquivo
        csvData.close()

        # Não retorna nada
        return

    # Quando um erro acontece
    def on_error(self, status_code):

        # Exibe o código do erro
        print('Erro encontrado. Código:', status_code)

        # Se o código do erro for 401, então é um erro de credencial incorreta
        if status_code == 401:
            # Termina a stream
            return False

    # Quando um tweet deletado aparece
    def on_delete(self, status_id, user_id):

        # Exibe mensagem
        print("Delete notice")

        # Não retorna nada
        return

    # Quando a taxa limite é alcançada
    def on_limit(self, track):

        # Ecibe a mensagem de limite de Erro
        print("Rate limited, continuing")

        # Continua minerando Tweets
        return True

    # Quando o tempo acaba
    def on_timeout(self):

        # Imprime mensagem de tempo esgotado
        print(sys.stderr, 'Timeout...')

        # Espera 10 segundos...
        time.sleep(10)

        # Não retorna nada
        return


# Função que realizará a mineraçao de Tweets
def start_mining(queries):
    ''' Recebe uma lista de argumentos de busca, e retorna os Tweets que possuem tais termos'''


    # Credenciais da API
    consumer_key = 'mgpSEJ1Fu9le1ND0iulsoWHaM'
    consumer_secret = 'HMvPmooVtTmiJkfwixOORifcUZz1C442AbYz2Nodg8k0kFKjjP'
    access_token = '1086082843476938753-6ax1DxzwPMrMfqmganAcnLJ31amKrI'
    access_token_secret = 'O7IT1RuvhO5KhhAF7Vf5uI5TekF3VaqrYjjosnH3nYwQ2'

    # Cria um listener
    listener = StdOutListener()

    # Cria a classe de atorização de acesso a API (authorization)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Cria um objeto Stream, com um listener e um authorization
    stream = Stream(auth, listener)

    # Filtra a stream usando as queries informadas e a linguagem português
    stream.filter(track=queries, languages=['pt'])


# Roda os códigos de mineração
start_mining(['governo', '#bozo', '#LulaLivre', 'bolsominions', '#BolsonaroEnvergonhaOBrasil', '#bolsolixo ', '#lulaLivreJá', '#PatriaAmadaBrasil', '#DireitaUnida', '#DireitaSegueDireita', '#Conservadorismo', '#BolsonaroOrgulhodoBrasil', '#Luladrão', '#PTNuncaMais'])
