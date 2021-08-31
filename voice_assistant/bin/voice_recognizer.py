import speech_recognition as sr
from cred_config_service import read_app_config

config = read_app_config()
language = config.get('Global', 'app.language')


def recognize_voice():
    print('Скажите что-нибудь >>>')

    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        audio = voice_recognizer.listen(source)

    voice_text = voice_recognizer.recognize_google(audio, language=language)

    print('Вы сказали:', voice_text)

    return voice_text
