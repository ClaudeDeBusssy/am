import requests
from bs4 import BeautifulSoup as bs
import sqlite3

colorTable = []



url = 'https://dtpstudio.de/atlas/farbsysteme/standox%20Autolacke_bs00_3.htm'

res = requests.get(url)

soup = bs(res.text, 'html.parser')

colorListItems = soup.find_all("tr")

for item in colorListItems:
    itemSoup = bs(str(item), 'html.parser')
    entrys = itemSoup.find_all("td")
    # print(entrys[1].text)
    # print(entrys[0]["bgcolor"])
    colorTable.append([entrys[1].text, entrys[0]["bgcolor"]])

database = sqlite3.connect("colors.db")
cursor = database.cursor()
cursor.execute( """
create table if not exists colorTable (
    id INTEGER PRIMARY KEY,
    color_name TEXT,
    color_code TEXT
);
""" )


index = 0

for entry in colorTable:
    index += 1
    sqlCommand = "insert into colorTable values"
    sqlCommand += "("+ str(index) + ",'" + str(entry[0].replace("'", "")) + "','" + str(entry[1].replace("'", "")) + "')"
    sqlCommand += ';'
    print(sqlCommand)
    cursor.execute(sqlCommand)



database.commit()