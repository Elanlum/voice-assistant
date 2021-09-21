from voice_assistant.bin.service.translator_service import translate_en_ru
from voice_assistant.bin.service.weather_service import get_weather_status, get_avg_temperature
from voice_assistant.bin.service.yandex_player_service import play_yandex_last_favourite_track
from voice_assistant.bin.service.voice_web_search_service import go_to_website, search_google


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


def reply_music(reply_phrase, tts_engine):
    reply(reply_phrase, tts_engine)
    # TODO: playing music causes an extra phrase said by assistant after playing
    play_yandex_last_favourite_track()


def reply_bye(reply_phrase, tts_engine):
    reply(reply_phrase, tts_engine)
    exit()


def reply_to_browse(reply_phrase, web_site, tts_engine):
    reply(reply_phrase, tts_engine)
    go_to_website(web_site)


def reply_search_google(reply_phrase, search_request, tts_engine):
    reply(reply_phrase, tts_engine)
    search_google(search_request)
