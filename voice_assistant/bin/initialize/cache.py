from voice_assistant.bin.util.constants import SYSTEM_PARAMS_PROP_NAME

cache = {}


def get_params_from_cache():
    return cache[SYSTEM_PARAMS_PROP_NAME]


def get_language_from_cache():
    params = cache[SYSTEM_PARAMS_PROP_NAME]
    return params.get_language()


def is_language_ru():
    return get_language_from_cache() == 'ru'


def is_language_en():
    return get_language_from_cache() == 'en'
