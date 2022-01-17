import requests
from bs4 import BeautifulSoup
from csv import DictWriter
flag=0
num=1
while num <250:
    url="https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start="+str(num)+"&ref_=adv_nxt"
    with open("movies.csv", "a") as file:
        headers = ["Movie Name", "Rating","Time","Director"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
    r=requests.get(url)
    html=r.text #html code
    #print(html)
    soup=BeautifulSoup(html,'html.parser')

    listtitle=soup.findAll('div',{'class':'lister-item mode-advanced'})


    for row in listtitle:
        title=row.find('h3',{'class':'lister-item-header'})
        title=title.a.string

        rating=row.find('div',{'class':'ratings-bar'})
        rating=rating.strong.string

        time=row.find('p',{'class':'text-muted'})
        for period in time:
            period=time.find('span',{'class':'runtime'})
        time=period.string

        director=row.find('p',{'class':''})
        director=director.a.string
        
        movie=(title,rating,time,director)

        with open("movies.csv", "a") as file:
            if flag == 0:
                headers = ["Movie Name", "Rating","Time","Director"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writeheader()
                flag+=1
            headers = ["Movie Name", "Rating","Time","Director"]
            csv_writer = DictWriter(file, fieldnames=headers)
            csv_writer.writerow({"Movie Name": movie[0], "Rating": movie[1], "Time": movie[2], "Director": movie[3]})
    print((num+49), " Movies Recorded" )
    num+=50
