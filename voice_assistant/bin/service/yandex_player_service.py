import os
import sys
from yandex_music import Client
from yandex_music.exceptions import YandexMusicError
from playsound import playsound
from configparser import NoOptionError, NoSectionError

from voice_assistant.bin.initialize.cache import cache, get_yandex_token_from_cache, YANDEX_TOKEN
from voice_assistant.bin.service.text_commands_resolver import print_command, return_command
from voice_assistant.bin.dict.text_commands_dictionary import INSERT_YA_LOGIN, INSERT_YA_PWD, YANDEX_LOGIN_ERROR
from voice_assistant.bin.service.config_service import read_credentials, write_credentials, YANDEX_BLOCK, TRACK_NAME, \
    YANDEX_TOKEN

config = read_credentials()


def yandex_authorize():
    token = get_yandex_token_from_cache()
    if not token:
        token = get_token_from_file()
        if not token:
            (login, pwd) = enter_credentials()
            token = get_token_by_credentials(login, pwd)
            save_token(token)

    return Client.from_token(token)


def play_yandex_last_favourite_track():
    client = yandex_authorize()

    client.users_likes_tracks()[0].fetch_track().download(TRACK_NAME)
    playsound(sys.path[0] + '/' + TRACK_NAME)
    os.remove(TRACK_NAME)


def write_token_to_cache(token):
    cache[YANDEX_TOKEN] = token


def enter_credentials():
    login = input(return_command(INSERT_YA_LOGIN))
    pwd = input(return_command(INSERT_YA_PWD))
    return login, pwd


def save_token(token):
    config[YANDEX_BLOCK] = {YANDEX_TOKEN: token}
    # TODO: writing of all blocks happens here
    write_credentials(config)


def get_token_by_credentials(login, pwd):
    try:
        token = Client().generate_token_by_username_and_password(login, pwd)
        write_token_to_cache(token)
        return token
    except YandexMusicError:
        print_command(YANDEX_LOGIN_ERROR)


def get_token_from_file():
    try:
        return config.get(YANDEX_BLOCK, YANDEX_TOKEN)
    except NoOptionError:
        pass
    except NoSectionError:
        pass
#
