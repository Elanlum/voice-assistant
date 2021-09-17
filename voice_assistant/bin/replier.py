from translator_service import translate_en_ru
from weather_service import get_weather_status, get_avg_temperature
from yandex_player import play_yandex_last_favourite_track


def reply(text, tts_engine):
    # TODO: Internationalize this
    print('Ассистент:', text)

    tts_engine.say(str(text))
    tts_engine.runAndWait()


# TODO: make this ready for I18n
def reply_weather(city, tts_engine):
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


def reply_music(phrase, tts_engine):
    reply(phrase, tts_engine)
    # TODO: playing music causes an extra phrase said by assistant after playing
    play_yandex_last_favourite_track()


def reply_bye(phrase, tts_engine):
    reply(phrase, tts_engine)
    exit()
