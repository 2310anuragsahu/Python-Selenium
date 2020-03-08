from selenium import webdriver
import time

FILEDIR = "C:/Users/inasahu/PycharmProjects/SeleniumPython/"
#FILEDIR = "C:/Users/Anurag/PycharmProjects/Python-Selenium/"


driver = webdriver.Chrome(executable_path=FILEDIR + "Drivers/chromedriver.exe")

# implicit wait
driver.implicitly_wait(5)

driver.get("https://demoqa.com/automation-practice-table/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

# counting number of Rows
rows = len( driver.find_elements_by_xpath("*//table[@class='tsc_table_s13']/tbody/tr"))
print("Number of Rows: ", rows)

# counting number of Columns
cols = len( driver.find_elements_by_xpath("*//table[@class='tsc_table_s13']/tbody/tr[1]/th "
                                          "| *//table[@class='tsc_table_s13']/tbody/tr[1]/td"))
print("Number of Columns: ", cols)
print()

# Printing Header row
row_header = len(driver.find_elements_by_xpath("*//table[@class='tsc_table_s13']/thead/tr/th"))
for rh in range(1, row_header+1):
    # value_header = driver.find_element_by_xpath( f"*//table[@class='tsc_table_s13']/thead/tr/th[{rh}]" )
    # OR
    value_header = driver.find_element_by_xpath("*//table[@class='tsc_table_s13']/thead/tr/th["+str(rh)+"]")
    print(value_header.text, end="    ")
print()

# Printing Table Body
for r in range(1, rows+1):
    xpath_th = "*//table[@class='tsc_table_s13']/tbody/tr["+str(r)+"]/th[1]"
    value_th = driver.find_element_by_xpath(xpath_th)
    print(value_th.text, end="    ")
    for c in range(1, cols):
        xpath_td = "*//table[@class='tsc_table_s13']/tbody/tr["+str(r)+"]/td["+str(c)+"]"
        value_td = driver.find_element_by_xpath(xpath_td)
        print(value_td.text, end="    ")
    print()
time.sleep(3)

driver.quit()

