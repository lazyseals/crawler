#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from categories import categories


def get_collection(database="categories"):
    print('### GET MONGODB COLLECTION ###')

    client = MongoClient(
        "mongodb+srv://daniel:hrgvbdxUVW2baN8W@cluster0-ccevx.mongodb.net/test?retryWrites=true&w=majority")
    db = client[database]
    col = db[database]

    print("Fetched: " + str(col))

    return col


def update_collection(col):
    # update if document exists
    print("### UPDATE ###")
    for category in categories:
        col.update_one({'cid': category['cid']}, {"$set": category}, upsert=True)
        # Product exists in DB
        print("Successfully Updated " + str(category))


def update_categories():
    # 1. Get database
    col = get_collection()

    # 2. Update collection
    update_collection(col)


update_categories()
