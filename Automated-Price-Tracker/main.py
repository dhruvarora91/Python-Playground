import requests
from bs4 import BeautifulSoup
import smtplib

URL = ""
BUY_PRICE = 3000

SMTP_ADDRESS = ""
EMAIL = ""
PASSWORD = ""
TO_EMAIL = ""
subject = "Price Drop Alert"
message = f"Price for your item dropped below {BUY_PRICE}"


def send_email():
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:{subject}\n\n{message}",
        )


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price_text = soup.find("span", class_="a-price-whole").get_text()

price_numbers_list = []

for char in price_text:
    if char.isdigit():
        price_numbers_list.append(char)

price = int("".join(price_numbers_list))

if price < 3000:
    send_email()
