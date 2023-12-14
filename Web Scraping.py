# Molly Tran
# CS 87B - Web Scraping
# Assignment 7

import requests
import json
import re
import csv

# Method to fetch and extract data from the URL and create dictionary entry for each breed
def fetch_extract_data(url):
    breed_data = {}
    response = requests.get(url)

    data = json.loads(response.text)

    items = data['items']

    for item in items:
        breed_match = re.search(r"'name': '([a-zA-Z. ]+)", str(item))
        breed_name = breed_match.group(1)
        description_match = re.search(r"'shareDescription': '(.*?)'", str(item))
        description = description_match.group(1)
        hearts_match = re.search(r"':heart:', (\d+)", str(item))
        hearts = hearts_match.group(1)
        thumbsUp_match = re.search(r"':thumbsup:', (\d+)", str(item))
        thumbsUp = thumbsUp_match.group(1)

        breed_data[breed_name] = {
            'Description': str(description),
            'Hearts': hearts,
            'Thumbs Up': thumbsUp
        }

    return breed_data


# Method to create a json file and write breed data to it
def create_json_file(breed_data):
    output_file = 'breed_data.json'
    with open(output_file, 'w') as file:
        json.dump(breed_data, file, indent=4)

    print(f'Data has been written to {output_file}.')

    return file

# Method to create a CSV file and write breed data to it
def create_text_file(breed_data):
    output_file = 'breed_data.csv'
    with open(output_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        headers = ['Breed', 'Description', 'Hearts', 'Thumbs Up']
        csv_writer.writerow(headers)

        for key, value in breed_data.items():
            breed = key
            description = value['Description']
            hearts = value['Hearts']
            thumbsUp = value['Thumbs Up']
            csv_writer.writerow([breed, description, hearts, thumbsUp])

    print(f'Data has been written to {output_file}.')

    return file

# Main method to execute the code
def main():
    url = "http://list.ly/api/v4/lists/17qW/items"

    breed_data = fetch_extract_data(url)
    create_json_file(breed_data)
    create_text_file(breed_data)


main()
