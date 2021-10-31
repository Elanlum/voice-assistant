from voice_assistant.bin.util.constants import BYE, MUSIC_YANDEX, PLAY_YANDEX, TURN_ON_YANDEX, WHAT_WEATHER, \
    CANCEL, HELLO, HOW_ARE_YOU, HOWS_DAY, WHOS_SIRI, BROWSE, SEARCH, OPEN_FILE, \
    WHAT_CAN_YOU, WRONG_WEBSITE, WHO_ARE_YOU, WHATS_YOUR_NAME, WHAT_TIME


# Dictionary consists of phrases with correspondent array of request and response:
# phrase : [request, response]
# TODO: remove all auto responses from here, leave only request-response pairs
def dictionary_ru():
    return {
        HELLO: ['привет', 'Привет-привет!'],
        BYE: ['пока', 'Пока!'],
        HOW_ARE_YOU: ['как дела', 'Всё хорошо, спасибо'],
        HOWS_DAY: ['как день', 'Хороший денёк'],
        WHOS_SIRI: ['кто такая siri', 'Не знаю эту сучку, но она мне не нравится'],
        MUSIC_YANDEX: ['музыка яндекс', 'Играю Яндекс'],
        PLAY_YANDEX: ['играй яндекс', 'Играю Яндекс'],
        TURN_ON_YANDEX: ['включи яндекс', 'Играю Яндекс'],
        WHAT_WEATHER: ['какая погода', 'Температура сегодня'],
        CANCEL: ['отмена', 'Действие отменено'],
        BROWSE: ['перейди на сайт', 'Перехожу на запрошенный сайт'],
        SEARCH: ['ищи в google', 'Ищу в Google'],
        OPEN_FILE: ['открой файл', 'Открываю'],
        WHAT_CAN_YOU: ['что ты умеешь', 'я могу немного поболтать, включить музыку, подсказать погоду, открыть сайт и '
                                        'кое-что другое'],
        WRONG_WEBSITE: ['вы неверно назвали сайт', 'вы неверно назвали сайт'],
        WHO_ARE_YOU: ['кто ты', 'Я Сюзи, ваш голосовой ассистент'],
        WHATS_YOUR_NAME: ['как тебя зовут', 'Меня зовут Сюзи, я ваш голосовой ассистент'],
        WHAT_TIME: ['который час', 'Текущее время']
    }
