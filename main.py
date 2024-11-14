#!/usr/bin/python

import json
import cProfile

extracted_url_list = []

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        returned_json_data = json.load(file)
    print(type(returned_json_data))
    return returned_json_data

# Extract values of url key to global list. 
def get_url_from_json(json_data, key='url'):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == 'url':
                extracted_url_list.append(value)
            get_url_from_json(value, extracted_url_list)  # Recursively search in the value
    elif isinstance(json_data, list):
        for item in json_data:
            get_url_from_json(item, extracted_url_list)  # Recursively search in the list items

def main():
    print('[BEGIN]')
    json_data = read_json_file("test.json")
    get_url_from_json(json_data)
    print("[!] URL List: ")
    for item in extracted_url_list:
        print(item)
    print("Line count: " + str(len(extracted_url_list)))
        
if __name__ == '__main__':
    cProfile.runctx(main(), globals(), locals())
