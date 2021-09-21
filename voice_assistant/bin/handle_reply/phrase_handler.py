from pyowm.commons.exceptions import NotFoundError
from voice_assistant.bin.dict.phrase_dictionary_ru import dictionary_ru
from voice_assistant.bin.dict.phrase_dictionary_en import dictionary_en
from voice_assistant.bin.handle_reply.replier import reply, reply_weather, reply_music, reply_bye, reply_to_browse, \
    reply_search_google
from voice_assistant.bin.service.voice_recognize_service import recognize_voice
from voice_assistant.bin.service.translator_service import translate_ru_en
from voice_assistant.bin.service.config_service import read_app_config
import voice_assistant.bin.util.constants as const

app_config = read_app_config()
language = app_config.get('Global', 'app.language')

phrases = dictionary_ru() if language == 'ru' else dictionary_en()
phrases = dict(phrases)


def handle_phrase(user_text, tts_engine):
    request = user_text.lower()
    (phrase, response) = get_phrase_and_response_tuple(request)

    if phrase == const.BYE:
        reply_bye(response, tts_engine)
    elif phrase == const.PLAY_YANDEX or phrase == const.MUSIC_YANDEX or phrase == const.TURN_ON_YANDEX:
        reply_music(response, tts_engine)
    elif phrase == const.WHAT_WEATHER:
        select_city_and_reply(tts_engine)
    elif phrase == const.BROWSE:
        url_part = extract_url_part(get_request(phrase), request)
        reply_to_browse(response, url_part, tts_engine)
    elif phrase == const.SEARCH:
        url_part = extract_url_part(get_request(phrase), request)
        reply_search_google(response, url_part, tts_engine)
    else:
        reply(response, tts_engine)


def get_request(phrase):
    return phrases[phrase][0]


def get_response(phrase):
    return phrases[phrase][1]


def get_phrase_and_response_tuple(request):
    phrase = None
    response = None

    for phrase in phrases.keys():
        if get_request(phrase) == request or get_request(phrase) in request:
            response = get_response(phrase)
            return phrase, response

        response = get_response(const.NO_PHRASE)
        phrase = ''
    return phrase, response


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


def extract_url_part(key_phrase, inp):
    url_part = ''
    if key_phrase in inp:
        url_part = inp.replace(key_phrase, '').strip()

    return url_part
