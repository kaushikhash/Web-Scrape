from bs4 import BeautifulSoup
import requests
import json

def main(URL):

    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(URL,headers=HEADERS)
    soup = BeautifulSoup(webpage.content,"html.parser")
    
    all_title = soup.find_all("span",{"class": 'a-size-medium a-color-base a-text-normal'})
    all_prices = soup.find_all("span",{"class":"a-price-whole"})
    l = {}
    u = list()
    for i in range(0,len(all_title)):
        l["title"] = all_title[i].text.replace("\n","")
        l["price"] = all_prices[i].text.replace("\n","")
        u.append(l)
        l={}
    

    
    with open("sample.json","w") as outfile:
        json.dump(u,outfile)
        

if __name__ == '__main__':
    file = open("url.txt", "r")
 
    for links in file.readlines():
        main(links)
