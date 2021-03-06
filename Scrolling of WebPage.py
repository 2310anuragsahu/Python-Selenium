from selenium import webdriver
import time

#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("https://demoqa.com/automation-practice-table/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

# driver.execute_script("window.scrollBy(0,500)", "")
# time.sleep(3)

# element = driver.find_element_by_link_text("Tooltip")
# driver.execute_script("arguments[0].scrollIntoView();", element)
# time.sleep(3)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

driver.quit()

