from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")
time.sleep(5)


driver.get("http://www.newtours.demoaut.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)

driver.get("https://demoqa.com/automation-practice-form/")
print(driver.title)
time.sleep(5)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)

driver.quit()

