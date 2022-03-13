from selenium import webdriver
import time

chrome_driver_path = "/home/dhruvarora/Code/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Cookie element to click on
cookie = driver.find_element_by_id("cookie")

# Upgrade item ids.
price_element = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in price_element]

timeout = time.time() + 5

while True:

    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Prices of upgrades
        price_element = driver.find_elements_by_css_selector("#store b")
        price_element_text = [element.text for element in price_element]
        price_element_text.pop()  # Removing last element because it's empty
        item_prices = [
            int(element.split("-")[1].replace(",", "").strip())
            for element in price_element_text
        ]

        # Dictionary of store items and prices
        cookie_upgrades = {}
        for index in range(len(item_prices)):
            cookie_upgrades[item_prices[index]] = item_ids[index]

        # Current cookie count
        money_text = driver.find_element_by_id("money").text
        if "," in money_text:
            money_text = money_text.replace(",", "").strip()
        cookie_count = int(money_text)

        # Upgrades that can be afforded
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_affordable_upgrade]
        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5
