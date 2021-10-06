from voice_assistant.bin.service.translator_service import translate_en_ru
from voice_assistant.bin.service.weather_service import get_weather_status, get_avg_temperature
from voice_assistant.bin.service.yandex_player_service import play_yandex_last_favourite_track
from voice_assistant.bin.service.voice_web_search_service import go_to_website, search_google
from voice_assistant.bin.service.file_service import open_file
from voice_assistant.bin.initialize.cache import cache, get_params_from_cache, get_language_from_cache
from voice_assistant.bin.service.text_commands_resolver import print_command
from voice_assistant.bin.dict.text_commands_dictionary import ASSISTANT, WEATHER_REPLY, get_en_response, get_ru_response
from voice_assistant.bin.util.constants import CITY_LOCAL_NAME, TEMPERATURE, STATUS


def reply(text):
    params = get_params_from_cache()
    tts_engine = params.tts_engine
    print_command(ASSISTANT, text_key=text)

    tts_engine.say(str(text))
    tts_engine.runAndWait()


# TODO: fix translating city and conditions
def reply_weather(city):
    city_local_name = translate_en_ru(city)
    temperature = get_avg_temperature(city_local_name)
    status = get_weather_status(city)
    cache[CITY_LOCAL_NAME] = city
    cache[TEMPERATURE] = temperature
    cache[STATUS] = status

    language = get_language_from_cache()
    reply(get_ru_response(WEATHER_REPLY)) if language == 'ru' else reply(get_en_response(WEATHER_REPLY))


def reply_music(reply_phrase):
    reply(reply_phrase)
    # TODO: playing music causes an extra phrase said by assistant after playing
    play_yandex_last_favourite_track()


def reply_bye(reply_phrase):
    reply(reply_phrase)
    exit()


def reply_to_browse(reply_phrase, web_site):
    reply(reply_phrase)
    go_to_website(web_site)


def reply_search_google(reply_phrase, search_request):
    reply(reply_phrase)
    search_google(search_request)


def reply_open_file(reply_phrase, file_type_name):
    reply(reply_phrase)
    params = get_params_from_cache()
    open_file(params.os, file_type_name)

