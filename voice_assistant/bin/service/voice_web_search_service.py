import webbrowser


def go_to_website(website):
    # TODO: add validation on website name (non-cyrillic at least)
    webbrowser.open('http://' + website)


def search_google(search_request):
    webbrowser.open('http://google.com/search?q=' + search_request)
