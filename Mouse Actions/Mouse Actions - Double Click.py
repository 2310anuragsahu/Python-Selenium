from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
actions.double_click(element).perform()

time.sleep(3)

driver.quit()

