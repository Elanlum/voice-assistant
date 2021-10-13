from voice_assistant.bin.dict.text_commands_dictionary import text_commands
from voice_assistant.bin.initialize.cache import cache, SYSTEM_PARAMS_PROP_CACHE
from voice_assistant.bin.util.constants import TEXT_KEY


def print_command(command_name, **kwargs):
    params = cache[SYSTEM_PARAMS_PROP_CACHE]
    language = params.get_language()

    value = kwargs.get(TEXT_KEY) or ''

    if language == 'ru':
        print(text_commands()[command_name][0], value)
    elif language == 'en':
        print(text_commands()[command_name][1], value)
    else:
        print('Something\'s wrong')
