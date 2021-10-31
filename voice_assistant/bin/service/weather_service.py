from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

from voice_assistant.bin.initialize.cache import cache
from voice_assistant.bin.service import location_info_service
from voice_assistant.bin.service.config_service import write_credentials, get_from_cred_file, read_credentials, \
    read_app_config, WEATHER_APIKEY, WEATHER_BLOCK
from voice_assistant.bin.initialize.cache import get_params_from_cache
from voice_assistant.bin.service.text_commands_resolver import print_command, return_command
from voice_assistant.bin.dict.auto_response_dictionary import INSERT_OPEN_WEATHER_APIKEY, INVALID_API_KEY

cred_config = read_credentials()
app_config = read_app_config()


# TODO: rework usage of configs here, they should be in cache already (see if reading on fly works)
def config_weather_manager():
    apikey = get_from_cred_file(WEATHER_BLOCK, WEATHER_APIKEY)

    if not apikey or apikey is None:
        apikey = input(return_command(INSERT_OPEN_WEATHER_APIKEY))
        write_apikey_to_cache(apikey)
        # TODO: do not save invalid API Key
        save_apikey(apikey)

    owm_config = get_default_config()
    params = get_params_from_cache()
    params.get_language()
    owm_config['language'] = params.get_language()
    owm = OWM(apikey, owm_config)
    return owm.weather_manager()


def get_weather_info(city):
    mgr = config_weather_manager()
    return mgr.weather_at_place(city + ', RU').weather


def get_weather_local_info():
    mgr = config_weather_manager()
    location = location_info_service.get_region_city()
    return mgr.weather_at_place(location).weather


def get_avg_temperature(city):
    weather_info = get_weather_info(city)
    temperature_type = app_config.get('Global', 'weather.temperature.type')
    temperature_info = weather_info.temperature(temperature_type)
    temp_avg = temperature_info['temp']
    return round(temp_avg)


def get_weather_status(city):
    return get_weather_info(city).detailed_status


def save_apikey(apikey):
    cred_config[WEATHER_BLOCK] = {WEATHER_APIKEY: apikey}
    write_credentials(cred_config)


def write_apikey_to_cache(apikey):
    cache[WEATHER_APIKEY] = apikey
