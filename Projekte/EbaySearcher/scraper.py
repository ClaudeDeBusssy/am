from bs4 import BeautifulSoup
import requests


class EbayKleinanzeigenScraper:
    def __init__(self, url_parameters):
        self.url_parameters = url_parameters
        self.proxy_list = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            # 'Host': 'www.ebay-kleinanzeigen.de',
            'Accept': '*/*'}

    def get_page(self):
        itemlist = []
        formated_url = self.format_url()
        html = self.get_data(formated_url)
        listitems = html.find_all("li", {'class': 'ad-listitem'})

        for item in listitems:
            itemSoup = BeautifulSoup(str(item), 'html.parser')

            try:
                name = itemSoup.find('a', {'class': 'ellipsis'}).text
                link = itemSoup.find('a', {'class': 'ellipsis'})['href']
                price = itemSoup.find(
                    'p', {'class': 'aditem-main--middle--price-shipping--price'}).text
                place = itemSoup.find(
                    'div', {'class': 'aditem-main--top--left'}).text

                # print(name, link, price)
                itemlist.append([name.strip(), price.strip(), place.strip()])

            except:
                # print('fail')
                pass

        return itemlist

    def get_data(self, formated_url):
        res = requests.get(formated_url, headers=self.headers)
        return BeautifulSoup(res.text, 'html.parser')

    def format_url(self):
        formated_url = ""

        for index, key in enumerate(self.url_parameters.keys()):
            formated_url += str(self.format_parameter(key,
                                self.url_parameters[key]))

            if(index < len(self.url_parameters)-1):
                formated_url += '/'

        return formated_url

    def format_parameter(self, key, value):
        formated_value = ""
        value = str(value)

        if key == "number":
            formated_value = "seite:" + value
        elif key == "sortierung":
            formated_value = "sortierung:" + value
        elif key == "preis":
            formated_value = "preis:" + value + ":"
        else:
            formated_value = value

        return formated_value


# newEKC = Ebay_Kleinanzeigen_scraper(url_parameters_list=[{"base_url":"https://www.ebay-kleinanzeigen.de/"},{"category":"s-autos"},{"number": 1},{"search":"bmw-330ci"},{"code":"k0c216"}])
# newEKC = Ebay_Kleinanzeigen_scraper(url_parameters_list=[["base_url","https,//www.ebay-kleinanzeigen.de/"],["category","s-autos"],["number", 1],["search","bmw-330ci"],["code","k0c216"]])
# newEKC = Ebay_Kleinanzeigen_scraper(url_parameters_list=["base_url":"https://www.ebay-kleinanzeigen.de/",{"category":"s-autos"},{"number": 1},{"search":"bmw-330ci"},{"code":"k0c216"}])

# print(sc.url_parameters_list)

# sc.url_base = "https://www.ebay-kleinanzeigen.de/{category}{page}{search}{code}"
# sc.url_category = "{category}/"
# sc.url_page = "seite:{number}/"
# sc.url_search = "{search}/"
# sc.url_code = "{code}"

# sc.url_formatet_category = sc.url_category.format(category=sc.category)
# sc.url_formatet_page = sc.url_page.format(number = sc.number)
# sc.url_formatet_search = sc.url_search.format(search=sc.search)
# sc.url_formatet_code = sc.url_code.format(code = sc.code)

# sc.url_formatet_base = sc.url_base.format(category=sc.url_formatet_category, page=sc.url_formatet_page, search=sc.url_formatet_search, code=sc.url_formatet_code)
# print(sc.url_formatet_base)
