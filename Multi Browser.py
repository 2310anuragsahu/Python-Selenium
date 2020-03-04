from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


def select_browser(browser_name: str):
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")
        return driver
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=FILEDIR + "Drivers/geckodriver.exe")
        return driver
    elif browser_name.lower() == 'ie':
        driver = webdriver.Ie(executable_path=FILEDIR + "Drivers/IEDriverServer.exe")
        return driver
    else:
        print("Invalid Browser")


driver = select_browser(input("Enter the browser: "))
driver.get("http://www.newtours.demoaut.com/")
driver.maximize_window()
print(driver.title)
print(driver.page_source)

time.sleep(5)

driver.close()
