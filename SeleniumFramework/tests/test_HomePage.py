import pytest
from selenium.webdriver.support.select import Select
import time

from TestData.HomePageData import HomePageData
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    # @pytest.mark.usefixtures("getData")
    def test_formSubmission(self, getData):
        log = self.getLogger()
        # driver = webdriver.Chrome(executable_path="/Users/ami23772/Downloads/Study/Selenium_with_Python/chromedriver")
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckout().click()
        # dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        """
        This is very exhaustive way and not to say hardcoded
        
            homepage.getGender().select_by_visible_text("Female")
            time.sleep(1)
            homepage.getGender().select_by_visible_text("Male")
        
        We can make it more flexible and reusable by making it generic in BaseClass
        then call the method and pass text
        """
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        radio = self.driver.find_elements_by_name("inlineRadioOptions")
        radio[1].click()
        # self.selectRadioOption(homepage.getEmploymentStatus(), "Employed")
        time.sleep(1)
        homepage.getDOB().send_keys(getData["birthdate"])
        log.info("Entered data is: " + getData['firstname'] + " " + getData['email'] + " " + getData['gender'] + " " + getData['birthdate'])
        time.sleep(1)
        # from here we assert the page content and then submit the form then we will go to shop
        # assert driver.execute_script("return document.getElementsByName('name')[0].value") == "A B C"
        # assert driver.execute_script("return document.getElementsByName('email')[0].value") == "abc@def.com"
        # assert driver.execute_script("return document.getElementById('exampleInputPassword1').value") != ""
        # assert driver.execute_script("return document.getElementById('exampleFormControlSelect1').value") == "Male"
        # assert radio[1].is_selected()
        # assert driver.execute_script("return document.getElementsByName('bday')[0].value") == "1999-12-21"
        homepage.getButton().click()
        time.sleep(1)
        log.info("Text after submission is: " + homepage.getMessage().text)
        assert "Success" in homepage.getMessage().text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase1", "Testcase2"))
    def getData(self, request):
        return request.param
