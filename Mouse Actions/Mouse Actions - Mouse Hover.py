from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
userMgmt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(userMgmt).move_to_element(users).click()
actions.perform()


time.sleep(3)
driver.quit()

