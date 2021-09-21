import speech_recognition as sr
from voice_assistant.bin.handle_reply.phrase_handler import handle_phrase
from voice_assistant.bin.service.voice_recognize_service import recognize_voice
from initialize.initializer import app_initialize


def main():
    params = app_initialize()

    while True:
        try:
            user_text = recognize_voice()
            handle_phrase(user_text, params.tts_engine)
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
