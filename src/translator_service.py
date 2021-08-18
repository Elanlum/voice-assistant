from googletrans import Translator


def translate(text):
    translator = Translator()
    result = translator.translate(text, dest='ru')
    return result.text
