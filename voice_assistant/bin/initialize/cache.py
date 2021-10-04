from voice_assistant.bin.util.constants import SYSTEM_PARAMS_PROP_NAME

cache = {}


def get_params_from_cache():
    return cache[SYSTEM_PARAMS_PROP_NAME]