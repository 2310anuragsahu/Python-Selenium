import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from DataDrivenTestingExcel import ExcelUtilities

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

path = "C:/Users/Anurag/PycharmProjects/Python-Selenium/DataDrivenTestingExcel/Login.xlsx"
page_title = "Find a Flight: Mercury Tours: "

driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

driver.get("http://amazon.in")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)

driver.save_screenshot("C:/Users/Anurag/Pictures/ScreenshotDemo1.jpg")
time.sleep(2)

driver.get_screenshot_as_file("C:/Users/Anurag/Pictures/ScreenshotDemo2.jpg")

driver.quit()