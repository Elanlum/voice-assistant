import speech_recognition as sr


def recognize_voice():
    print('Скажите что-нибудь >>>')

    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        audio = voice_recognizer.listen(source)

    voice_text = voice_recognizer.recognize_google(audio, language='ru')

    print('Вы сказали:', voice_text)

    return voice_text
