from selenium.webdriver.common.by import By

from pageObjects.confirmationPage import Confirmation


class Checkout:

    items = (By.CSS_SELECTOR, "h4")
    prices = (By.CSS_SELECTOR, "tbody tr td[class*='text-center']")
    button = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def Items(self):
        return self.driver.find_elements(*Checkout.items)

    def getPrices(self):
        return self.driver.find_elements(*Checkout.prices)

    def confirmCheckout(self):
        self.driver.find_element(*Checkout.button).click()
        confirmation = Confirmation(self.driver)
        return confirmation
