from util.constants import BYE, MUSIC_YANDEX, PLAY_YANDEX, TURN_ON_YANDEX, WHAT_WEATHER, NO_REPLICA, SELECT_CITY, \
    CITY_NOT_FOUND, CANCEL


def dictionary_ru():
    return {
        'hello': ['привет', 'Привет-привет!'],
        BYE: ['пока', 'Пока!'],
        'how are you': ['как дела', 'Всё хорошо, спасибо'],
        'how is your day': ['как день', 'Хороший денёк'],
        'who\'s Siri': ['кто такая siri', 'Не знаю эту сучку, но она мне не нравится'],
        MUSIC_YANDEX: ['музыка яндекс', 'Играю Яндекс'],
        PLAY_YANDEX: ['играй яндекс', 'Играю Яндекс'],
        TURN_ON_YANDEX: ['включи яндекс', 'Играю Яндекс'],
        WHAT_WEATHER: ['какая погода', 'Температура сегодня'],
        NO_REPLICA: ['Не понимаю Вас', 'Не понимаю Вас'],
        SELECT_CITY: ['Какой город интересует', 'Какой город интересует'],
        CITY_NOT_FOUND: ['Город не найден', 'Город не найден, попробуйте снова'],
        CANCEL: ['отмена', 'Действие отменено']
    }
