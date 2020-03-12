import time
from selenium import webdriver

FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
#FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

path = "C:/Users/Anurag/PycharmProjects/Python-Selenium/DataDrivenTestingExcel/Login.xlsx"
page_title = "Find a Flight: Mercury Tours: "

#driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")
driver = webdriver.Chrome()

driver.get("http://amazon.in")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)

# Getting all Cookies
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

# Adding a Cookie
cookie = {'name': 'MyCookie', 'value': '321654897'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

# Deleting a Cookie
driver.delete_cookie("MyCookie")
time.sleep(3)
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

# Deleting all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

driver.quit()