from voice_assistant.bin.service.config_service import read_app_config
from voice_assistant.bin.dict.phrase_dictionary_en import dictionary_en
from voice_assistant.bin.dict.phrase_dictionary_ru import dictionary_ru
import voice_assistant.bin.util.constants as const

# Selects dictionary based on language setting, extracts requests and responses from it

# TODO: avoid second read from config, use initializer object
app_config = read_app_config()
language = app_config.get('Global', 'app.language')

phrases = dictionary_ru() if language == 'ru' else dictionary_en()
phrases = dict(phrases)


def get_voice_params(request):

    for phrase in phrases.keys():
        # To accept substrings as commands
        if get_request(phrase) in request:
            response = get_response(phrase)
            return VoiceParams(request, response, phrase)

    return VoiceParams(request, get_response(const.NO_PHRASE), '')


def get_request(phrase):
    return phrases[phrase][0]


def get_response(phrase):
    return phrases[phrase][1]


class VoiceParams:
    def __init__(self, request, response, phrase):
        self.request = request
        self.response = response
        self.phrase = phrase
