import speech_recognition as sr


def recognize_voice():
    print('Скажите что-нибудь >>>')

    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Mic captured
        audio = voice_recognizer.listen(source)

    voice_text = voice_recognizer.recognize_google(audio, language='ru')

    print('Вы сказали:', voice_text)

    return voice_text
