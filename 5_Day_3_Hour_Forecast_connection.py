'''
Connects to the OpenWeather "5 Day / 3 Hour Forecast" API, retrieves the 5-day weather forecast in 3-hour intervals for a specified location, and stores into a Pandas DataFrame.
'''

import requests
import pandas as pd
from datetime import datetime
import pytz

# The variable 'key' is the API keys you obtain after registering at https://openweathermap.org
key = ''
units = 'metric'  # default 'standard'
'''
The parameters 'lat' and 'lon' should correspond to the location coordinates you want to obtain weather information.
These could be enter directly or retrieved from the Geocoding API.
The significant figures are accurate up to four decimal places.
The sample code utilizes New York City as an example.
'''
lat = 40.7127
lon = -74.0060
timezone = 'GMT-4'


url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&units={units}&timezone={timezone}'
response = requests.get(url)
print(f'Status: {response.status_code}')
data_5day = response.json()


'''
The timestamp of the raw data is Greenwich Mean Time (GMT).
To convert it back to the correct time, a conversion is required.
'''
target_timezone = pytz.timezone('America/New_York')
lst = []

for i in range(40):  # The raw data comprises 40 records
    dt = data_5day['list'][i]['dt']
    dt = datetime.fromtimestamp(dt)
    dt = dt.astimezone(target_timezone).strftime('%Y-%m-%d %H:%M:%S')
    lst.append(dt)

df_weather_5day = pd.DataFrame({'date_time': lst})  # Create Pandas DataFrame

# Put 'temp', 'feels_like', 'temp_min', and 'temp_max' into DataFrame
for item_temp in ['temp', 'feels_like', 'temp_min', 'temp_max']:
    new_col = {item_temp: [data_5day['list'][i]
                           ['main'][item_temp] for i in range(40)]}
    df_weather_5day[item_temp] = pd.DataFrame(new_col)

# Put 'main' and 'description' into DataFrame
for item_other in ['main', 'description']:
    new_col = {item_other: [data_5day['list'][i]
                            ['weather'][0][item_other] for i in range(40)]}
    df_weather_5day[item_other] = pd.DataFrame(new_col)

df_weather_5day = df_weather_5day.rename(columns={'main': 'weather_condition'})
print(df_weather_5day.head())
