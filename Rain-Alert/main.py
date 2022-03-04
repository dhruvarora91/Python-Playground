import requests
from twilio.rest import Client

ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
FROM_NUMBER = "YOUR_TWILIO_TRIAL_NUMBER"
TO_NUMBER = "YOUR_NUMBER"
API_KEY = "YOUR_API_KEY"
LAT = 28.627562
LONG = 77.278404

parameters = {
  "lat": LAT,
  "lon": LONG,
  "exclude": "current,minutely,daily",
  "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

weather_ids = []

for index in range(12):
  weather_ids.append(data['hourly'][index]['weather'][0]['id'])

for id in weather_ids:
  if id < 700:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
      body="Bring an Umbrella ☂, it's going to rain within 12 hours.",
      from_=FROM_NUMBER,
      to=TO_NUMBER
    )
    print(message.status)
    break