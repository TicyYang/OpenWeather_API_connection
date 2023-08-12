'''
Connects to the OpenWeather "Current weather data" API, retrieves the current weather data for a specified location.
'''

import requests
from datetime import datetime
import pytz

# The variable 'key' is the API keys you obtain after registering at https://openweathermap.org
key = ''
units = 'metric'  # default 'standard'
'''
The variables 'lat' and 'lon' should correspond to the location coordinates you want to obtain weather information.
These could be enter directly or retrieved from the Geocoding API.
The significant figures are accurate up to four decimal places.
The sample code utilizes New York City as an example.
'''
lat = 40.7127
lon = -74.0060


url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units={units}'
response = requests.get(url)
print(f'Status: {response.status_code}')
data_current = response.json()


# Print current time.
dt = data_current['dt']
dt = datetime.fromtimestamp(dt)
'''
The timestamp of the raw data is based on the time zone of the IP.
To convert it back to the correct time, a conversion is required.
'''
target_timezone = pytz.timezone('America/New_York')
dt = dt.astimezone(target_timezone).strftime('%Y-%m-%d %H:%M:%S')
print(dt)


# Print the current weather data including: temp, feels_like, temp_min, temp_max, pressure, humidity
for i in data_current['main']:
    print(str(i) + ': ', data_current['main'][i])
