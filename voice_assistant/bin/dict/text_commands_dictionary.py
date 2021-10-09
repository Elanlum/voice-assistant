from voice_assistant.bin.initialize.cache import cache, get_weather_from_cache
from voice_assistant.bin.util.constants import WEATHER
from voice_assistant.bin.service.weather_service import Weather

SPEAK = 'speak'
DONT_HEAR = 'cant hear you'
YOU_SAID = 'you\'ve said'
ASSISTANT = 'assistant'
YOU_SILENT = 'you\'re silent'
WEATHER_REPLY = 'weather'

cache[WEATHER] = Weather()


# TODO: technically it's not text commands dictionary anymore. Need fix/rename
def text_commands():
    return {
        SPEAK: ['Говорите, пожалуйста >>>', 'Speak, please >>>'],
        DONT_HEAR: ['Вас не слышно', 'Can\'t hear you'],
        YOU_SAID: ['Вы сказали:', 'You have said:'],
        ASSISTANT: ['Ассистент:', 'Assistant:'],
        YOU_SILENT: ['Кажется, вы молчите', 'Seems like you too silent'],
        WEATHER_REPLY: [f'В городе {get_weather_from_cache().target_city} '
                        f'температура сегодня {get_weather_from_cache().temperature} градусов, '
                        f'{get_weather_from_cache().status}',
                        f'The weather in {get_weather_from_cache().target_city} '
                        f'city today is {get_weather_from_cache().temperature} degrees, '
                        f'{get_weather_from_cache().status}']
    }


def get_ru_response(command):
    return text_commands()[command][0]


def get_en_response(command):
    return text_commands()[command][1]
