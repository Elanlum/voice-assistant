import pyttsx3
import speech_recognition as sr
import replica_handler
import voice_recognizer

GOOGLE_RUSSIAN_FEMALE_VOICE = 27


def config_tts():
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty("voices")
    tts_engine.setProperty("voice", voices[GOOGLE_RUSSIAN_FEMALE_VOICE].id)
    return tts_engine


def main():
    tts_engine = config_tts()

    while True:
        try:
            user_text = voice_recognizer.recognize_voice()
            replica_handler.handle_replica(user_text, tts_engine)
        except sr.UnknownValueError:
            replica_handler.reply('Вас не слышно', tts_engine)


if __name__ == "__main__":
    main()
