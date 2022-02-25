from datetime import datetime
import pandas
import random
import smtplib

SMTP_ADDRESS = "YOUR_SMTP_ADDRESS"
EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row['month'], row['day']):row for (index, row) in data.iterrows()}

if today in birthdays_dict:
  
  birthday_person = birthdays_dict[today]
  
  with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
    contents = letter_file.read()
    contents = contents.replace('[NAME]', birthday_person['name'])

  with smtplib.SMTP(SMTP_ADDRESS) as connection:
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
      from_addr=EMAIL,
      to_addrs=birthday_person['email'],
      msg=f"Subject:Happy Birthday\n\n{contents}"
    )
