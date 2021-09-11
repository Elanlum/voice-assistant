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
    user_text = user_text.lower()

    # TODO: get rid of this
    response = ''
    replica = ''

    # TODO: extract to a separate function returning tuple of (request, response)
    for r in replicas.keys():
        replica = r
        if select_request_replica(r) == user_text:
            response = select_response_replica(r)
            break
        else:
            response = select_response_replica(const.NO_REPLICA)

    if replica == const.BYE:
        reply_bye(response, tts_engine)
    if replica == const.PLAY_YANDEX or replica == const.MUSIC_YANDEX or replica == const.TURN_ON_YANDEX:
        reply_music(response, tts_engine)
    if replica == const.WHAT_WEATHER:
        # TODO: extract logic on selecting city to a separate service, ask city until 'forget it' phrase
        reply(select_request_replica(const.SELECT_CITY), tts_engine)
        try:
            user_text_en = translate_ru_en(recognize_voice())
            reply_weather(user_text_en, tts_engine)
        except NotFoundError:
            reply(select_request_replica(const.CITY_NOT_FOUND), tts_engine)
    else:
        reply(response, tts_engine)


def select_request_replica(replica):
    return replicas[replica][0]


def select_response_replica(replica):
    return replicas[replica][1]
