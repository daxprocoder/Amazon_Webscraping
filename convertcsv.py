import json
import csv

# Open the JSON file and load the data
with open('Digestion.json', 'r') as f:
    data = json.loads(f.read())

# Define the field names for the CSV file
fieldnames = [
    # 'url',
    'title',
    # 'Is Discontinued By Manufacturer',
    # 'Product Dimensions',
    'description',
    'main_img',
    'list_price',
    'price',
    'discount',
    'image1',
    'image2',
    'image3',
    'image4',
    'Net Quantity',
    'Manufacturer',
    'ASIN',
    'Item Weight',
    'Item Dimensions',
    'Item model number',
    'Country of Origin',
    'Manufacturer Address',
]

# Open the CSV file in write mode and write the header row
with open('Digestion.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each item in the data list and extract the details
    for item in data['data']:
        details_str = item['details']
        details_list = details_str.split('\n')
        details_dict = {}
        for detail in details_list:
            try:
                key, value = detail.split(' : ')
                details_dict[key] = value
            except ValueError:
                pass

        # Write the data row
        row = {
            # 'url': item['url'],
            'title': item['title'],
            # 'Is Discontinued By Manufacturer': details_dict.get('Is Discontinued By Manufacturer', ''),
            'description': item['description'],
            # 'Product Dimensions': details_dict.get('Product Dimensions', ''),
            # 'Date First Available': details_dict.get('Date First Available', ''),
            'Manufacturer': details_dict.get('Manufacturer', ''),
            'ASIN': details_dict.get('ASIN', ''),
            'Item model number': details_dict.get('Item model number', ''),
            'Country of Origin': details_dict.get('Country of Origin', ''),
            'Item Weight': details_dict.get('Item Weight', ''),
            'Item Dimensions': details_dict.get('Item Dimensions LxWxH', ''),
            'Net Quantity': details_dict.get('Net Quantity', ''),
            'main_img': item['main_img'],
            'list_price': item['list_price'],
            'price': item['price'],
            'discount': item['discount'],
            'Manufacturer Address': details_dict.get('Manufacturer', ''),
        }

        # Assign each image URL to a separate field named "image1", "image2", etc.
        for i, image_url in enumerate(item['images']):
            if i >= 4:
                break  # only store up to 10 images
            row[f'image{i+1}'] = image_url

        writer.writerow(row)
