SPEAK = 'speak'
DONT_HEAR = 'cant hear you'
YOU_SAID = 'you\'ve said'


def text_commands():
    return {
        SPEAK: ['Говорите, пожалуйста >>>', 'Speak, please >>>'],
        DONT_HEAR: ['Вас не слышно', 'Can\'t hear you'],
        YOU_SAID: ['Вы сказали:', 'You have said']
    }