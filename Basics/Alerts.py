from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)

# alerts
print(driver.switch_to_alert().text)
driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()

time.sleep(5)

driver.quit()

