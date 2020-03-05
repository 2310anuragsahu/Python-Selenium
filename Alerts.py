from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# alerts
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()

print(driver.switch_to_alert().text)
time.sleep(2)
#driver.switch_to_alert().dismiss()

driver.switch_to.frame()

time.sleep(5)

driver.quit()

