from selenium import webdriver
import time
from csv import DictWriter
import pandas as pd

header = ['ISBN', 'packtpub', 'amazon', 'barnesandnoble'] 
li=[]
dic=dict()

counter=1
while counter<6:
    driver = webdriver.Chrome('D:\\Sem\\RPA\\selenium\\chromedriver.exe')
    driver.maximize_window()
    url='https://www.packtpub.com/'
    driver.get(url)

    pricex='//*[@id="maincontent"]/div[3]/div/div[4]/div/div[2]/div/div/div[2]/div['+str(counter)+']/div/div[1]'
    try:
        price1=str(driver.find_element_by_xpath(pricex).text).replace(" ","").decode()
    except:
        price1=str(driver.find_element_by_xpath(pricex).text).replace(" ","")
    print("PRICE1=======================================> ",price1)
    try:
        bookx='//*[@id="maincontent"]/div[3]/div/div[4]/div/div[2]/div/div/div[2]/div['+str(counter)+']/div/a[2]'
        link=driver.find_element_by_xpath(bookx)
        link.click()
    except:
        bookx='//*[@id="maincontent"]/div[3]/div/div[4]/div/div[2]/div/div/div[2]/div['+str(counter)+']/a/span/span/img'
        link=driver.find_element_by_xpath(bookx)
        link.click()

    time.sleep(5)
    nurl=str(driver.current_url)
    isbn=nurl[-13:]
    time.sleep(5)


    url='https://www.amazon.in/s?k='+str(isbn)
    driver.get(url)
    price2=driver.find_element_by_css_selector('span[class="a-price-whole"]').text
    try:
        price2=("Rs "+str(price2)).decode()
    except:
        price2=("Rs "+str(price2))
    print("PRICE2=======================================> ",price2)
    time.sleep(5)



    url='https://www.barnesandnoble.com/w/privilege-escalation-techniques-alexis-ahmed/1140020136?ean='+str(isbn)
    driver.get(url)
    try:
        price3=(driver.find_element_by_css_selector('span[id="pdp-cur-price"]').text).decode()
    except:
        price3=(driver.find_element_by_css_selector('span[id="pdp-cur-price"]').text)
    print("PRICE3=======================================> ",price3)
    time.sleep(5)

    li.append({"ISBN":isbn,"packtpub":price1,"amazon":price2,"barnesandnoble":price3})

    counter+=1


with open("books.csv", "a") as file:
    headers = header
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for data in li:
        csv_writer.writerow(data)
df=pd.read_csv("books.csv")
df.to_csv("books.csv",index=False)
