from voice_assistant.bin.service.config_service import read_app_config
from voice_assistant.bin.dict.phrase_dictionary_en import dictionary_en
from voice_assistant.bin.dict.phrase_dictionary_ru import dictionary_ru
import voice_assistant.bin.util.constants as const
from voice_assistant.bin.initialize.cache import cache

# Selects dictionary based on language setting, extracts requests and responses from it


def get_voice_params(request):
    phrases = put_dictionary_to_cache()

    for phrase in phrases.keys():
        # To accept substrings as commands
        if get_request(phrase) in request:
            response = get_response(phrase)
            return VoiceParams(request, response, phrase)

    return VoiceParams(request, get_response(const.NO_PHRASE), '')


def get_request(phrase):
    phrases = get_dictionary_from_cache()
    return phrases[phrase][0]


def get_response(phrase):
    phrases = get_dictionary_from_cache()
    return phrases[phrase][1]


def get_dictionary_from_cache():
    params = cache[const.SYSTEM_PARAMS_PROP_NAME]
    phrases = params.get_dictionary()
    return dict(phrases)


def put_dictionary_to_cache():
    params = cache[const.SYSTEM_PARAMS_PROP_NAME]
    phrases = dictionary_ru() if params.language == 'ru' else dictionary_en()
    phrases = dict(phrases)
    params.set_dictionary(phrases)
    return phrases


class VoiceParams:
    def __init__(self, request, response, phrase):
        self.request = request
        self.response = response
        self.phrase = phrase
