import configparser

CRED_PROPERTIES = '../cred.properties'
YANDEX_BLOCK = 'Yandex'
TRACK_NAME = 'yandex_track.mp3'

configurer = configparser.RawConfigParser()
configurer.read(CRED_PROPERTIES)