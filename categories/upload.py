#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from categories import categories


# Gets collection "categories" from database "categories"
def get_collection(database="categories"):
    print('### GET MONGODB COLLECTION ###')

    client = MongoClient(
        "mongodb+srv://daniel:hrgvbdxUVW2baN8W@cluster0-ccevx.mongodb.net/test?retryWrites=true&w=majority")
    db = client[database]
    col = db[database]

    print("Fetched: " + str(col))

    return col


# Update collection "categories".
# Iterate over all categories from categories.py and insert them one by one
def update_collection(col):
    # update if document exists
    print("### UPDATE ###")
    for category in categories.categories:
        col.update_one({'cid': category['cid']}, {"$set": category}, upsert=True)
        # Product exists in DB
        print("Successfully Updated " + str(category))


# Update categories in database "categories"
def update_categories():
    # 1. Get database
    col = get_collection()

    # 2. Update collection
    update_collection(col)


# Update categories
update_categories()
