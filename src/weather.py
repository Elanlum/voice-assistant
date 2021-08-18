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
    weather_data = mgr.weather_at_place(location).weather

    temp_dict_celsius = weather_data.temperature('celsius')
    temp_avg = temp_dict_celsius['temp']
    return round(temp_avg)
