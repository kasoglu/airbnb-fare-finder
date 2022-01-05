from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH"
GOOGLE_FORMS_LINK = "YOUR_GOOGLE_FORMS_LINK"

# Fill the information where would you like to go to trip? Type date as format YYYY-MM-DD
CITY = ""
CHECK_IN_DATE = ""
CHECK_OUT_DATE = ""
MAX_PRICE = 100 # Default currency is USD (United States Dollar)
GUESTS_NUMBER = 1

APARTMENTS_LINK = f"https://www.airbnb.com/s/{CITY}/homes?checkin={CHECK_IN_DATE}&checkout={CHECK_OUT_DATE}" \
                  f"&price_max={MAX_PRICE}&adults={GUESTS_NUMBER}"
print(APARTMENTS_LINK)


class AirBnbFareFinder:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.apartment_titles = []
        self.apartments_prices = []
        self.apartments_links = []
        self.apartments_reviews = []

    def get_apartment_details(self):
        self.driver.get(APARTMENTS_LINK)
        time.sleep(5)

        apartment_names = self.driver.find_elements(By.CLASS_NAME, 't16jmdcf')
        self.apartment_titles = [apartments.text for apartments in apartment_names]
        print(self.apartment_titles)

        apartment_prices = self.driver.find_elements(By.CLASS_NAME, '_tyxjp1')
        self.apartments_prices = [f"{price_per_night.text}" for price_per_night in apartment_prices]
        print(self.apartments_prices)

        apartment_links = self.driver.find_elements(By.CLASS_NAME, 'l1axmu71')
        self.apartments_links = [f"{link.get_attribute('href')}" for link in apartment_links]
        print(self.apartments_links)

        apartment_reviews = self.driver.find_elements(By.CLASS_NAME, 'r1g2zmv6')
        self.apartments_reviews = [f"{review.text}" for review in apartment_reviews]
        print(self.apartments_reviews)

    def submit_apartments(self):
        for n in range(20):
            self.driver.get(GOOGLE_FORMS_LINK)

            time.sleep(2)
            name = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            review = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

            name.send_keys(self.apartment_titles[n])
            price.send_keys(self.apartments_prices[n])
            link.send_keys(self.apartments_links[n])
            review.send_keys(self.apartments_reviews[n])
            submit_button.click()


bot = AirBnbFareFinder()
bot.get_apartment_details()
bot.submit_apartments()
