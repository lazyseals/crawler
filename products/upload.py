#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

import os

from categories import categories
from products import items as d
from products import parser as p

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
                # Item schema
                item = {'iid': document['iid'], 'name': document['name'], 'allergens': document['allergens'],
                        'averageBewertung': document['averageBewertung'],
                        'descriptionLong': document['descriptionLong'],
                        'descriptionShort': document['descriptionShort'], 'flavours': document['flavours'],
                        'img': document['img'], 'nutritionImg': document['nutritionImg'],
                        'nutritionText': document['nutritionText'], 'minPrice': document['minPrice'],
                        'minSize': document['minSize'], 'popularity': document['popularity'],
                        'shops': document['shops'], 'category': document['category'],
                        'bewertungen': document['bewertungen'], 'pricesInShops': document['pricesInShops'],
                        'urlsInShops': document['urlsInShops']}
                item_list.append(item)
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


# Checks if item-name in products.cid.
# If yes: Update this products.
# If no: Insert with iid greater than the latest element inserted.
def update_collection(col, documents):
    # 1. Remove collection
    col.drop()

    # 2. Insert created documents
    print("### INSERT ###")
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
def update_file(file, update_all=False):
    global current_shop
    global items
    current_shop = d.collection_names[file]

    # 1. Parse csv
    p.parse_csv("../data/"+file, current_shop, items)

    # If update all files at once, than upload items only ones inside upload all files method
    if not update_all:

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
    dir = os.fsencode("../data")
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            print("### PROCESS: " + filename + " ###")
            update_file(filename, update_all=True)
    db = get_database()
    for category, item_list in items.items():
        # 3. Get collection
        col = get_collection(db, category)
        # 4. Update collection
        update_collection(col, item_list)


# Prints categories which weren't parsed even they were declared to be
def print_missing_categories(shop):
    print("Missing Categories: " + str({k: shop[k] for k in set(shop) - replaced_categories}))


# Global variables
current_shop = ""
replaced_categories = set()
new_products = []

create_items()

# Methods to update
update_all_files()
# update_file("myprotein.csv")

# print_missing_categories(d.category_matching["weider"])
