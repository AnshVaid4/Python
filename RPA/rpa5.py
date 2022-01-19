from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://quotes.toscrape.com')
time.sleep(2)
usr=input("Enter username: ")
pwd=input("Enter password: ")
driver.find_element_by_css_selector('.col-md-4 a').click()
listloing=driver.find_element_by_css_selector('.col-md-4 a').click()
usrinp=driver.find_element_by_css_selector('#username')
usrinp.send_keys(usr)
pwdinp=driver.find_element_by_css_selector('#password')
pwdinp.send_keys(pwd)

driver.find_element_by_css_selector('.btn-primary').click() #going with value then "[value="Login"]"
driver.quit()