from googletrans import Translator


def translate_en_ru(text):
    translator = Translator()
    result = translator.translate(text, src='en', dest='ru')
    return result.text


def translate_ru_en(text):
    translator = Translator()
    result = translator.translate(text, src='ru', dest='en')
    return result.text
