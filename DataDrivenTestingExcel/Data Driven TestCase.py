import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from DataDrivenTestingExcel import ExcelUtilities

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

path = "C:/Users/Anurag/PycharmProjects/Python-Selenium/DataDrivenTestingExcel/Login.xlsx"
page_title = "Find a Flight: Mercury Tours: "

driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

driver.get("http://www.newtours.demoaut.com/")
driver.refresh()
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)

rows = ExcelUtilities.getRowCount(path, "Sheet1")
for r in range(2, rows+1):
    username = ExcelUtilities.readData(path, "Sheet1", r, 1)
    password = ExcelUtilities.readData(path, "Sheet1", r, 2)
    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element_by_name("login").click()

    print(driver.title)

    if driver.title == page_title:
        print("Test Passed")
        ExcelUtilities.writeData(path, "Sheet1", r, 3, "Passed")
    else:
        print("Test Failed")
        ExcelUtilities.writeData(path, "Sheet1", r, 3, "Failed")

    driver.find_element_by_link_text("Home").click()
    time.sleep(3)

driver.quit()

