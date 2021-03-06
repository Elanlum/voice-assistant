from pyowm.commons.exceptions import NotFoundError, UnauthorizedError
import re

from voice_assistant.bin.service.voice_recognize_service import recognize_voice
from voice_assistant.bin.service.translator_service import translate_ru_en
from voice_assistant.bin.util import constants as const
from voice_assistant.bin.service.dictionary_service import get_voice_params, get_request, get_response
from voice_assistant.bin.initialize.cache import is_language_ru
from voice_assistant.bin.handle_reply.replier import reply, reply_weather, reply_music, reply_bye, reply_to_browse, \
    reply_search_google, reply_open_file
from voice_assistant.bin.service.auto_commands_resolver import return_command
from voice_assistant.bin.dict.auto_response_dictionary import SELECT_CITY, CITY_NOT_FOUND, WRONG_WEBSITE, \
    INVALID_API_KEY
from voice_assistant.bin.dict.constants import CANCEL

from voice_assistant.bin.objects.voice_parameters import VoiceParams


def handle_phrase(user_text: str):
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


def bye(params: VoiceParams):
    reply_bye(params.response)


def play_yandex(params: VoiceParams):
    reply_music(params.response)


def weather():
    select_city_and_reply()


def browse(params: VoiceParams):
    url_part = extract_request_part(get_request(params.phrase), params.request)
    if re.search(const.CYRILLIC_PATTERN, url_part) or re.match(const.WEBSITE_PATTERN, url_part) is None:
        reply(return_command(WRONG_WEBSITE))
    else:
        reply_to_browse(params.response, url_part)


def search(params: VoiceParams):
    url_part = extract_request_part(get_request(params.phrase), params.request)
    reply_search_google(params.response, url_part)


def open_file(params: VoiceParams):
    file_name_type = extract_request_part(get_request(params.phrase), params.request)
    reply_open_file(params.response, file_name_type)


def base_case(params: VoiceParams):
    reply(params.response)


def select_city_and_reply():
    reply(return_command(SELECT_CITY))

    city_found = False
    while not city_found:
        try:
            user_command = recognize_voice()
            if user_command == get_request(CANCEL):
                reply(get_response(CANCEL))
                return

            user_command = translate_ru_en(user_command) if is_language_ru() else user_command
            reply_weather(user_command)
            city_found = True
        except NotFoundError:
            reply(return_command(CITY_NOT_FOUND))
        except UnauthorizedError:
            reply(return_command(INVALID_API_KEY))


def extract_request_part(key_phrase: str, inp: str):
    url_part = ''
    if key_phrase in inp:
        url_part = inp.replace(key_phrase, '').strip()

    return url_part
