import pyttsx3
import platform
from voice_assistant.bin.config_service import read_app_config

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

    return Parameters(os, tts_engine)


# My first Class - pity to kill it
class Parameters:
    def __init__(self, os, tts_engine):
        self.os = os
        self.tts_engine = tts_engine
