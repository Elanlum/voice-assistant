import requests


def get_location():
    return requests.get("http://ipinfo.io").json()
