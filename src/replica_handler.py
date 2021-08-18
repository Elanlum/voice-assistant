from yandex_player import play_yandex_last_favourite_track
import weather_service
from replicas_dictionary import dictionary
import location_info
import translator_service

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
            city = location_info.get_city_name()
            city_local = translator_service.translate(city)
            temperature = weather_service.get_avg_temperature()
            status = weather_service.get_weather_status()
            reply('В городе ' + city_local + ' ' + replica + ' ' + str(temperature) + ' градусов, ' + status, tts_engine)
        else:
            reply(replica, tts_engine)

    except KeyError:
        reply("Не понимаю Вас", tts_engine)
