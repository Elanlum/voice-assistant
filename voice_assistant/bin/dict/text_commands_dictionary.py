from voice_assistant.bin.initialize.cache import get_weather_from_cache

SPEAK = 'speak'
DONT_HEAR = 'cant hear you'
YOU_SAID = 'you\'ve said'
ASSISTANT = 'assistant'
YOU_SILENT = 'you\'re silent'
WEATHER_REPLY = 'weather'
INSERT_YA_LOGIN = 'insert Yandex login'
INSERT_YA_PWD = 'insert Yandex password'
YANDEX_LOGIN_ERROR = 'Yandex login error'
INSERT_OPEN_WEATHER_APIKEY = 'insert OpenWeather ApiKey'
INVALID_API_KEY = 'Invalid ApiKey'


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
                        f'{get_weather_from_cache().status}'],
        INSERT_YA_LOGIN: ['Введите логин Yandex: ', 'Type Yandex login: '],
        INSERT_YA_PWD: ['Введите пароль Яндекс: ', 'Type Yandex password: '],
        INSERT_OPEN_WEATHER_APIKEY: ['Введите OpenWeather API Key: ', 'Insert OpenWeather API Key: '],
        YANDEX_LOGIN_ERROR: ['Неверный логин или пароль Яндекс', 'Wrong Yandex login or password'],
        INVALID_API_KEY: ['Введен неверный API Key', 'Invalid API Key provided']
    }


def get_ru_response(command):
    return text_commands()[command][0]


def get_en_response(command):
    return text_commands()[command][1]
