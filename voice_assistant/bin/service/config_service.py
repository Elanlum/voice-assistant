import configparser

CRED_PROPERTIES = '../cred.properties'
CONFIG_PROPERTIES = '../config.properties'
YANDEX_BLOCK = 'Yandex'
TRACK_NAME = 'yandex_track.mp3'
YANDEX_LOGIN = 'yandex.login'
YANDEX_PWD = 'yandex.password'
WEATHER_BLOCK = 'OpenWeather'
WEATHER_APIKEY = 'weather.apikey'

configurer = configparser.RawConfigParser()


def read_credentials():
    configurer.read(CRED_PROPERTIES)
    return configurer


def read_app_config():
    configurer.read(CONFIG_PROPERTIES)
    return configurer
