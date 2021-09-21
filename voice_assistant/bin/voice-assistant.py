import pyttsx3
import speech_recognition as sr
from phrase_handler import handle_phrase
from voice_recognizer import recognize_voice
from initialize.initializer import app_initialize


def config_tts():
    tts_engine = pyttsx3.init()
    params = app_initialize()
    tts_engine.setProperty('voice', params.voice)
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
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            # TODO: Internationalize this
            print('Не могу разобрать ваше молчание')


if __name__ == '__main__':
    main()
