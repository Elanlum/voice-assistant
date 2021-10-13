WEATHER_CACHE = 'weather_cache_key'
SYSTEM_PARAMS_PROP_CACHE = 'system_params_cache'

cache = {}


def get_params_from_cache():
    return cache[SYSTEM_PARAMS_PROP_CACHE]


def get_language_from_cache():
    params = cache[SYSTEM_PARAMS_PROP_CACHE]
    return params.get_language()


def get_weather_from_cache():
    return cache[WEATHER_CACHE]


def is_language_ru():
    return get_language_from_cache() == 'ru'


def is_language_en():
    return get_language_from_cache() == 'en'
