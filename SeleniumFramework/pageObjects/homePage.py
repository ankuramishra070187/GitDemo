from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.objectsSelection import ObjectSelection


class HomePage:

    shop = (By.CSS_SELECTOR, "[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    ice_cream = (By.XPATH, "//input[@type='checkbox']")
    gender = (By.ID, "exampleFormControlSelect1")
    # emp_status = (By.NAME, "inlineRadioOptions")
    DOB = (By.NAME, "bday")
    button = (By.CSS_SELECTOR, "input[type='submit']")
    message = (By.XPATH, "//*[contains(@class,'alert-success')]")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        object_selection = ObjectSelection(self.driver)
        return object_selection
        # * is used to give instruction to class that it is to be treated as tuple
        # self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_link_text("Shop"))

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckout(self):
        return self.driver.find_element(*HomePage.ice_cream)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    """ 
        def getEmploymentStatus(self):
        radio = self.driver.find_elements(*HomePage.emp_status)
        return radio
    """

    def getDOB(self):
        return self.driver.find_element(*HomePage.DOB)

    def getButton(self):
        return self.driver.find_element(*HomePage.button)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
