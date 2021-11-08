"""
Voice parameters object which contains:
- request as an input string
- response as a result string
- phrase as the name of that pair in dictionary

phrase : [request, response]
"""


class VoiceParams:
    def __init__(self, request: str, response: str, phrase: str):
        self.request = request
        self.response = response
        self.phrase = phrase
