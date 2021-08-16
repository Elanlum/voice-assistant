from pyowm.owm import OWM
import configparser
from pyowm.utils.config import get_default_config
from location import get_location

CRED_PROPERTIES = 'cred.properties'
WEATHER_BLOCK = 'OpenWeather'


def location():
    info = get_location()
    city = info['city']
    country = info['country']
    return city + ', ' + country


def get_weather():
    config = configparser.RawConfigParser()
    config.read(CRED_PROPERTIES)

    if config.has_option(WEATHER_BLOCK, 'weather.apikey'):
        api_key = config.get(WEATHER_BLOCK, 'weather.apikey')

    config = get_default_config()
    config['language'] = 'ru'
    owm = OWM(api_key, config)

    mgr = owm.weather_manager()

    weather_data = mgr.weather_at_place(location()).get_weather

    temp_dict_celsius = weather_data.temperature('celsius')
    temp_avg = temp_dict_celsius['temp']
    return round(temp_avg)
