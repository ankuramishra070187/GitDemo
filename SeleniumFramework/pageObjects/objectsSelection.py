from selenium.webdriver.common.by import By

from pageObjects.cehckoutPage import Checkout


class ObjectSelection:

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # cards = self.driver.find_elements_by_css_selector(".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.XPATH, "//*[contains(@class,'btn-primary')]")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*ObjectSelection.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*ObjectSelection.cardFooter)

    def gotoCheckout(self):
        self.driver.find_element(*ObjectSelection.checkout).click()
        checkout = Checkout(self.driver)
        return checkout
