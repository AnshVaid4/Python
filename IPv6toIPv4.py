import ipaddress
import requests
import time
from bs4 import BeautifulSoup
with open("Filtered_initialiPsDump.txt") as file:
    lines=file.readlines()
    for line in lines:
        #print(line)
        try:
            if ":" in line:
                ipv6=line.replace("\n","")
                url="https://ipfind.io/ipv6-to-ipv4/"+ipv6
                r=requests.get(url)
                html=r.text #html code
                #print(html)
                soup=BeautifulSoup(html,'html.parser')
                #print(html)
                div = soup.find("a", class_= "innerATag")
                ipv4=str(div.text)+"\n"
                #print(ipv6," => ",ipv4)
                print(ipv4)
        except:
            pass
