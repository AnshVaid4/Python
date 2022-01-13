import requests
counter=1
while True:
    url="https://quotes.toscrape.com/page/"+str(counter)
    r=requests.get(url)
    #print(r.status_code)
    if r.status_code >=400 or counter > 10:
        break
    #print(r.text)
    code=r.text.split('\n')
    for i in code:
        if "<span class=\"text\" itemprop=\"text\">" in i:
            quote=i.split("“")
            quote=quote[1]
            quote=quote.split("”")
            quote=quote[0]
            print(quote)
    counter+=1