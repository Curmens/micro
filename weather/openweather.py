import requests
from pprint import pprint


city = input('Enter your name of city: ')
api_key = 'Your api key from open weather'

units = 'metric'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}'

res = requests.get(url)
data = res.json()

# print(res)
pprint(data)

weather_stat = data['weather'][0]['description']
wind_speed = data['wind']['speed']
temperature = data['main']['temp']

# Get current weather status, temperature and wind_speed
print(weather_stat, temperature, wind_speed)
