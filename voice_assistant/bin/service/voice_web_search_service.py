import webbrowser


def go_to_website(website: str):
    webbrowser.open('http://' + website)


def search_google(search_request: str):
    webbrowser.open('http://google.com/search?q=' + search_request)
