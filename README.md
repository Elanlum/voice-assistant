## Python-based voice-assistant. Currently, launches in Terminal, recognizes several phrases in English and Russian.

## Usage of voice assistant features

### Yandex.Music

For early development purpose you have to create `cred.properties` file and store

```
[Yandex]
yandex.login = login
yandex.password = pass
```

### OpenWeather

Register or sign in to your account openweathermap.org and copy your ApiKey from your profile into properties file

```
[OpenWeather]
weather.apikey = apikey
```


### Roadmap:

* Show current weather condition based on current location (! Done 08.19.21)
* Show weather conditions based on second command with city name (! Done 08.20.21)
* Extract all app settings to properties file(! Done 09.01.21)
* Create internalization and at least two dictionaries for commands (! Done 09.09.21)
* Added voice-controlled web browsing and Google search (! Done 09.20.21)
* Windows and macOS support for selecting voice for tts (! Done 09.23.21)
* Added voice-controlled file opening (! Done 09.24.21)
* Add support of phrases based on selected language and resource bundles (! Done 10.07.21)
* Improve cache storage for tokens (Yandex, OpenWeather)
* Show current time based on current location
* Add console input for login, password, token input for services and store them in cache
* Create a way of stopping music without terminating app
* Better location definition, not based on ip request
* Packaging of the application to something (probably app)
* Create graph structure for replies handling

### Developing notes:

To launch project on macOS or Windows, you will need to install pyaudio.
For instance, if you are using pip:

macOS: 
```
pip install pyaudio
```
Windows:
```
pip install pipwin
pipwin install pyaudio
```
or
```
conda install pyaudio
```

googletrans lib 4.0.0 required

```
pip install googletrans==4.0.0-rc1
```