from pyowm.commons.exceptions import NotFoundError
from replicas_dictionary_ru import dictionary_ru
from replicas_dictionary_en import dictionary_en
from replier import reply, reply_weather, reply_music, reply_bye
from voice_recognizer import recognize_voice
from translator_service import translate_ru_en
from config_service import read_app_config
import util.constants as const

app_config = read_app_config()
language = app_config.get('Global', 'app.language')

replicas = dictionary_ru() if language == 'ru' else dictionary_en()
replicas = dict(replicas)


def handle_replica(user_text, tts_engine):
    request = user_text.lower()
    (replica, response) = get_replica_and_response_tuple(request)

    if replica == const.BYE:
        reply_bye(response, tts_engine)
    if replica == const.PLAY_YANDEX or replica == const.MUSIC_YANDEX or replica == const.TURN_ON_YANDEX:
        reply_music(response, tts_engine)
    if replica == const.WHAT_WEATHER:
        select_city_and_reply(tts_engine)
    else:
        reply(response, tts_engine)


def get_request(replica):
    return replicas[replica][0]


def get_response(replica):
    return replicas[replica][1]


def get_replica_and_response_tuple(request):
    replica = None
    response = None

    for replica in replicas.keys():
        if get_request(replica) == request:
            response = get_response(replica)
            return replica, response

        response = get_response(const.NO_REPLICA)
    return replica, response


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
