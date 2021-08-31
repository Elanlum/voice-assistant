## Python-based voice-assistant. Currently launches in Terminal, recognizes several phrases in Russian.

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
* Create a way of stopping music without terminating app
* Show current time based on current location
* Better location definition, not based on ip request
* Packaging of the application to something (probably app)
* Create internalization module and at least two dictionaries for commands
