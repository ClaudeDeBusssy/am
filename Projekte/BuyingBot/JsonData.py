import json


def read_json_data(json_name):
    with open(json_name) as json_file:
        data = json.load(json_file)
        return data


def write_json_data(json_name, data):
    with open(json_name, 'w') as outfile:
        json.dump(data, outfile)
