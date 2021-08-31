from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import location_info
import cred_config_service as conf

cred_config = conf.read_credentials()
app_config = conf.read_app_config()
weather_block = conf.WEATHER_BLOCK
api_key_prop = conf.WEATHER_APIKEY


def config_owm():
    if cred_config.has_option(weather_block, api_key_prop):
        api_key = cred_config.get(weather_block, api_key_prop)

    owm_config = get_default_config()
    owm_config['language'] = app_config.get('Global', 'app.language')
    return OWM(api_key, owm_config)


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
    temperature_type = app_config.get('Global', 'weather.temperature.type')
    temperature_info = weather_info.temperature(temperature_type)
    temp_avg = temperature_info['temp']
    return round(temp_avg)


def get_weather_status(city):
    return get_weather_info(city).detailed_status
