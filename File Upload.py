from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("http://demo.guru99.com/test/upload/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

input_tag_id = "//*[@id='uploadfile_0']"

driver.find_element_by_xpath(input_tag_id).send_keys("C:/Users/Anurag/Downloads/Hair-Loss-Protocol.png")

time.sleep(3)

driver.quit()

