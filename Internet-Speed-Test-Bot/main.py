from selenium import webdriver
import time

CHROME_DRIVER_PATH = "/home/dhruvarora/Code/chromedriver"


class InternetSpeedTestBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed_from_speedtest(self):
        self.driver.get("https://www.speedtest.net")
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_class_name("download-speed").text)
        self.up = float(self.driver.find_element_by_class_name("upload-speed").text)
        print(f"Download Speed from speedtest.net: {self.down}")
        print(f"Upload Speed from speedtest.net: {self.up}")

    def get_internet_speed_from_fast(self):
        self.driver.get("https://www.fast.com")
        time.sleep(60)
        self.down = float(self.driver.find_element_by_id("speed-value").text)
        show_more_info_element = self.driver.find_element_by_id(
            "show-more-details-link"
        )
        show_more_info_element.click()
        self.up = float(self.driver.find_element_by_id("upload-value").text)
        print(f"Download Speed from fast.com: {self.down}")
        print(f"Upload Speed from fast.com: {self.up}")


bot = InternetSpeedTestBot()
bot.get_internet_speed_from_speedtest()
bot.get_internet_speed_from_fast()
