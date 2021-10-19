from pyowm.commons.exceptions import NotFoundError, UnauthorizedError
import re

from voice_assistant.bin.service.voice_recognize_service import recognize_voice
from voice_assistant.bin.service.translator_service import translate_ru_en
from voice_assistant.bin.util import constants as const
from voice_assistant.bin.service.dictionary_service import get_voice_params, get_request, get_response
from voice_assistant.bin.service import dictionary_service as dict
from voice_assistant.bin.initialize.cache import is_language_ru
from voice_assistant.bin.handle_reply.replier import reply, reply_weather, reply_music, reply_bye, reply_to_browse, \
    reply_search_google, reply_open_file
from voice_assistant.bin.service.text_commands_resolver import return_command
from voice_assistant.bin.dict.text_commands_dictionary import INVALID_API_KEY


def handle_phrase(user_text):
    request = user_text.lower()
    voice_params = get_voice_params(request)

    phrase_handler = {
        const.BYE: bye,
        const.PLAY_YANDEX: play_yandex,
        const.MUSIC_YANDEX: play_yandex,
        const.TURN_ON_YANDEX: play_yandex,
        const.WHAT_WEATHER: weather,
        const.BROWSE: browse,
        const.SEARCH: search,
        const.OPEN_FILE: open_file
    }

    phrase = voice_params.phrase
    func = phrase_handler.get(phrase, lambda x: base_case(voice_params))
    func(voice_params)


def bye(voice_params):
    reply_bye(voice_params.response)


def play_yandex(voice_params):
    reply_music(voice_params.response)


def weather(voice_params):
    select_city_and_reply()


def browse(voice_params):
    url_part = extract_request_part(get_request(voice_params.phrase), voice_params.request)
    if re.search(const.CYRILLIC_PATTERN, url_part) or re.match(const.WEBSITE_PATTERN, url_part) is None:
        response = dict.get_response(const.WRONG_WEBSITE)
        reply(response)
    else:
        reply_to_browse(voice_params.response, url_part)


def search(voice_params):
    url_part = extract_request_part(get_request(voice_params.phrase), voice_params.request)
    reply_search_google(voice_params.response, url_part)


def open_file(voice_params):
    file_name_type = extract_request_part(get_request(voice_params.phrase), voice_params.request)
    reply_open_file(voice_params.response, file_name_type)


def base_case(voice_params):
    reply(voice_params.response)


def select_city_and_reply():
    reply(get_request(const.SELECT_CITY))

    city_found = False
    while not city_found:
        try:
            user_command = recognize_voice()
            if user_command == get_request(const.CANCEL):
                reply(get_response(const.CANCEL))
                return

            user_command = translate_ru_en(user_command) if is_language_ru() else user_command
            reply_weather(user_command)
            city_found = True
        except NotFoundError:
            reply(get_response(const.CITY_NOT_FOUND))
        except UnauthorizedError:
            reply(return_command(INVALID_API_KEY))


def extract_request_part(key_phrase, inp):
    url_part = ''
    if key_phrase in inp:
        url_part = inp.replace(key_phrase, '').strip()

    return url_part
