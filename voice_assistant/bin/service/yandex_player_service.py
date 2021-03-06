import os
import sys
from yandex_music import Client
from yandex_music.exceptions import BadRequest
from playsound import playsound

from voice_assistant.bin.initialize.cache import cache, get_yandex_token_from_cache
from voice_assistant.bin.service.auto_commands_resolver import print_command, return_command
from voice_assistant.bin.dict.auto_response_dictionary import INSERT_YA_LOGIN, INSERT_YA_PWD, YANDEX_LOGIN_ERROR
from voice_assistant.bin.service.config_service import read_credentials, write_credentials, get_from_cred_file
from voice_assistant.bin.util.constants import YANDEX_TOKEN, YANDEX_BLOCK, TRACK_NAME

configurer = read_credentials()


def yandex_authorize():
    token = get_yandex_token_from_cache()
    if not token:
        token = get_from_cred_file(YANDEX_BLOCK, YANDEX_TOKEN)
        if not token:
            token = request_token_and_save()

    return Client.from_token(token)


def play_yandex_last_favourite_track():
    try:
        client = yandex_authorize()
        client.users_likes_tracks()[0].fetch_track().download(TRACK_NAME)
        playsound(sys.path[0] + '/' + TRACK_NAME)
        os.remove(TRACK_NAME)
    except BadRequest:
        print_command(YANDEX_LOGIN_ERROR)


def request_token_and_save():
    (login, pwd) = enter_credentials()
    token = get_token_by_credentials(login, pwd)
    write_token_to_cache(token)
    save_token(token)
    return token


def enter_credentials():
    login = input(return_command(INSERT_YA_LOGIN))
    pwd = input(return_command(INSERT_YA_PWD))
    return login, pwd


def get_token_by_credentials(login: str, pwd: str):
    token = Client().generate_token_by_username_and_password(login, pwd)
    if token == 'None':
        return ''
    return token


def write_token_to_cache(token: str):
    cache[YANDEX_TOKEN] = token


def save_token(token: str):
    configurer[YANDEX_BLOCK] = {YANDEX_TOKEN: token}
    write_credentials(configurer)
