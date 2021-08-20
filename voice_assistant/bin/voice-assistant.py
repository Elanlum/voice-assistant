import pyttsx3
import speech_recognition as sr
from replica_handler import handle_replica
from replier import reply
from voice_recognizer import recognize_voice

GOOGLE_RUSSIAN_FEMALE_VOICE = 27


def config_tts():
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[GOOGLE_RUSSIAN_FEMALE_VOICE].id)
    return tts_engine


def main():
    tts_engine = config_tts()

    while True:
        try:
            user_text = recognize_voice()
            handle_replica(user_text, tts_engine)
        except sr.UnknownValueError:
            reply('Вас не слышно', tts_engine)


if __name__ == '__main__':
    main()
