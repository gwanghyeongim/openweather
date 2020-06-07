# openweather
Get the current weather of a city using OpenWeather API

## Example
Run python getOpenWeather.py CITYNAME

    $ python getOpenWeather.py Oslo
    
The result follows as:

    Current weather in oslo, NO:
    Rain - light rain
    Temperature is 9.9°C
    Feels like 8.2°C
    Humidity is 89%
    Time at oslo: June 07, 10:44

## Required
- ```$ pip install requests``` in your command line to install requests library.
- Get APPID to use openweather API. [Visit OpenWeather](https://openweathermap.org/) and sign in to get your APPID
- Put your APPID in ```getOpenWeather.py``` at line 4.

This program was inspired by the book *Automate The Boring Stuff With Python* whose author is Al Sweigart
