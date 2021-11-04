class Parameters:
    def __init__(self, os, tts_engine, language, dictionary=None):
        self.os = os
        self.tts_engine = tts_engine
        self.language = language
        self.dictionary = dictionary

    def set_dictionary(self, dictionary):
        self.dictionary = dictionary

    def get_dictionary(self):
        return self.dictionary

    def get_language(self):
        return self.language
