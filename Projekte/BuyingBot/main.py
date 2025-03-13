import JsonData as jd

fileName = "./personalData.json"

firstName = "Thomas"
lastName = "Margowski"

country = "Deutschland"
city = "Grettstadt"
postalCode = "97508"
street = "Bachstraße"
streetNumber = "7"

data = {
    "firstName": firstName,
    "lastName": lastName,
    "country": country,
    "city": city,
    "postalCode": postalCode,
    "street": street,
    "streetNumber": streetNumber
}

jd.write_json_data(fileName, data)
print(jd.read_json_data(fileName))
