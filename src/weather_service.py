from pyowm.owm import OWM
import configparser
from pyowm.utils.config import get_default_config
import location_info

CRED_PROPERTIES = 'cred.properties'
WEATHER_BLOCK = 'OpenWeather'


def config_owm():
    config = configparser.RawConfigParser()
    config.read(CRED_PROPERTIES)

    if config.has_option(WEATHER_BLOCK, 'weather.apikey'):
        api_key = config.get(WEATHER_BLOCK, 'weather.apikey')

    config = get_default_config()
    config['language'] = 'ru'
    return OWM(api_key, config)


def get_weather_info(city):
    owm = config_owm()
    mgr = owm.weather_manager()
    return mgr.weather_at_place(city + ', RU').weather


def get_weather_local_info():
    owm = config_owm()
    mgr = owm.weather_manager()
    location = location_info.get_region_city()
    return mgr.weather_at_place(location).weather


def get_avg_temperature(city):
    weather_info = get_weather_info(city)
    temp_dict_celsius = weather_info.temperature('celsius')
    temp_avg = temp_dict_celsius['temp']
    return round(temp_avg)


def get_weather_status(city):
    return get_weather_info(city).detailed_status
