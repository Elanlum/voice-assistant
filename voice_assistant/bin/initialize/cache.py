from voice_assistant.bin.service.weather import Weather
from voice_assistant.bin.util.constants import YANDEX_TOKEN, WEATHER_CACHE, SYSTEM_PARAMS_PROP_CACHE, WEATHER_APIKEY


cache = {
    YANDEX_TOKEN: '',
    WEATHER_CACHE: Weather(),
    SYSTEM_PARAMS_PROP_CACHE: None,
    WEATHER_APIKEY: ''
}


def get_params_from_cache():
    return cache[SYSTEM_PARAMS_PROP_CACHE]


def get_yandex_token_from_cache():
    return cache[YANDEX_TOKEN]


def get_language_from_cache():
    params = cache[SYSTEM_PARAMS_PROP_CACHE]
    return params.get_language()


def get_weather_from_cache():
    return cache[WEATHER_CACHE]


def is_language_ru():
    return get_language_from_cache() == 'ru'


def is_language_en():
    return get_language_from_cache() == 'en'
