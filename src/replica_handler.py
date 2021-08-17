from yandex_player import play_yandex_last_favourite_track
from weather import get_weather
from replicas_dictionary import dictionary

replicas = dictionary()


def reply(text, tts_engine):
    print("Ассистент:", text)

    tts_engine.say(str(text))
    tts_engine.runAndWait()


def handle_replica(user_text, tts_engine):
    user_text = user_text.lower()

    try:
        replica = replicas[user_text]

        if replica == 'Пока!':
            reply(replica, tts_engine)
            exit()
        if replica == 'Играю яндекс':
            reply(replica, tts_engine)
            play_yandex_last_favourite_track()
        if replica == 'Температура сегодня':
            temperature = get_weather()
            reply(replica + ' ' + str(temperature) + ' градусов', tts_engine)
        else:
            reply(replica, tts_engine)

    except KeyError:
        reply("Не понимаю Вас", tts_engine)
