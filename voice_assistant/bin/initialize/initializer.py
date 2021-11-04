import pyttsx3
import platform

from voice_assistant.bin.service.config_service import read_app_config
from voice_assistant.bin.initialize.cache import cache, SYSTEM_PARAMS_PROP_CACHE
from voice_assistant.bin.util.constants import WIN_RUSSIAN_FEMALE_VOICE, WIN_ENGLISH_FEMALE_VOICE, \
    MACOS_RUSSIAN_FEMALE_VOICE, MACOS_ENGLISH_FEMALE_VOICE
from voice_assistant.bin.objects.parameters import Parameters


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

    cache[SYSTEM_PARAMS_PROP_CACHE] = Parameters(os, tts_engine, language)
