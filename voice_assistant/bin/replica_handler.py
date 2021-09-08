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

    try:
        response = ''
        replica = ''

        for r in replicas.keys():
            replica = r
            value = replicas[r]
            if value[0] == user_text:
                response = value[1]
                break
            else:
                response = replicas['no replica'][1]

        if replica == 'bye':
            reply_bye(response, tts_engine)
        if replica == 'play yandex':
            reply_music(response, tts_engine)
        if replica == 'what is the weather':
            reply(replicas['what city'][0], tts_engine)
            try:
                user_text_en = translate_ru_en(recognize_voice())
                reply_weather(user_text_en, tts_engine)
            except NotFoundError:
                reply(replicas['city not found'][0], tts_engine)
        else:
            reply(response, tts_engine)

    except KeyError:
        reply('Не понимаю Вас', tts_engine)
