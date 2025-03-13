from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    # 'Host': 'www.ebay-kleinanzeigen.de',
    'Accept': '*/*',
}

searchPromts = ["survival horror let's play"]
# "horror let's play",
# "scary game let's play",
# "best survival horror let's play",
# "funny survival horror let's play",
# "new survival horror let's play",
# "upcoming survival horror let's play",
# "indie survival horror let's play",
# "retro survival horror let's play",
# "Japanese survival horror let's play",
# "Korean survival horror let's play",
# "Chinese survival horror let's play",
# "Resident Evil let's play",
# "Silent Hill let's play",
# "Fatal Frame let's play",
# "Amnesia let's play",
# "Outlast let's play",
# "Soma let's play",
# "Alien: Isolation let's play",
# "Dead Space let's play",
# "Little Nightmares let's play",
# "Layers of Fear let's play",
# "Visage let's play",
# "The Evil Within let's play"]


urlSearch = "https://www.youtube.com/results?search_query="
urlList = []

users = []

for promt in searchPromts:
    urlList.append(urlSearch + promt.replace(" ", "+"))


for url in urlList:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # executable_path param is not needed if you updated PATH
    browser = webdriver.Chrome(
        options=options, executable_path='./chromedriver.exe')
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    browser.quit()

    list = soup.find_all("div", {'class': 'style-scope ytd-video-renderer'})

    for item in list:
        try:
            newUser = "https://www.youtube.com" + item.find(
                "a", {'class': 'yt-simple-endpoint style-scope yt-formatted-string'})['href']
        except:
            pass

        userAlreadyInList = False

        for user in users:
            if user == newUser:
                userAlreadyInList = True

        if userAlreadyInList == False:
            users.append(newUser)

with open('youtuberList.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(users)
