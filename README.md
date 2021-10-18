## Python-based voice-assistant. Currently, launches in Terminal, recognizes several phrases in English and Russian.

## Usage of voice assistant features

### Yandex.Music

For early development purpose you have to create `cred.properties` file in root and store your token there

```
[Yandex]
yandex.token = token
```

### OpenWeather

Register or sign in to your account openweathermap.org and copy your ApiKey from your profile into cred.properties file
located in root folder of the project

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
* Add console input for login, password, token input for services and store them in cache (! Done 10.16.21)
* Improve cache storage for tokens (Yandex, OpenWeather)
* Show current time based on current location
* Create a way of stopping music without terminating app (Keyboard listener or input of any key)
* Better location definition, not based on ip request
* Packaging of the application to something (probably app)
* Dockerfile for deploy of project to some cloud
* Create graph structure for replies handling (more flexible dialogue)
* Write tests, check coverage

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