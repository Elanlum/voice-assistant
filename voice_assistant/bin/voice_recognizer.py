import speech_recognition as sr
from config_service import read_app_config

app_config = read_app_config()
language = app_config.get('Global', 'app.language')
phrase_time_limit = app_config.get('Global', 'phrase.time.limit')


def recognize_voice():
    print('Говорите, пожалуйста >>>')

    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        audio = voice_recognizer.listen(source, None, int(phrase_time_limit))

    voice_text = voice_recognizer.recognize_google(audio, language=language)

    print('Вы сказали:', voice_text)

    return voice_text
