from selenium import webdriver
import time
import pytest

FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
#FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()


    def test_homePageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        assert self.driver.title == "OrangeHRM"


    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM 123"

# pytest -v -s --html=report.html --self-contained-html test_Orange_Reporting.py

# To change directory
# pytest -v -s --html=.\reports\report.html --self-contained-html test_Orange_Reporting.py