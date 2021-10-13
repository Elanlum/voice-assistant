import os
import sys
from yandex_music import Client
from playsound import playsound
from voice_assistant.bin.initialize.cache import cache, get_yandex_token_from_cache, YANDEX_TOKEN
from voice_assistant.bin.service.text_commands_resolver import return_command
from voice_assistant.bin.dict.text_commands_dictionary import INSERT_YA_LOGIN, INSERT_YA_PWD

from voice_assistant.bin.service.config_service import read_credentials, write_credentials,  YANDEX_BLOCK, YANDEX_LOGIN, \
    YANDEX_PWD, TRACK_NAME

config = read_credentials()


def yandex_authorize():
    token = get_yandex_token_from_cache()
    if not token:
        login = config.get(YANDEX_BLOCK, YANDEX_LOGIN)
        pwd = config.get(YANDEX_BLOCK, YANDEX_PWD)

        if not login or not pwd:
            login = input(return_command(INSERT_YA_LOGIN))
            pwd = input(return_command(INSERT_YA_PWD))
            config['Yandex'] = {'yandex.login': login,
                                'yandex.password': pwd}
            # TODO: writing of all blocks happens here
            write_credentials(config)

        token = Client().generate_token_by_username_and_password(login, pwd)
        write_token_to_cache(token)

    return Client.from_token(token)


def play_yandex_last_favourite_track():
    client = yandex_authorize()

    client.users_likes_tracks()[0].fetch_track().download(TRACK_NAME)
    playsound(sys.path[0] + '/' + TRACK_NAME)
    os.remove(TRACK_NAME)


def write_token_to_cache(token):
    cache[YANDEX_TOKEN] = token
