from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://quotes.toscrape.com')
# print((driver.find_element_by_css_selector('.text').text))  #returns single selenium class
# driver.find_elements_by_css_selector('.text')  #returns list of class

while True:
    
    for sclass in driver.find_elements_by_css_selector('.quote'):
        print(sclass.find_element_by_css_selector('.text').text,"\n ~By: ",sclass.find_element_by_css_selector('.author').text)
        print("\n\n")
    try:
        driver.find_element_by_css_selector('.next a').click()
    except:
        driver.quit()