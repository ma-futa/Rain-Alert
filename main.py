import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

os.environ['API_KEY'] = '3681e4be8e9ef7e63b5201d8d1427d45'
os.environ['AUTH_TOKEN'] = '782d9cca218d87250c674b985421d23b'
print(os.getenv('bisquit'))
api_key = os.environ.get("API_KEY") #"3681e4be8e9ef7e63b5201d8d1427d45"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
OWN_ENDPOINT_2 = "https://api.openweathermap.org/data/3.0/onecall"
OWN_ENDPOINT_3 = "https://api.openweathermap.org/data/2.5/onecall"
print(api_key)

account_sid = 'ACed5dcf790f17cf39c1918ffdf5e4ef2d'
auth_token = os.environ.get('AUTH_TOKEN') #'782d9cca218d87250c674b985421d23b'
print(auth_token)

parameters = {
    "lat": 6.695070,
    "lon": -1.615800,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

print('start')
response = requests.get(OWN_ENDPOINT_3, params=parameters)
response.raise_for_status()
hourly_conditions = response.json()['hourly']
print('1')

will_rain = False

for hour in hourly_conditions[:12]:
    weather_states = hour['weather']
    for weather_state in weather_states:
        if int(weather_state['id']) > 700:
            will_rain = True
print(2)
if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token,)#http_client=proxy_client)
    print(2.1)
    message = client.messages.create(body='its gonna rain',from_='+13193673549',to='+233271250546')

    print(message.status)
    print(message.error_message)
print('end')