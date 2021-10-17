from configparser import RawConfigParser, NoSectionError, NoOptionError

CRED_PROPERTIES = '../cred.properties'
CONFIG_PROPERTIES = '../config.properties'
YANDEX_BLOCK = 'Yandex'
TRACK_NAME = 'yandex_track.mp3'
YANDEX_TOKEN = 'yandex.token'
WEATHER_BLOCK = 'OpenWeather'
WEATHER_APIKEY = 'weather.apikey'


def read_credentials():
    config = RawConfigParser()
    config.read(CRED_PROPERTIES)
    return config


def read_app_config():
    config = RawConfigParser()
    config.read(CONFIG_PROPERTIES)
    return config


def write_credentials(config):
    with open(CRED_PROPERTIES, 'w') as cred_file:
        config.write(cred_file)


def get_from_cred_file(block, option):
    config = read_credentials()
    try:
        return config.get(block, option)
    except NoOptionError:
        pass
    except NoSectionError:
        pass
