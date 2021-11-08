from voice_assistant.bin.initialize.cache import get_weather_from_cache
from voice_assistant.bin.dict.constants import SPEAK, DONT_HEAR, YOU_SAID, ASSISTANT, YOU_SILENT, WEATHER_REPLY, \
    INSERT_YA_LOGIN, INSERT_YA_PWD, INSERT_OPEN_WEATHER_APIKEY, YANDEX_LOGIN_ERROR, INVALID_API_KEY, NO_PHRASE, \
    SELECT_CITY, CITY_NOT_FOUND, WRONG_WEBSITE


def auto_response():
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
        INVALID_API_KEY: ['Введен неверный API Key', 'Invalid API Key provided'],
        NO_PHRASE: ['Не понимаю Вас', 'I don\'t get it'],
        SELECT_CITY: ['Какой город интересует', 'Which city'],
        CITY_NOT_FOUND: ['Город не найден, попробуйте снова', 'City not found, try again'],
        WRONG_WEBSITE: ['Вы неверно назвали сайт', 'Wrong website name']
    }


def get_ru_response(command: str):
    return auto_response()[command][0]


def get_en_response(command: str):
    return auto_response()[command][1]
