import sqlite3
from bs4 import BeautifulSoup
import requests

url = 'https://www.ebay-kleinanzeigen.de/s-autos/bmw-e46-330d-touring/k0c216+autos.km_i:%2C250000'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        # 'Host': 'www.ebay-kleinanzeigen.de',
        'Accept': '*/*',
    }


res = requests.get(url, headers=headers)
# text = res.text
soup = BeautifulSoup(res.text, 'html.parser')
listitems = soup.find_all("li",{'class': 'ad-listitem'})

for item in listitems:
    itemSoup = BeautifulSoup(str(item), 'html.parser')
    

    try:
        name = itemSoup.find('a', {'class': 'ellipsis'}).text
        link = itemSoup.find('a', {'class': 'ellipsis'})['href']
        price = itemSoup.find('p', {'class': 'aditem-main--middle--price-shipping--price'}).text
        place = itemSoup.find('div', {'class': 'aditem-main--top--left'}).text
        
        print(name, link, price)

    except:
        print('fail')
        

# names = listitems.find("a", {'class': 'ellipsis'})
# print(names.text)