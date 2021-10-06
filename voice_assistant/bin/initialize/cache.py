from voice_assistant.bin.util.constants import SYSTEM_PARAMS_PROP_NAME

cache = {}


def get_params_from_cache():
    return cache[SYSTEM_PARAMS_PROP_NAME]


def get_language_from_cache():
    params = cache[SYSTEM_PARAMS_PROP_NAME]
    return params.get_language()
