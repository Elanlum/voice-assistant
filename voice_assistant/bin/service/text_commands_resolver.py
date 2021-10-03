from voice_assistant.bin.dict.text_commands_dictionary import text_commands
from voice_assistant.bin.initialize.cache import cache
from voice_assistant.bin.util.constants import SYSTEM_PARAMS_PROP_NAME


def print_command(command_name):
    params = cache[SYSTEM_PARAMS_PROP_NAME]
    language = params.get_language()

    if language == 'ru':
        print(text_commands()[command_name][0])
    elif language == 'en':
        print(text_commands()[command_name][1])
    else:
        print('Something\'s wrong')
