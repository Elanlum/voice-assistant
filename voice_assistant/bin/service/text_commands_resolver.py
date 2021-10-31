from voice_assistant.bin.dict.auto_response_dictionary import get_ru_response, get_en_response
from voice_assistant.bin.initialize.cache import cache, SYSTEM_PARAMS_PROP_CACHE
from voice_assistant.bin.util.constants import TEXT_KEY


def print_command(command_name, **kwargs):
    params = cache[SYSTEM_PARAMS_PROP_CACHE]
    language = params.get_language()

    value = kwargs.get(TEXT_KEY) or ''

    if language == 'ru':
        print(get_ru_response(command_name), value)
    elif language == 'en':
        print(get_en_response(command_name), value)
    else:
        print('Something\'s wrong')


def return_command(command_name):
    params = cache[SYSTEM_PARAMS_PROP_CACHE]
    language = params.get_language()

    if language == 'ru':
        return get_ru_response(command_name)
    elif language == 'en':
        return get_en_response(command_name)
    else:
        return 'Something\'s wrong'
