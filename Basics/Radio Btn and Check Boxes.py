from selenium import webdriver
from selenium.webdriver.common.by import By
import time

FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
#FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("https://demoqa.com/automation-practice-form/")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)

firstName = driver.find_element( By.NAME, "firstname" )
if firstName.is_displayed( ) & firstName.is_enabled( ):
    firstName.send_keys( "Anurag" )
else:
    print("Invalid element")

lastName = driver.find_element( By.ID, "lastname" )
if lastName.is_displayed( ) & lastName.is_enabled( ):
    lastName.send_keys( "Sahu" )
else:
    print("Invalid element")


sex_male = driver.find_element_by_id("sex-0")
if not sex_male.is_selected():
    sex_male.click()

profession = driver.find_element_by_id("profession-1")
if not profession.is_selected():
    profession.click()

driver.implicitly_wait(5)

time.sleep(5)

driver.quit()

