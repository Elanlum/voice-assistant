from yandex_music import Client
from playsound import playsound

import os
import sys
import cred_config_service as cred

config = cred.read_credentials()

yandex_block = cred.YANDEX_BLOCK
yandex_token = cred.YANDEX_TOKEN
yandex_login = cred.YANDEX_LOGIN
yandex_pwd = cred.YANDEX_PWD
track_name = cred.TRACK_NAME
cred_file = cred.CRED_PROPERTIES


def yandex_authorize():
    if config.has_option(yandex_block, yandex_token):
        token = config.get(yandex_block, yandex_token)
    else:
        login = config.get(yandex_block, yandex_login)
        pwd = config.get(yandex_block, yandex_pwd)

        token = Client().generate_token_by_username_and_password(login, pwd)
        write_token(token)

    return Client.from_token(token)


def play_yandex_last_favourite_track():
    client = yandex_authorize()

    client.users_likes_tracks()[0].fetch_track().download(track_name)
    playsound(sys.path[0] + '/' + track_name)
    os.remove(track_name)


def write_token(token):
    config.set(yandex_block, yandex_token, token)
    with open(cred_file, 'w') as configfile:
        config.write(configfile)

