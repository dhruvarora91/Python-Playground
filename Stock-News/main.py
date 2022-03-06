import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_PRICE_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
FROM_NUMBER = ""
TO_NUMBER = ""


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_PRICE_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(data_list[0]['4. close'])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

price_diff = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if price_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_diff = price_diff / day_before_yesterday_closing_price * 100

if abs(percentage_diff) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()['articles'][:3]
    news_list = [f"Headline: {news['title']} \n\nBrief: {news['description']}" for news in data]
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for news_article in news_list:
        print(news_article)
        message = client.messages.create(
            body=f"{STOCK_NAME}: {up_down}{round(percentage_diff, 2)}% \n{news_article}",
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
        print(message.status)
