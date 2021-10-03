import pyttsx3
import platform
from voice_assistant.bin.service.config_service import read_app_config
from voice_assistant.bin.initialize.cache import cache
from voice_assistant.bin.util.constants import SYSTEM_PARAMS_PROP_NAME

MACOS_RUSSIAN_FEMALE_VOICE = 'com.apple.speech.synthesis.voice.milena.premium'
MACOS_ENGLISH_FEMALE_VOICE = 'com.apple.speech.synthesis.voice.samantha'
WIN_ENGLISH_FEMALE_VOICE = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
WIN_RUSSIAN_FEMALE_VOICE = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'


def app_initialize():
    app_config = read_app_config()
    language = app_config.get('Global', 'app.language')

    os = platform.system()

    voice = None
    if os == 'Windows':
        voice = WIN_RUSSIAN_FEMALE_VOICE if language == 'ru' else WIN_ENGLISH_FEMALE_VOICE
    elif os == 'Darwin':
        voice = MACOS_RUSSIAN_FEMALE_VOICE if language == 'ru' else MACOS_ENGLISH_FEMALE_VOICE

    tts_engine = pyttsx3.init()
    tts_engine.setProperty('voice', voice)

    cache[SYSTEM_PARAMS_PROP_NAME] = Parameters(os, tts_engine, language)


# My first Class - pity to kill it
class Parameters:
    def __init__(self, os, tts_engine, language, dictionary=None):
        self.os = os
        self.tts_engine = tts_engine
        self.language = language
        self.dictionary = dictionary

    def set_dictionary(self, dictionary):
        self.dictionary = dictionary

    def get_dictionary(self):
        return self.dictionary

    def get_language(self):
        return self.language
