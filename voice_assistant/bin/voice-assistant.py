import pyttsx3
import speech_recognition as sr
from phrase_handler import handle_phrase
from replier import reply
from voice_recognizer import recognize_voice
from config_service import read_app_config

RUSSIAN_FEMALE_VOICE = 'com.apple.speech.synthesis.voice.milena.premium'
ENGLISH_FEMALE_VOICE = 'com.apple.speech.synthesis.voice.samantha'

app_config = read_app_config()
language = app_config.get('Global', 'app.language')


def config_tts():
    tts_engine = pyttsx3.init()
    voice = RUSSIAN_FEMALE_VOICE if language == 'ru' else ENGLISH_FEMALE_VOICE
    tts_engine.setProperty('voice', voice)
    return tts_engine


def main():
    tts_engine = config_tts()

    while True:
        try:
            user_text = recognize_voice()
            handle_phrase(user_text, tts_engine)
        except sr.UnknownValueError:
            # TODO: Internationalize this
            print('Вас не слышно')
            # reply('Вас не слышно', tts_engine)


if __name__ == '__main__':
    main()
