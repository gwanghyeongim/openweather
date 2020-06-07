#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
# https://openweathermap.org/current
APPID = 'Replace me with your APPID'

import json, requests, sys
from pprint import pprint
from datetime import datetime, timedelta

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}'
response = requests.get(url)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print('City not found')
    sys.exit()

# Uncomment to see the raw JSON text:
#pprint(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['weather']
m = weatherData['main']
utcOffset = timedelta(seconds=weatherData['timezone'])
utcTime   = datetime.utcnow()
localTime = utcTime + utcOffset
print('Current weather in %s, %s:' % (location, weatherData['sys']['country']))
print(w[0]['main'], '-', w[0]['description'])
print('Temperature is ' + str(round(m['temp'] - 273.15, 1)) + '°C')
print('Feels like ' + str(round(m['feels_like'] - 273.15, 1)) + '°C')
print('Humidity is ' + str(round(m['humidity'])) + '%')
print(f"Time at {location}: " + localTime.strftime("%B %d, %H:%M"))
