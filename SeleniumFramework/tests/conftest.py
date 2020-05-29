import datetime

import pytest
from selenium import webdriver
driver = None  # for making driver a global variable for use with report modules


# browser invocation choose option from command line
# its called as hook \ and it has to be specifically like this
def pytest_addoption(parser):
    parser.addoption(
        "--BrowserName", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("BrowserName")  # you get it from request configuration as per the syntax here
    # option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    # option.add_argument("--ignore-certificate-errors")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/ami23772/Downloads/Study/Selenium_with_Python/chromedriver")
    elif browser_name == "firefox":
        # driver = webdriver.Chrome(executable_path="/Users/ami23772/Downloads/Study/Selenium_with_Python/chromedriver")
        print("Firefox is not installed on this machine")
    elif browser_name == "safari":
        driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver  # return and yield does not go together thus this is the industry practice to handle the objects
    # driver shall be returned to next class so that the child class knows which browser it invokes based on request as passed by this method
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    path = "/Users/ami23772/PycharmProjects/PythonSelFramework/reports/"

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + str(datetime.datetime.now().isoformat(' ', 'seconds')) + ".png"  # another way for time is datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            _capture_screenshot(path+file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
