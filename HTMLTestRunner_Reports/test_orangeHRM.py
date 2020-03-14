import unittest

from selenium import webdriver
from unittest import TestCase
import time
import HtmlTestRunner

FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
#FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


class TestOrangeHRM(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed..")

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        title = self.driver.title
        self.assertEqual(title, "OrangeHRM123")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(3)
        self.assertEqual(self.driver.title, "OrangeHRM")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=".//HTMLTestRunner_Reports/Reports"))
