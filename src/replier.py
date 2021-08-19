from location_info import locate_city
from translator_service import translate_en_ru
from weather_service import get_weather_status, get_avg_temperature
from yandex_player import play_yandex_last_favourite_track


def reply(text, tts_engine):
    print("Ассистент:", text)

    tts_engine.say(str(text))
    tts_engine.runAndWait()


def reply_weather(city, tts_engine):
    # city = locate_city()
    city_local_name = translate_en_ru(city)
    temperature = get_avg_temperature(city)
    status = get_weather_status(city)

    reply_list = ['В городе ',
                  city_local_name,
                  ' температура сегодня ',
                  str(temperature),
                  ' градусов, ',
                  status]

    reply(''.join(reply_list), tts_engine)


def reply_music(replica, tts_engine):
    reply(replica, tts_engine)
    play_yandex_last_favourite_track()


def reply_bye(replica, tts_engine):
    reply(replica, tts_engine)
    exit()
