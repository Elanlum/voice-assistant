from voice_assistant.bin.dict.constants import BYE, MUSIC_YANDEX, PLAY_YANDEX, TURN_ON_YANDEX, WHAT_WEATHER, CANCEL, \
    HELLO, HOW_ARE_YOU, HOWS_DAY, WHOS_SIRI, BROWSE, SEARCH, OPEN_FILE, WHAT_CAN_YOU, WHO_ARE_YOU, WHATS_YOUR_NAME, \
    WHAT_TIME

YANDEX_RESPONSE = 'Играю Яндекс'

"""
Dictionary consists of phrases with correspondent array of request and response:
phrase : [request, response]
"""


def dictionary_ru():
    return {
        HELLO: ['привет', 'Привет-привет!'],
        BYE: ['пока', 'Пока!'],
        HOW_ARE_YOU: ['как дела', 'Всё хорошо, спасибо'],
        HOWS_DAY: ['как день', 'Хороший денёк'],
        WHOS_SIRI: ['кто такая siri', 'Не знаю эту сучку, но она мне не нравится'],
        MUSIC_YANDEX: ['музыка яндекс', YANDEX_RESPONSE],
        PLAY_YANDEX: ['играй яндекс', YANDEX_RESPONSE],
        TURN_ON_YANDEX: ['включи яндекс', YANDEX_RESPONSE],
        WHAT_WEATHER: ['какая погода', 'Температура сегодня'],
        CANCEL: ['отмена', 'Действие отменено'],
        BROWSE: ['перейди на сайт', 'Перехожу на запрошенный сайт'],
        SEARCH: ['ищи в google', 'Ищу в Google'],
        OPEN_FILE: ['открой файл', 'Открываю'],
        WHAT_CAN_YOU: ['что ты умеешь', 'я могу немного поболтать, включить музыку, подсказать погоду, открыть сайт и '
                                        'кое-что другое'],
        WHO_ARE_YOU: ['кто ты', 'Я Сюзи, ваш голосовой ассистент'],
        WHATS_YOUR_NAME: ['как тебя зовут', 'Меня зовут Сюзи, я ваш голосовой ассистент'],
        WHAT_TIME: ['который час', 'Текущее время']
    }
