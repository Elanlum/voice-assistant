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

Register or sign into your account openweathermap.org and copy your ApiKey from your profile into properties file

```
[OpenWeather]
weather.apikey = apikey
```


### Roadmap:

* Show current weather condition based on current location (! Done 08.19.21)
* Show weather conditions based on second command with city name (! Done 08.20.21)
* Extract all app settings to properties file(! Done 09.01.21)
* Create internalization and at least two dictionaries for commands (! Done 09.09.21)
* Create graph structure for replies handling
* Create a way of stopping music without terminating app
* Show current time based on current location
* Add support of phrases based on selected language and resource bundles
* Better location definition, not based on ip request
* Packaging of the application to something (probably app)

### Developing notes:

To launch project on Mac OS or Windows, you will need to install pyaudio.
For instance, if you are using pip:

Mac OS: 
```
pip install pyaudio
```
Windows:
```
pip install pipwin
pipwin install pyaudio
```