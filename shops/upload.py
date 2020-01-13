#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from shops import shops


def get_collection(collection, database="shops"):
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
    col.update_one({'sid': d['sid']}, {"$set": d}, upsert=True)
    # Product exists in DB
    print("Successfully Updated " + str(d))


def update_shop(shop):
    # 1. Get database
    col = get_collection(collection=shop['sid'])

    # 2. Update collection
    update_collection(col, shop)


def update_all_shops():
    for shop in shops:
        update_shop(shop)


update_all_shops()