from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("http://www.newtours.demoaut.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)

# Links
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links on Demo Tour page: ", len(links))

for link in links:
    print(link.text)

#driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()

time.sleep(5)

driver.quit()

