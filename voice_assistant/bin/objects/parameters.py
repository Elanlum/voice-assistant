import pyttsx3

"""
App parameters object which contains:
- os - operation system name
- tts_engine - initialized Engine object
- language - defined based on config.properties file
- dictionary - defined based on language
"""


class Parameters:
    def __init__(self, os: str, tts_engine: pyttsx3.Engine, language: str, dictionary=None):
        self.os = os
        self.tts_engine = tts_engine
        self.language = language
        self.dictionary = dictionary

    def set_dictionary(self, dictionary: dict):
        self.dictionary = dictionary

    def get_dictionary(self):
        return self.dictionary

    def get_language(self):
        return self.language
