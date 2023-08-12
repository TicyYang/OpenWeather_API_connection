import requests

key = ''  # The API keys you obtain after registering at https://openweathermap.org
# city, state, and country can be modified according to your requirements
city = 'New York'
state = 'NY'
country = 'US'

url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={key}'

response = requests.get(url)
print(f'Status: {response.status_code}')
data_geo = response.json()

lat = data_geo[0]['lat']
lon = data_geo[0]['lon']
