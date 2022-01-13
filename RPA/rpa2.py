import requests
from bs4 import BeautifulSoup

file = open("quote.txt","a")
file2 = open("quote.csv","a")
r=requests.get("https://quotes.toscrape.com")
html=r.text #html code
print(html)
soup=BeautifulSoup(html,'html.parser')
print(soup.span.string)
listquote=soup.findAll('span',{'class':'text'})
listauthor=soup.findAll('small',{'class':'author'})
for quote in listquote:
    file.write(quote.string)
    file.write("\n")
for author in listauthor:
    file2.write(author.string)
    file2.write("\n")