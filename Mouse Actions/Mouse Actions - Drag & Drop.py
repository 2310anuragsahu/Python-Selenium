from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("https://demoqa.com/droppable/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

source = driver.find_element_by_xpath("//*[@id='draggable']")
target = driver.find_element_by_xpath("//*[@id='droppable3']")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

time.sleep(3)

driver.quit()

