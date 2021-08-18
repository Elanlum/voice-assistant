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

* Better location definition, not based on ip request
* Show current time based on current location
* Show current weather condition based on current location (! Done 08.19.21)
* Create internalization module
* Packaging of the application to something (probably app)
