import os
import sys
from yandex_music import Client
from playsound import playsound
from config_service import read_credentials, YANDEX_BLOCK, YANDEX_TOKEN, YANDEX_LOGIN, YANDEX_PWD, TRACK_NAME, \
    CRED_PROPERTIES

config = read_credentials()


def yandex_authorize():
    if config.has_option(YANDEX_BLOCK, YANDEX_TOKEN):
        token = config.get(YANDEX_BLOCK, YANDEX_TOKEN)
    else:
        login = config.get(YANDEX_BLOCK, YANDEX_LOGIN)
        pwd = config.get(YANDEX_BLOCK, YANDEX_PWD)

        token = Client().generate_token_by_username_and_password(login, pwd)
        write_token(token)

    return Client.from_token(token)


def play_yandex_last_favourite_track():
    client = yandex_authorize()

    client.users_likes_tracks()[0].fetch_track().download(TRACK_NAME)
    playsound(sys.path[0] + '/' + TRACK_NAME)
    os.remove(TRACK_NAME)


def write_token(token):
    config.set(YANDEX_BLOCK, YANDEX_TOKEN, token)
    with open(CRED_PROPERTIES, 'w') as configfile:
        config.write(configfile)

