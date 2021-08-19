from replicas_dictionary import dictionary
from replier import reply, reply_weather, reply_music, reply_bye

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
            reply_weather(tts_engine)
        else:
            reply(replica, tts_engine)

    except KeyError:
        reply("Не понимаю Вас", tts_engine)
