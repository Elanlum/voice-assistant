from voice_assistant.bin.dict.phrase_dictionary_en import dictionary_en
from voice_assistant.bin.dict.phrase_dictionary_ru import dictionary_ru
from voice_assistant.bin.initialize.cache import cache, SYSTEM_PARAMS_PROP_CACHE
from voice_assistant.bin.service.auto_commands_resolver import return_command
from voice_assistant.bin.dict.auto_response_dictionary import NO_PHRASE
from voice_assistant.bin.objects.voice_parameters import VoiceParams

# Selects dictionary based on language setting, extracts requests and responses from it


def get_voice_params(request: str):
    phrases = put_dictionary_to_cache()

    for phrase in phrases.keys():
        # To accept substrings as commands
        if get_request(phrase) in request:
            response = get_response(phrase)
            return VoiceParams(request, response, phrase)

    return VoiceParams(request, return_command(NO_PHRASE), '')


def get_request(phrase: str):
    phrases = get_dictionary_from_cache()
    return phrases[phrase][0]


def get_response(phrase: str):
    phrases = get_dictionary_from_cache()
    return phrases[phrase][1]


def get_dictionary_from_cache():
    params = cache[SYSTEM_PARAMS_PROP_CACHE]
    phrases = params.get_dictionary()
    return dict(phrases)


def put_dictionary_to_cache():
    params = cache[SYSTEM_PARAMS_PROP_CACHE]
    phrases = dictionary_ru() if params.language == 'ru' else dictionary_en()
    phrases = dict(phrases)
    params.set_dictionary(phrases)
    return phrases
