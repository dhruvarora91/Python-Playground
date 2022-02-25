import smtplib
import datetime as dt
import random

SMTP_ADDRESS = ""
EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()

if now.weekday() == 0: # Monday
  
  with open("quotes.txt") as quotes_file:
    all_quotes = quotes_file.readlines()
    quote = random.choices(all_quotes)[0]
    
  with smtplib.SMTP(SMTP_ADDRESS) as connection:
    connection.starttls() 
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
      from_addr=EMAIL, 
      to_addrs=EMAIL, 
      msg=f"Subject:Quote of the Day\n\n{quote}"
    )
