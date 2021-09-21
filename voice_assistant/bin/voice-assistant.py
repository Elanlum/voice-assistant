import speech_recognition as sr
from phrase_handler import handle_phrase
from voice_recognizer import recognize_voice
from initialize.initializer import app_initialize


def main():
    tts_engine = app_initialize()

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
