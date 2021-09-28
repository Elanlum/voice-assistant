import webbrowser


def go_to_website(website):
    webbrowser.open('http://' + website)


def search_google(search_request):
    webbrowser.open('http://google.com/search?q=' + search_request)
