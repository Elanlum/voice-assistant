from pyowm.commons.exceptions import NotFoundError
from voice_assistant.bin.dict.phrase_dictionary_en import dictionary_en
from voice_assistant.bin.dict.phrase_dictionary_ru import dictionary_ru
from voice_assistant.bin.handle_reply.replier import reply, reply_weather, reply_music, reply_bye, reply_to_browse, \
    reply_search_google, reply_open_file
from voice_assistant.bin.service.voice_recognize_service import recognize_voice
from voice_assistant.bin.service.translator_service import translate_ru_en
from voice_assistant.bin.service.config_service import read_app_config
import voice_assistant.bin.util.constants as const
from voice_assistant.bin.service.dictionary_service import get_voice_params, get_request, get_response

# app_config = read_app_config()
# language = app_config.get('Global', 'app.language')
#
# phrases = dictionary_ru() if language == 'ru' else dictionary_en()
# phrases = dict(phrases)


def handle_phrase(user_text, params):
    request = user_text.lower()
    voice_params = get_voice_params(request)

    # if phrase == const.BYE:
    #     reply_bye(response, params)
    # elif phrase == const.PLAY_YANDEX or phrase == const.MUSIC_YANDEX or phrase == const.TURN_ON_YANDEX:
    #     reply_music(response, params)
    # elif phrase == const.WHAT_WEATHER:
    #     select_city_and_reply(params)
    # elif phrase == const.BROWSE:
    #     url_part = extract_request_part(get_request(phrase), request)
    #     reply_to_browse(response, url_part, params)
    # elif phrase == const.SEARCH:
    #     url_part = extract_request_part(get_request(phrase), request)
    #     reply_search_google(response, url_part, params)
    # elif phrase == const.OPEN_FILE:
    #     file_name_type = extract_request_part(get_request(phrase), request)
    #     reply_open_file(response, file_name_type, params)
    # else:
    #     reply(response, params)

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
    func = phrase_handler.get(phrase, lambda x, y: base_case(voice_params, params))
    func(voice_params, params)


def bye(voice_params, params):
    reply_bye(voice_params.response, params)


def play_yandex(voice_params, params):
    reply_music(voice_params.response, params)


def weather(voice_params, params):
    select_city_and_reply(params)


def browse(voice_params, params):
    url_part = extract_request_part(get_request(voice_params.phrase), voice_params.request)
    reply_to_browse(voice_params.response, url_part, params)


def search(voice_params, params):
    url_part = extract_request_part(get_request(voice_params.phrase), voice_params.request)
    reply_search_google(voice_params.response, url_part, params)


def open_file(voice_params, params):
    file_name_type = extract_request_part(get_request(voice_params.phrase), voice_params.request)
    reply_open_file(voice_params.response, file_name_type, params)


def base_case(voice_params, params):
    reply(voice_params.response, params)


def select_city_and_reply(tts_engine):
    reply(get_request(const.SELECT_CITY), tts_engine)

    city_found = False
    while not city_found:
        try:
            user_text = recognize_voice()
            if user_text == get_request(const.CANCEL):
                reply(get_response(const.CANCEL), tts_engine)
                return

            user_text_en = translate_ru_en(user_text)
            reply_weather(user_text_en, tts_engine)
            city_found = True
        except NotFoundError:
            reply(get_response(const.CITY_NOT_FOUND), tts_engine)


def extract_request_part(key_phrase, inp):
    url_part = ''
    if key_phrase in inp:
        url_part = inp.replace(key_phrase, '').strip()

    return url_part
