from playsound import playsound
import pyttsx3
import speech_recognition as sr
import os
import sys

google_russian_female_voice = 27

replicas = {
        'привет': 'Привет-привет!',
        'пока': 'Песня для вас, раз такое дело',
        'как дела': 'Город засыпает, мафия просыпается',
        'как здоровье': 'Все нормас'
    }


def user_input():
    print("Скажите что-нибудь >>>")

    # We will transform this function later to get voice
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Mic captured
        audio = voice_recognizer.listen(source)

    # Mic released

    voice_text = voice_recognizer.recognize_google(audio, language="ru")

    print("Вы сказали:", voice_text)

    return voice_text


def reply(text):
    print("Ассистент:", text)
    
    ttsEngine.say(str(text))
    ttsEngine.runAndWait()


def handle_command(user_text):
    user_text = user_text.lower()

    try:
        replica = replicas[user_text]
        reply(replica)
        
        if replica == 'Песня для вас, раз такое дело':
            playsound(sys.path[0] + '/../zveri.mp3')
            exit()

    except KeyError:
        reply("Не понимаю Вас")


def start():
    while True:
        try:
            user_text = user_input()
            handle_command(user_text)
        except sr.UnknownValueError:
            reply('Вас не слышно')

if __name__ == "__main__":

    ttsEngine = pyttsx3.init()
    voices = ttsEngine.getProperty("voices")
    ttsEngine.setProperty("voice", voices[google_russian_female_voice].id)

    start()
