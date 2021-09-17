from util.constants import BYE, MUSIC_YANDEX, PLAY_YANDEX, TURN_ON_YANDEX, WHAT_WEATHER, NO_PHRASE, SELECT_CITY, \
    CITY_NOT_FOUND, CANCEL, HELLO, HOW_ARE_YOU, HOWS_DAY, WHOS_SIRI


# Dictionary consists of phrases with correspondent array of request and response:
# phrase : [request, response]
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
        NO_PHRASE: ['Не понимаю Вас', 'Не понимаю Вас'],
        SELECT_CITY: ['Какой город интересует', 'Какой город интересует'],
        CITY_NOT_FOUND: ['Город не найден', 'Город не найден, попробуйте снова'],
        CANCEL: ['отмена', 'Действие отменено']
    }
