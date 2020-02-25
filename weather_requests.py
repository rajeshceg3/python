import requests

city = input('Enter your city : ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ade6ca51701b480b4ff90740e6d14611&units=metric'.format(city)
response = requests.get(url)
data = response.json()

temp = data['main']['temp']
wnd_spd = data['wind']['speed']
lat = data['coord']['lat']
long = data['coord']['lon']
desc = data['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wnd_spd))
print('Latitude : {}'.format(lat))
print('Longitude : {}'.format(long))
print('Description : {}'.format(desc))
