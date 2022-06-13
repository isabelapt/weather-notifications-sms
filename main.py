import requests
import os
from twilio.rest import Client 

print(os.environ)

BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = os.environ.get('API_KEY')
account_sid = 'ACd25909a31ea29aeabd7196ce5212fde9' 
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')


parameters = {
    "lat": -1.455833,
    "lon": -48.503887,
    "appid":API_KEY,
}

response = requests.get(BASE_URL, params = parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

for hour_data in weather_slice:
    weather_condition_codes = int(hour_data['weather'][0]['id']) 
    if weather_condition_codes < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, AUTH_TOKEN)
    message = client.messages.create(
        from_='+18022664701',
        to='+5591982119567',
        body = "Take a Umbrella!",        
        )           

print(message.sid)