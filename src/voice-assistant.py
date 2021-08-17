import pyttsx3
import speech_recognition as sr
import replica_handler

GOOGLE_RUSSIAN_FEMALE_VOICE = 27


def recognize_voice():
    print("Скажите что-нибудь >>>")

    # We will transform this function later to get voice
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Mic captured
        audio = voice_recognizer.listen(source)

    voice_text = voice_recognizer.recognize_google(audio, language="ru")

    print("Вы сказали:", voice_text)

    return voice_text


def config_tts():
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty("voices")
    tts_engine.setProperty("voice", voices[GOOGLE_RUSSIAN_FEMALE_VOICE].id)
    return tts_engine


def main():
    tts_engine = config_tts()

    while True:
        try:
            user_text = recognize_voice()
            replica_handler.handle_replica(user_text, tts_engine)
        except sr.UnknownValueError:
            replica_handler.reply('Вас не слышно', tts_engine)


if __name__ == "__main__":
    main()
