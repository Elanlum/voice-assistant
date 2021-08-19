from pyowm.commons.exceptions import NotFoundError
from replicas_dictionary import dictionary
from replier import reply, reply_weather, reply_music, reply_bye
from voice_recognizer import recognize_voice
from translator_service import translate_ru_en

replicas = dictionary()


def handle_replica(user_text, tts_engine):
    user_text = user_text.lower()

    try:
        replica = replicas[user_text]

        if replica == 'Пока!':
            reply_bye(replica, tts_engine)
        if replica == 'Играю яндекс':
            reply_music(replica, tts_engine)
        if replica == 'Температура сегодня':
            reply('Какой город интересует?', tts_engine)
            try:
                user_text = recognize_voice()
                user_text_en = translate_ru_en(user_text)
                reply_weather(user_text_en, tts_engine)
            except NotFoundError:
                reply('Город не найден', tts_engine)
        else:
            reply(replica, tts_engine)

    except KeyError:
        reply("Не понимаю Вас", tts_engine)
