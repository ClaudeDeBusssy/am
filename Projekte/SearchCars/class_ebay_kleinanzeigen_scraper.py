


class Ebay_Kleinanzeigen_scraper:
    def __init__(sc,url_parameters):
        sc.url_parameters = url_parameters
        sc.proxy_list = []


    def get_page(sc):
        formated_url = sc.format_url()
        return sc.get_data(formated_url)


    def get_data(sc, formated_url):
        data = "data for " + formated_url
        return data


    def format_url(sc):
        formated_url = ""

        for index, key in enumerate(sc.url_parameters.keys()):
            formated_url+= str(sc.format_parameter(key, sc.url_parameters[key]))
            
            if(index < len(sc.url_parameters)-1):
                formated_url += '/' 

        return formated_url


    def format_parameter(sc, key,value):
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
newEKC = Ebay_Kleinanzeigen_scraper(
    url_parameters={
    "base_url":"https://www.ebay-kleinanzeigen.de",
    "category":"s-autos","number": 1,
    "sortierung":"preis",
    "preis":0,
    "search":"bmw-330ci",
    "code":"k0c216"
    })

print(newEKC.get_page())














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
