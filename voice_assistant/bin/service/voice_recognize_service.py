import speech_recognition as sr
from voice_assistant.bin.service.config_service import read_app_config
from voice_assistant.bin.service.auto_commands_resolver import print_command
from voice_assistant.bin.dict.auto_response_dictionary import SPEAK, YOU_SAID


app_config = read_app_config()
phrase_time_limit = app_config.get('Global', 'phrase.time.limit')
language = app_config.get('Global', 'app.language')


def recognize_voice():
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        print_command(SPEAK)
        audio = voice_recognizer.listen(source, None, int(phrase_time_limit))

    voice_text = voice_recognizer.recognize_google(audio, language=language)

    print_command(YOU_SAID, text_key=voice_text)

    return voice_text
