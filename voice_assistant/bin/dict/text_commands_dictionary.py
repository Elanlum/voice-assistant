SPEAK = 'speak'
DONT_HEAR = 'cant hear you'
YOU_SAID = 'you\'ve said'
ASSISTANT = 'assistant'
YOU_SILENT = 'you\'re silent'


def text_commands():
    return {
        SPEAK: ['Говорите, пожалуйста >>>', 'Speak, please >>>'],
        DONT_HEAR: ['Вас не слышно', 'Can\'t hear you'],
        YOU_SAID: ['Вы сказали:', 'You have said'],
        ASSISTANT: ['Ассистент:', 'Assistant:'],
        YOU_SILENT: ['Кажется, вы молчите', 'Seems like you too silent']
    }