from voice_assistant.bin.dict.constants import BYE, MUSIC_YANDEX, PLAY_YANDEX, TURN_ON_YANDEX, WHAT_WEATHER, CANCEL, \
    HELLO, HOW_ARE_YOU, HOWS_DAY, WHOS_SIRI, BROWSE, SEARCH, OPEN_FILE, WHAT_CAN_YOU, WHO_ARE_YOU, WHATS_YOUR_NAME, \
    WHAT_TIME

YANDEX_RESPONSE = 'Playing Yandex'


# Dictionary consists of phrases with correspondent array of request and response:
# phrase : [request, response]
def dictionary_en():
    return {
        HELLO: ['hello', 'Hello-hello!'],
        BYE: ['bye', 'Bye!'],
        HOW_ARE_YOU: ['how are you', 'I am fine, thanks'],
        HOWS_DAY: ['how is your day', 'It is quite good'],
        WHOS_SIRI: ['who\'s siri', 'I don\'t know that bitch but I don\'t like her'],
        MUSIC_YANDEX: ['music yandex', YANDEX_RESPONSE],
        PLAY_YANDEX: ['play yandex', YANDEX_RESPONSE],
        TURN_ON_YANDEX: ['turn on yandex', YANDEX_RESPONSE],
        WHAT_WEATHER: ['what is the weather', 'The temperature today'],
        CANCEL: ['Cancel', 'Action cancelled'],
        BROWSE: ['browse', 'Browsing'],
        SEARCH: ['search', 'Searching in Google'],
        OPEN_FILE: ['open', 'Opening'],
        WHAT_CAN_YOU: ['what can you do', 'I can do the small talk, turn on music, give a weather forecast, browse in '
                                          'web and more'],
        WHO_ARE_YOU: ['who are you', 'I am Suzy, your voice assistant'],
        WHATS_YOUR_NAME: ['what is your name', 'My name is Suzy, I am your voice assistant'],
        WHAT_TIME: ['what time is it', 'Current time']
    }
