from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
import allure


FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
#FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

@allure.severity(allure.severity_level.NORMAL)
class TestOrangeHRM():
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        image_present = self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if image_present == True:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_listEmployees(self):
        pytest.skip("Skipping Test - Not ready")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        title = self.driver.title
        if title == "OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

# pytest -v -s  --alluredir="C:\Users\inasahu\PycharmProjects\Python-Selenium\PyTestDemo\Allure_Reporting_pytest\reports" PyTestDemo\Allure_Reporting_pytest\test_Orange_AllureReporting.py

