import requests

res = requests.get('https://ipinfo.io/')
data = res.json()
loc = data['loc'].split(',')
city = data['city']
latitude = loc[0]
longitude = loc[1]
# Enter your apikey below
apikey = ''
url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric'.format(latitude, longitude,apikey)
response = requests.get(url)
data = response.json()

temp = data['main']['temp']
wnd_spd = data['wind']['speed']
lat = data['coord']['lat']
long = data['coord']['lon']
desc = data['weather'][0]['description']

print('Your City : {}'.format(city))
print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wnd_spd))
print('Latitude : {}'.format(lat))
print('Longitude : {}'.format(long))
print('Description : {}'.format(desc))
