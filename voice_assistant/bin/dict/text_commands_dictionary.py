from voice_assistant.bin.initialize.cache import cache
from voice_assistant.bin.util.constants import TEMPERATURE, CITY_LOCAL_NAME, STATUS

SPEAK = 'speak'
DONT_HEAR = 'cant hear you'
YOU_SAID = 'you\'ve said'
ASSISTANT = 'assistant'
YOU_SILENT = 'you\'re silent'
WEATHER_REPLY = 'weather'

cache[STATUS] = ''
cache[CITY_LOCAL_NAME] = ''
cache[TEMPERATURE] = ''


# TODO: technically it's not text commands dictionary anymore. Need fix/rename
def text_commands():
    return {
        SPEAK: ['Говорите, пожалуйста >>>', 'Speak, please >>>'],
        DONT_HEAR: ['Вас не слышно', 'Can\'t hear you'],
        YOU_SAID: ['Вы сказали:', 'You have said:'],
        ASSISTANT: ['Ассистент:', 'Assistant:'],
        YOU_SILENT: ['Кажется, вы молчите', 'Seems like you too silent'],
        WEATHER_REPLY: [f'В городе {cache[CITY_LOCAL_NAME]} температура сегодня {cache[TEMPERATURE]} градусов, {cache[STATUS]}',
                        f'The weather in {cache[CITY_LOCAL_NAME]} city today is {cache[TEMPERATURE]} degrees, {cache[STATUS]}']
    }


def get_ru_response(command):
    return text_commands()[command][0]


def get_en_response(command):
    return text_commands()[command][1]
