import requests
from datetime import datetime 
import smtplib
import time

MY_LATITUDE = 28.704060
MY_LONGITUDE = 77.102493
SMTP_ADDRESS = ""
EMAIL = ""
PASSWORD = ""
TO_EMAIL = ""
EMAIL_SUBJECT = ""
EMAIL_MESSAGE = ""

def is_iss_overhead():

  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()

  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])
  
  if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
    return True
  return False


def is_night():
  
  paramaters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
  }

  response = requests.get("https://api.sunrise-sunset.org/json", params=paramaters)
  response.raise_for_status()
  data = response.json()
  sunrise = data['results']['sunrise']
  sunset = data['results']['sunset']

  sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
  sunset_hour = int(sunset.split("T")[1].split(":")[0])
  time_now_hour = datetime.now().hour
  
  if time_now_hour >= sunset_hour or time_now_hour <= sunrise_hour:
    return True
  return False


while True:
  time.sleep(60)
  if is_iss_overhead() and is_night():
    
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
      connection.starttls()
      connection.login(user=EMAIL, password=PASSWORD)
      connection.sendmail(
        from_addr=EMAIL, 
        to_addrs=TO_EMAIL, 
        msg=f"Subject:{EMAIL_SUBJECT}\n\n{EMAIL_MESSAGE}"
      )
