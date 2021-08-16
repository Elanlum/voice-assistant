import requests

IP_SERVER_ADDRESS = "http://ipinfo.io"

def get_location():
    return requests.get(IP_SERVER_ADDRESS).json()
