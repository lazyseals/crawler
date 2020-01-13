#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from categories import categories


def get_collection(collection, database="categories"):
    print('### GET MONGODB COLLECTION ###')

    client = MongoClient(
        "mongodb+srv://daniel:hrgvbdxUVW2baN8W@cluster0-ccevx.mongodb.net/test?retryWrites=true&w=majority")
    db = client[database]
    col = db[collection]

    print("Fetched: " + str(col))

    return col


def update_collection(col, d):
    # update if document exists
    print("### UPDATE ###")
    col.update_one({'cid': d['cid']}, {"$set": d}, upsert=True)
    # Product exists in DB
    print("Successfully Updated " + str(d))


def update_category(category):
    # 1. Get database
    col = get_collection(collection=category['cid'])

    # 2. Update collection
    update_collection(col, category)


def update_all_categories():
    for category in categories:
        update_category(category)


update_all_categories()
