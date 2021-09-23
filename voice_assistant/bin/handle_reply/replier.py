from voice_assistant.bin.service.translator_service import translate_en_ru
from voice_assistant.bin.service.weather_service import get_weather_status, get_avg_temperature
from voice_assistant.bin.service.yandex_player_service import play_yandex_last_favourite_track
from voice_assistant.bin.service.voice_web_search_service import go_to_website, search_google
from voice_assistant.bin.service.file_service import open_file


def reply(text, params):
    tts_engine = params.tts_engine
    # TODO: Internationalize this
    print('Ассистент:', text)

    tts_engine.say(str(text))
    tts_engine.runAndWait()


# TODO: make this ready for I18n
def reply_weather(city, params):
    city_local_name = translate_en_ru(city)
    temperature = get_avg_temperature(city)
    status = get_weather_status(city)

    reply_list = ['В городе ',
                  city_local_name,
                  ' температура сегодня ',
                  str(temperature),
                  ' градусов, ',
                  status]

    reply(''.join(reply_list), params)


def reply_music(reply_phrase, params):
    reply(reply_phrase, params)
    # TODO: playing music causes an extra phrase said by assistant after playing
    play_yandex_last_favourite_track()


def reply_bye(reply_phrase, params):
    reply(reply_phrase, params)
    exit()


def reply_to_browse(reply_phrase, web_site, params):
    reply(reply_phrase, params)
    go_to_website(web_site)


def reply_search_google(reply_phrase, search_request, params):
    reply(reply_phrase, params)
    search_google(search_request)


def reply_open_file(reply_phrase, file_type_name, params):
    reply(reply_phrase, params)
    open_file(params.os, file_type_name)
