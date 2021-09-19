import webbrowser


def web_search(key_phrase, inp):
    if key_phrase in inp:
        inp = inp.replace(key_phrase, '').strip()
        webbrowser.open('http://' + inp)
