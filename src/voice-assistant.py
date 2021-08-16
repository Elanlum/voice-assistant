import pyttsx3
import speech_recognition as sr
from yandex_player import play_yandex_last_favourite_track
from weather import get_weather
from replicas_dictionary import dictionary

GOOGLE_RUSSIAN_FEMALE_VOICE = 27
replicas = dictionary()


def user_input():
    print("Скажите что-нибудь >>>")

    # We will transform this function later to get voice
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Mic captured
        audio = voice_recognizer.listen(source)

    voice_text = voice_recognizer.recognize_google(audio, language="ru")

    print("Вы сказали:", voice_text)

    return voice_text


def reply(text):
    print("Ассистент:", text)
    
    tts_engine.say(str(text))
    tts_engine.runAndWait()


def handle_replica(user_text):
    user_text = user_text.lower()

    try:
        replica = replicas[user_text]
        
        if replica == 'Пока!':
            reply(replica)
            exit()
        if replica == 'Играю яндекс':
            reply(replica)
            play_yandex_last_favourite_track()
        if replica == 'Температура сегодня':
            temperature = get_weather()
            reply(replica + ' ' + str(temperature) + ' градусов')

        reply(replica)

    except KeyError:
        reply("Не понимаю Вас")


def main():
    global tts_engine
    tts_engine = pyttsx3.init()

    voices = tts_engine.getProperty("voices")
    tts_engine.setProperty("voice", voices[GOOGLE_RUSSIAN_FEMALE_VOICE].id)

    while True:
        try:
            user_text = user_input()
            handle_replica(user_text)
        except sr.UnknownValueError:
            reply('Вас не слышно')


if __name__ == "__main__":
    main()
