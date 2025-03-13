from bs4 import BeautifulSoup
from selenium import webdriver
import time


def getAllPlayers():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # executable_path param is not needed if you updated PATH
    browser = webdriver.Chrome(
        options=options, executable_path='./chromedriver.exe')
    browser.get("https://www.ligainsider.de/stats/kickbase/rangliste/")
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    browser.quit()

    list = soup.find("tbody", {'class': 'ranking_column_holder'})
    rows = list.find_all("tr")

    spielerListe = []

    for row in rows:
        items = row.find_all("td")
        spieler = []
        for idx, item in enumerate(items):
            if idx > 1 & idx <= 9:
                spieler.append(item.text.replace("\n", ""))

        spielerListe.append(spieler)

    return spielerListe
