from selenium.webdriver.common.by import By


class Confirmation:

    labels = (By.CSS_SELECTOR, "label[for='country']")
    dynamic_text = (By.ID, "country")
    # India = (By.LINK_TEXT, "India")
    checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    submit = (By.CSS_SELECTOR, "input[value='Purchase']")
    success = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def getLabels(self):
        return self.driver.find_element(*Confirmation.labels)

    def getDropdown(self):
        return self.driver.find_element(*Confirmation.dynamic_text)

#   def waitCountry(self):
#       return self.driver.find_element(*Confirmation.India)

    def getCheckbox(self):
        return self.driver.find_element(*Confirmation.checkbox)

    def getSubmitButton(self):
        return self.driver.find_element(*Confirmation.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Confirmation.success)
