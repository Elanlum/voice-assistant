from voice_assistant.bin.util.constants import BYE, MUSIC_YANDEX, PLAY_YANDEX, TURN_ON_YANDEX, WHAT_WEATHER, NO_PHRASE, \
    SELECT_CITY, CITY_NOT_FOUND, CANCEL, HELLO, HOW_ARE_YOU, HOWS_DAY, WHOS_SIRI, BROWSE, SEARCH, OPEN_FILE, WHAT_CAN_YOU


# Dictionary consists of phrases with correspondent array of request and response:
# phrase : [request, response]
def dictionary_en():
    return {
        HELLO: ['hello', 'Hello-hello!'],
        BYE: ['bye', 'Bye!'],
        HOW_ARE_YOU: ['how are you', 'I am fine, thanks'],
        HOWS_DAY: ['how is your day', 'It is quite good'],
        WHOS_SIRI: ['who\'s siri', 'I don\'t know that bitch but I don\'t like her'],
        MUSIC_YANDEX: ['music yandex', 'Playing Yandex'],
        PLAY_YANDEX: ['play yandex', 'Playing Yandex'],
        TURN_ON_YANDEX: ['turn on yandex', 'Playing Yandex'],
        WHAT_WEATHER: ['what is the weather', 'The temperature today'],
        NO_PHRASE: ['I don\'t get it', 'I don\'t get it'],
        SELECT_CITY: ['Which city', 'Which city'],
        CITY_NOT_FOUND: ['City not found', 'City not found, try again'],
        CANCEL: ['Cancel', 'Action cancelled'],
        BROWSE: ['browse', 'Browsing'],
        SEARCH: ['search', 'Searching in Google'],
        OPEN_FILE: ['open', 'Opening'],
        WHAT_CAN_YOU: ['what can you do', 'I can do the small talk, turn on music, give a weather forecast, browse in '
                                          'web and more']
    }
