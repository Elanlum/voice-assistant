from yandex_music import Client
import configparser
from playsound import playsound

import os
import sys

CRED_PROPERTIES = 'cred.properties'
YANDEX_BLOCK = 'Yandex'
TRACK_NAME = 'yandex_track.mp3'


def yandex_authorize():
    config = configparser.RawConfigParser()
    config.read(CRED_PROPERTIES)

    if config.has_option(YANDEX_BLOCK, 'yandex.token'):
        token = config.get(YANDEX_BLOCK, 'yandex.token')
    else:
        login = config.get(YANDEX_BLOCK, 'yandex.login')
        pwd = config.get(YANDEX_BLOCK, 'yandex.password')

        token = Client().generate_token_by_username_and_password(login, pwd)
        write_token(config, token)

    return Client.from_token(token)


def play_yandex_last_favourite_track():
    client = yandex_authorize()

    client.users_likes_tracks()[0].fetch_track().download(TRACK_NAME)
    playsound(sys.path[0] + '/' + TRACK_NAME)
    os.remove('TRACK_NAME')


def write_token(config, token):
    config.set(YANDEX_BLOCK, 'yandex.token', token)
    with open(CRED_PROPERTIES, 'w') as configfile:
        config.write(configfile)

