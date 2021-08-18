from pyowm.owm import OWM
import configparser
from pyowm.utils.config import get_default_config
import location_info

CRED_PROPERTIES = 'cred.properties'
WEATHER_BLOCK = 'OpenWeather'


def get_weather():
    config = configparser.RawConfigParser()
    config.read(CRED_PROPERTIES)

    if config.has_option(WEATHER_BLOCK, 'weather.apikey'):
        api_key = config.get(WEATHER_BLOCK, 'weather.apikey')

    config = get_default_config()
    config['language'] = 'ru'
    owm = OWM(api_key, config)

    mgr = owm.weather_manager()
    location = location_info.get_region_city()
    return mgr.weather_at_place(location).weather


def get_avg_temperature():
    weather_data = get_weather()
    temp_dict_celsius = weather_data.temperature('celsius')
    temp_avg = temp_dict_celsius['temp']
    return round(temp_avg)


def get_weather_status():
    return get_weather().detailed_status
