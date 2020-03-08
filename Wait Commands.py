from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"

driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

#
# Implicit wait
#
driver.implicitly_wait(5)

driver.get("http://www.newtours.demoaut.com/")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)

userName = driver.find_element(By.NAME, "userName")
if userName.is_displayed() & userName.is_enabled():
    userName.send_keys("mercury")
else:
    print("Invalid element")

password = driver.find_element(By.NAME, "password")
if password.is_displayed() & password.is_enabled():
    password.send_keys("mercury")
else:
    print("Invalid element")

driver.find_element_by_name("login").click()

driver.implicitly_wait(5)

#
# Explicit wait
#
wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable(By.XPATH, "*//form[@name='findflight']//input[@value='roundtrip']"))
# OR
element = wait.until(EC.element_to_be_clickable((By.XPATH, "*//form[@name='findflight']//input[@value='roundtrip']")))
element.click()
print("clicked")

radiobutton_roundtrip = driver.find_element_by_xpath("*//form[@name='findflight']//input[@value='roundtrip']")
assert radiobutton_roundtrip.is_selected()

radiobutton_onetrip = driver.find_element_by_xpath("*//form[@name='findflight']//input[@value='oneway']")
assert not radiobutton_onetrip.is_selected()

driver.quit()

