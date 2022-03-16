from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

CHROME_DRIVER_PATH = "/home/dhruvarora/Code/chromedriver"
sel_url = "https://docs.google.com/forms/d/e/1FAIpQLScrWxfIjXWSEF8udRxaLD-wl_rj6cWIX_HxKewvVmHhJON-uQ/viewform?usp=sf_link"
bs_url = "https://www.zillow.com/homes/Toronto,-ON_rb/"


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(bs_url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

addresses = [
    address.getText() for address in soup.find_all("address", class_="list-card-addr")
]

prices = [price.getText() for price in soup.find_all("div", class_="list-card-price")]

links = []

for link_tag in soup.find_all("a", class_="list-card-link"):
    href = link_tag.get("href")
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)


driver = webdriver.Chrome(CHROME_DRIVER_PATH)


for index in range(len(addresses)):
    driver.get(sel_url)
    time.sleep(2)
    address_field = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    price_field = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    link_field = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )

    submit_button = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    )
    time.sleep(2)
    address_field.send_keys(addresses[index])
    price_field.send_keys(prices[index])
    link_field.send_keys(links[index])
    submit_button.click()
