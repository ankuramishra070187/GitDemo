import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  # to put explicit wait conditions
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 12)
        element = wait.until(ec.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        # ******** Logging object created *******************
        loggerName = inspect.stack()[1][3]  # this to get the correct method name
        logger = logging.getLogger(loggerName)  # changed from __name__ because it is changed to print correct test case name

        # ******** Define path and file name object *********
        # add handler will be given with handler for files
        # it takes file handler object (file handler object is nothing but file name and location)
        fileHandler = logging.FileHandler("logfile.log")

        # ******* define Logging format **********************
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # ****** make relation between format object and Logger object ****
        fileHandler.setFormatter(formatter)  # Passed log formatter to file handler to relate them together
        logger.addHandler(fileHandler)  # passed file handler object to logger to relate them

        logger.setLevel(logging.INFO)
        return logger
