#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import SequenceMatcher
from pymongo import MongoClient

import csv
import os
import re

from categories import categories
from shops import shops
from products import item_parser as ip, items as d

# Store products to be uploaded
# Has the form:
# {
#   'c1001': [{parsed_item_11},...,{parsed_item_1N}],
#   ...
#   'c5006': [{parsed_item_N1},...,{parsed_item_NN}]
#  }
items = {}

# Last given iid to product
iid = 1000


def fetch_items():
    create_items()
    fetch_items_and_highest_iid()


# Create categories dict to save products
def create_items():
    for category in categories.categories:
        items[category['cid']] = []


# Fetch highest iid from db and items
def fetch_items_and_highest_iid():
    global iid

    # 2. Get database
    db = get_database()

    # Iterate over all categories in products
    # Each collection in db products is a category
    # Each category holds multiple products
    for category, item_list in items.items():
        # 3. Get collection
        col = get_collection(db, category)
        try:
            # 4. Get highest iid
            col_iid = col.find().sort([('iid', -1)]).limit(1).next()['iid'][-4:]
            iid = max(iid, int(col_iid))
            print('Highest iid: i' + str(iid))

            # 5. Get items from category
            cursor = col.find()
            for document in cursor:
                item_list.append(document)
        except StopIteration:
            print('Empty Cursor!')


# Get database products from cloud
def get_database(database="products"):
    print('### GET MONGODB COLLECTION ###')

    client = MongoClient(
        "mongodb+srv://daniel:hrgvbdxUVW2baN8W@cluster0-ccevx.mongodb.net/test?retryWrites=true&w=majority")
    db = client[database]

    print("Fetched: " + str(db))

    return db


# Get collection cid from fetched db products
def get_collection(database, collection):
    return database[collection]


# Parse item information from scraped csv shop data files.
# Creates item which will be inserted into products into appropriate category.
# Takes care of line breaks in csv files by counting elements in row.
# No return because each item is inserted into products
def parse_csv(file):
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
                        create_document(previous_row.extend(row[:diff - 1]), attr_positions)
                        row = row[diff:]
                    else:
                        create_document(previous_row, attr_positions)

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
            create_document(previous_row.extend(row[:diff - 1]), attr_positions)
        else:
            create_document(previous_row, attr_positions)


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
def create_document(row, attr_positions):
    global replaced_categories
    global items

    # Item schema
    item = {'iid': '', 'name': '', 'allergens': [], 'averageBewertung': None, 'descriptionLong': '',
            'descriptionShort': '', 'flavours': [], 'img': '', 'nutritionImg': '', 'nutritionText': '', 'minPrice': '',
            'minSize': '', 'popularity': None, 'shops': [], 'category': '', 'bewertungen': [], 'pricesInShops': [],
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
        if (len(item['descriptionLong']) <
                len(ip.parse_description_long(row[attr_positions['product-description-long']]))):
            item['descriptionLong'] = ip.parse_description_long(row[attr_positions['product-description-long']])
        try:
            if (len(item['descriptionShort']) <
                    len(ip.parse_description_short(row[attr_positions['product-description-short']]))):
                item['descriptionShort'] = ip.parse_description_short(row[attr_positions['product-description-short']])
        except KeyError:
            pass  # Leave description short empty
        if (ip.parse_nutrition(row[attr_positions['product-nutrition']]) and len(item['nutritionText']) <
                len(row[attr_positions['product-nutrition']])):
            item['nutritionText'] = row[attr_positions['product-nutrition']]
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
            item['urlsInShops'].append({'sid': sid, 'url': row[attr_positions['product-url']]})

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
        item['img'] = ip.parse_img(row[attr_positions['product-img']])
        if ip.parse_nutrition(row[attr_positions['product-nutrition']]):
            item['nutritionImg'] = row[attr_positions['product-nutrition']]
        else:
            item['nutritionText'] = row[attr_positions['product-nutrition']]
        item['minPrice'] = ip.parse_price(row[attr_positions['product-price']])
        try:
            item['minSize'] = ip.parse_size(row[attr_positions['product-size']])
        except KeyError:
            item['minSize'] = ip.parse_size_from_name(row[attr_positions['product-name']])
        item['popularity'] = 1
        item['shops'].append(sid)
        item['pricesInShops'].append({'sid': sid, 'price': ip.parse_price(row[attr_positions['product-price']])})
        item['urlsInShops'].append({'sid': sid, 'url': row[attr_positions['product-url']]})

        # 4.2 Add item to products
        items[cid].append(item)

    print("Created document: " + str(item))


# Checks if item-name in products.cid.
# If yes: Update this products.
# If no: Insert with iid greater than the latest element inserted.
def update_collection(col, documents):
    # update if document exists
    print("### UPDATE ###")
    i = 1
    for d in documents:
        res = col.find({'name': d['name']})
        if res.count() > 0:
            # Product exists in db
            d['iid'] = res.next()['iid']
            col.update_one({'name': d['name']}, {"$set": d}, upsert=False)
            print("Successfully Updated " + str(i) + "/" + str(len(documents)) + ": " + str(d))
        else:
            # Product doesn't exist in DB
            global new_products
            global iid
            new_products.append((col.name, d))
            iid = iid + 1
            d['iid'] = 'i' + str(iid)
            col.insert_one(d)
            print("Successfully Inserted  " + str(i) + "/" + str(len(documents)) + ": " + str(d))
        i += 1
    print("New Products: " + str(new_products))


# Updates single file
def update_file(file):
    global current_shop
    current_shop = d.collection_names[file]

    # 1. Parse csv
    parse_csv("../data/"+file)

    # 2. Get database
    db = get_database()

    # Iterate over all categories in products
    # Each collection in db products is a category
    # Each category holds multiple products
    for category, item_list in items.items():
        # 3. Get collection
        col = get_collection(db, category)
        # 4. Update collection
        update_collection(col, item_list)


# Updates all files in data
def update_all_files():
    dir = os.fsencode("data")
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            print("### PROCESS: " + filename + " ###")
            update_file(filename)


# Prints categories which weren't parsed even they were declared to be
def print_missing_categories(shop):
    print("Missing Categories: " + str({k: shop[k] for k in set(shop) - replaced_categories}))


# Global variables
current_shop = ""
replaced_categories = set()
new_products = []

fetch_items()

# Methods to update
# update_all_files()
update_file("weider.csv")

# print_missing_categories(d.category_matching["weider"])
