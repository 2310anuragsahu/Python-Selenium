from selenium import webdriver
import time

FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
#FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)

print(driver.current_window_handle)

# For switching to new tab, uncomment the below code
# driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# For switching to new window, uncomment the below code
driver.find_element_by_link_text("Open New Seperate Windows").click()
driver.find_element_by_xpath("//*[@id='Seperate']/button").click()

time.sleep(3)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

driver.find_element_by_link_text("Contact").click()

time.sleep(3)

driver.quit()

