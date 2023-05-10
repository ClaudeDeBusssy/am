# webscraper mit such funktion bauen
import scraper
import searchdatabase as sdb
from pprint import pprint

newEKC = scraper.EbayKleinanzeigenScraper(
    url_parameters={
        "base_url": "https://www.ebay-kleinanzeigen.de",
        "category": "s-autos", "number": 1,
        "sortierung": "preis",
        "preis": 0,
        "search": "bmw-330ci",
        "code": "k0c216"
    })

pprint(newEKC.get_page())
