from pyowm.commons.exceptions import NotFoundError
from replicas_dictionary_ru import dictionary_ru
from replicas_dictionary_en import dictionary_en
from replier import reply, reply_weather, reply_music, reply_bye
from voice_recognizer import recognize_voice
from translator_service import translate_ru_en
from config_service import read_app_config

app_config = read_app_config()
language = app_config.get('Global', 'app.language')

replicas = dictionary_ru() if language == 'ru' else dictionary_en()
replicas = dict(replicas)


def handle_replica(user_text, tts_engine):
    user_text = user_text.lower()

    response = ''
    replica = ''

    for r in replicas.keys():
        replica = r
        if select_request_replica(r) == user_text:
            response = select_response_replica(r)
            break
        else:
            response = select_response_replica('no replica')

    if replica == 'bye':
        reply_bye(response, tts_engine)
    if replica == 'play yandex' or replica == 'music yandex' or replica == 'turn on yandex':
        reply_music(response, tts_engine)
    if replica == 'what is the weather':
        reply(select_request_replica('select city'), tts_engine)
        try:
            user_text_en = translate_ru_en(recognize_voice())
            reply_weather(user_text_en, tts_engine)
        except NotFoundError:
            reply(select_request_replica('city not found'), tts_engine)
    else:
        reply(response, tts_engine)


def select_request_replica(replica):
    return replicas[replica][0]


def select_response_replica(replica):
    return replicas[replica][1]
