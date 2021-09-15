from util.constants import BYE, MUSIC_YANDEX, PLAY_YANDEX, TURN_ON_YANDEX, WHAT_WEATHER, NO_PHRASE, SELECT_CITY, \
    CITY_NOT_FOUND, CANCEL


# Dictionary consists of phrases with correspondent array of request and response:
# phrase : [request, response]
def dictionary_en():
    return {
        'hello': ['hello', 'Hello-hello!'],
        BYE: ['bye', 'Bye!'],
        'how are you': ['how are you', 'I am fine, thanks'],
        'how is your day': ['how is your day', 'It is quite good'],
        'who\'s Siri': ['who\'s siri', 'I don\'t know that bitch but I don\'t like her'],
        MUSIC_YANDEX: ['music yandex', 'Playing Yandex'],
        PLAY_YANDEX: ['play yandex', 'Playing Yandex'],
        TURN_ON_YANDEX: ['turn on yandex', 'Playing Yandex'],
        WHAT_WEATHER: ['what is the weather', 'The temperature today'],
        NO_PHRASE: ['I don\'t get it', 'I don\'t get it'],
        SELECT_CITY: ['Which city', 'Which city'],
        CITY_NOT_FOUND: ['City not found', 'City not found, try again'],
        CANCEL: ['Cancel', 'Action cancelled']
    }
