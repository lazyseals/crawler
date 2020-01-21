#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import SequenceMatcher

import csv
import re

from categories import categories
from shops import shops
from products import item_parser as ip, items as d


# Parse item information from scraped csv shop data files.
# Creates item which will be inserted into products into appropriate category.
# Takes care of line breaks in csv files by counting elements in row.
# No return because each item is inserted into products
def parse_csv(file, current_shop, items):
    print('### CREATE DOCUMENTS FROM CSV ###')

    documents = []
    with open(file, newline='', encoding="utf8") as csvfile:

        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"', doublequote=True)
        previous_row = []
        iteration = 0

        for row in spamreader:
            # Check if the number of fields in this line is correct.
            # It will be less if any of this fields contained a line break.
            # If this is the case append the next line to this one.

            if iteration >= 1:
                # Rockanutrition is parsed differently than other files because of scraper output
                if file == "../data/rockanutrition.csv":
                    # Remove commas inside quotes
                    row = re.sub(',(?=[^"]*"[^"]*(?:"[^"]*"[^"]*)*$)', ".", row[0])
                    row = row.split(',')

                if iteration >= 2:
                    if len(previous_row) != 0 and len(previous_row) < fields_expected:
                        diff = fields_expected - len(previous_row)
                        create_document(previous_row.extend(row[:diff - 1]), attr_positions, current_shop, items)
                        row = row[diff:]
                    else:
                        create_document(previous_row, attr_positions, current_shop, items)

            elif iteration == 0:
                # Build element positions
                attr_positions = create_document_positions(row)
                fields_expected = len(row)
                print("Created attribute positions" + str(attr_positions))

            iteration += 1
            previous_row = row

        # Don't forget last row
        if len(previous_row) != 0 and len(previous_row) < fields_expected:
            diff = fields_expected - len(previous_row)
            create_document(previous_row.extend(row[:diff - 1]), attr_positions, current_shop, items)
        else:
            create_document(previous_row, attr_positions, current_shop, items)


# Creates positions where a certain attribute can be found in a row
def create_document_positions(row):
    attr_positions = {}

    # Define positions for elements to add in row
    i = 0
    for el in row:
        if el in d.possible_column_names:
            attr_positions[d.attribute_to_mongocol[el]] = i
        i += 1

    return attr_positions


# Creates item which will be inserted into products dictionary
def create_document(row, attr_positions, current_shop, items):

    # Item schema
    item = {'iid': '', 'name': '', 'allergens': [], 'averageBewertung': 0.0, 'descriptionLong': '',
            'descriptionShort': '', 'flavours': [], 'img': '', 'nutritionImg': '', 'nutritionText': '', 'minPrice': '',
            'minSize': '', 'popularity': 1, 'shops': [], 'category': '', 'bewertungen': [], 'pricesInShops': [],
            'urlsInShops': []}

    # 1. Get shop id
    for shop in shops.shops:
        if shop['name'] == current_shop:
            sid = shop['sid']
            break
    else:
        sid = None

    item['name'] = ip.parse_name(row[attr_positions['product-name']])
    item['category'], _replaced_categories, dont_upload = ip.parse_category(item['name'], current_shop,
                                                                           row[attr_positions['product-category']])

    if dont_upload:
        # Return if there are categories that shouldn't be uploaded
        return

    if _replaced_categories is not None:
        replaced_categories = _replaced_categories

    # 2. Get category id
    for category in categories.categories:
        if category['name'] == item['category']:
            cid = category['cid']
            item['category'] = cid
            break
    else:
        cid = None

    # 3. Check if product with url or same name exists
    item_found = False
    print(row)
    for i in items[cid]:
        if i['name'] == item['name']:
            item = i
            item_found = True
            break
        for sid_to_url in i['urlsInShops']:
            if sid_to_url['url'] == row[attr_positions['product-url']]:
                item = i
                item_found = True
                break
        else:
            continue
        break

    # 4. Update or insert item
    if item_found:
        # item exists in products => Only update certain fields
        name_match = SequenceMatcher(None, item['name'], ip.parse_name(row[attr_positions['product-name']]))\
            .find_longest_match(0, len(item['name']), 0, len(ip.parse_name(row[attr_positions['product-name']])))
        item['name'] = item['name'][name_match.a: name_match.a + name_match.size]
        item['averageBewertung'] = 0.0
        if (len(item['descriptionLong']) <
                len(ip.parse_description_long(row[attr_positions['product-description-long']]))):
            item['descriptionLong'] = ip.parse_description_long(row[attr_positions['product-description-long']])
        try:
            if (len(item['descriptionShort']) <
                    len(ip.parse_description_short(row[attr_positions['product-description-short']]))):
                item['descriptionShort'] = ip.parse_description_short(row[attr_positions['product-description-short']])
        except KeyError:
            pass  # Leave description short empty
        isImg, nutritionStr = ip.parse_nutrition(row[attr_positions['product-nutrition']])
        if not isImg and (len(item['nutritionText']) < len(nutritionStr)):
            item['nutritionText'] = nutritionStr
        if ip.parse_flavour(row[attr_positions['product-flavour']]) not in item['flavours']:
            item['flavours'].append(ip.parse_flavour(row[attr_positions['product-flavour']]))
        item['minPrice'] = min(ip.parse_price(row[attr_positions['product-price']]), item['minPrice'])
        try:
            item['minSize'] = ip.parse_size(row[attr_positions['product-size']])
        except KeyError:
            # Try to get size from name
            item['minSize'] = ip.parse_size_from_name(row[attr_positions['product-name']])
        if sid not in item['shops']:
            item['shops'].append(sid)
            item['pricesInShops'].append({'sid': sid, 'price': ip.parse_price(row[attr_positions['product-price']])})
            item['urlsInShops'].append({'sid': sid, 'url': ip.parse_url(row[attr_positions['product-url']])})

    else:
        # Insert new item in products

        # 4.1 Extract information from row
        item['allergens'] = ip.parse_allergens(row[attr_positions['product-allergens']])
        item['descriptionLong'] = ip.parse_description_long(row[attr_positions['product-description-long']])
        try:
            item['descriptionShort'] = ip.parse_description_short(row[attr_positions['product-description-short']])
        except KeyError:
            pass  # Leave description short empty
        item['flavours'].append(ip.parse_flavour(row[attr_positions['product-flavour']]))
        if current_shop == 'Zec+':
            item['img'] = 'https://www.zecplus.de/' + ip.parse_img(row[attr_positions['product-img']])
        else:
            item['img'] = ip.parse_img(row[attr_positions['product-img']])
        isImg, nutritionStr = ip.parse_nutrition(row[attr_positions['product-nutrition']])
        if isImg:
            item['nutritionImg'] = nutritionStr
        else:
            item['nutritionText'] = nutritionStr
        item['minPrice'] = ip.parse_price(row[attr_positions['product-price']])
        try:
            item['minSize'] = ip.parse_size(row[attr_positions['product-size']])
        except KeyError:
            item['minSize'] = ip.parse_size_from_name(row[attr_positions['product-name']])
        item['popularity'] = 1
        item['shops'].append(sid)
        item['pricesInShops'].append({'sid': sid, 'price': ip.parse_price(row[attr_positions['product-price']])})
        item['urlsInShops'].append({'sid': sid, 'url': ip.parse_url(row[attr_positions['product-url']])})

        # 4.2 Add item to products
        items[cid].append(item)

    print("Created document: " + str(item))