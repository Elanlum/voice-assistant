from configparser import RawConfigParser, NoSectionError, NoOptionError
from voice_assistant.bin.util.constants import CRED_PROPERTIES, CONFIG_PROPERTIES


def read_credentials():
    config = RawConfigParser()
    config.read(CRED_PROPERTIES)
    return config


def read_app_config():
    config = RawConfigParser()
    config.read(CONFIG_PROPERTIES)
    return config


def write_credentials(config: RawConfigParser):
    with open(CRED_PROPERTIES, 'w') as cred_file:
        config.write(cred_file)


def get_from_cred_file(block: str, option: str):
    config = read_credentials()
    try:
        return config.get(block, option)
    except NoOptionError:
        pass
    except NoSectionError:
        pass
