from voice_assistant.bin.service.translator_service import translate_en_ru
from voice_assistant.bin.service.weather_service import get_weather_status, get_avg_temperature
from voice_assistant.bin.service.yandex_player_service import play_yandex_last_favourite_track
from voice_assistant.bin.service.voice_web_search_service import go_to_website, search_google
from voice_assistant.bin.service.file_service import open_file
from voice_assistant.bin.initialize.cache import get_params_from_cache, is_language_ru, get_weather_from_cache
from voice_assistant.bin.service.auto_commands_resolver import print_command
from voice_assistant.bin.dict.auto_response_dictionary import ASSISTANT, WEATHER_REPLY, get_en_response, get_ru_response


def reply(text: str):
    params = get_params_from_cache()
    tts_engine = params.tts_engine
    print_command(ASSISTANT, text_key=text)

    tts_engine.say(str(text))
    tts_engine.runAndWait()


def reply_weather(city: str):
    weather = get_weather_from_cache()

    weather.set_target_city(translate_en_ru(city) if is_language_ru() else city)
    weather.set_temperature(get_avg_temperature(city))
    weather.set_status(get_weather_status(city))

    reply(get_ru_response(WEATHER_REPLY)) if is_language_ru() else reply(get_en_response(WEATHER_REPLY))


def reply_music(reply_phrase: str):
    reply(reply_phrase)
    # TODO: playing music causes an extra phrase said by assistant after playing
    play_yandex_last_favourite_track()


def reply_bye(reply_phrase: str):
    reply(reply_phrase)
    exit()


def reply_to_browse(reply_phrase: str, web_site: str):
    reply(reply_phrase)
    go_to_website(web_site)


def reply_search_google(reply_phrase: str, search_request: str):
    reply(reply_phrase)
    search_google(search_request)


def reply_open_file(reply_phrase: str, file_type_name: str):
    reply(reply_phrase)
    params = get_params_from_cache()
    open_file(params.os, file_type_name)
