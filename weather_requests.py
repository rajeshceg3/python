import requests

city = input('Enter your city : ')
# It is not a best pracice to put apikey in public
# Enter you api key below var to proceed with weather request
apikey = '' 
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,apikey)
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
