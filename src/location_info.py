import requests

IP_SERVER_ADDRESS = "http://ipinfo.io"


def get_location():
    return requests.get(IP_SERVER_ADDRESS).json()


def get_region_city():
    info = get_location()
    city = info['city']
    country = info['country']
    return city + ',' + country


def locate_city():
    info = get_location()
    return info['city']
