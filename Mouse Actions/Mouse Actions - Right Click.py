from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("http://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
print(driver.title)
time.sleep(3)

element = driver.find_element_by_xpath("//*[@id='authentication']/span")

actions = ActionChains(driver)
actions.context_click(element).perform()

time.sleep(3)

driver.quit()

