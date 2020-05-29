import pytest
from selenium import webdriver
import time

from pageObjects.cehckoutPage import Checkout
from pageObjects.confirmationPage import Confirmation
from pageObjects.homePage import HomePage
from pageObjects.objectsSelection import ObjectSelection
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        objects = homepage.shopItems()
        cards = objects.getCardTitles()
        log.info("Getting all card titles.")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                objects.getCardFooter()[i].click()

        time.sleep(2)

        checkout_items = objects.gotoCheckout()  # confirm items and transit checkout page

        phones = checkout_items.Items()

        for phone in phones:
            if phone.text == "Blackberry":
                print("Asserted")
                break

        price_info = checkout_items.getPrices()
        for element in price_info:
            log.info(element.text[3:])

        confirm = checkout_items.confirmCheckout()  # confirm checkout and transit to next page

        assert "location" in confirm.getLabels().text
        log.info("Entering country name as 'In' for searching India")
        confirm.getDropdown().send_keys("In")
        self.verifyLinkPresence("India")
        log.info("Selecting country as India")

        # confirm.waitCountry().click()
        self.driver.find_element_by_link_text("India").click()
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", confirm.getCheckbox())
        time.sleep(2)
        assert confirm.getCheckbox().is_enabled()

        self.driver.execute_script("arguments[0].click();", confirm.getSubmitButton())
        time.sleep(1)
        log.info("Text received is: "+confirm.getSuccessMessage().text)

        assert "Success! Thank you" in confirm.getSuccessMessage().text
