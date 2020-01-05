#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

import csv
import os
import re

import dictionaries as d
import shop_parser as sp


def get_collection(collection, database="shops"):
    print('### GET MONGODB COLLECTION ###')

    client = MongoClient(
        "mongodb+srv://daniel:hrgvbdxUVW2baN8W@cluster0-ccevx.mongodb.net/test?retryWrites=true&w=majority")
    db = client[database]
    col = db[collection]

    print("Fetched: " + str(col))

    return col


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
                if file == "data/rockanutrition.csv":
                    # Remove commas inside quotes
                    row = re.sub(',(?=[^"]*"[^"]*(?:"[^"]*"[^"]*)*$)', ".", row[0])
                    row = row.split(',')

                if iteration >= 2:
                    if len(previous_row) != 0 and len(previous_row) < fields_expected:
                        diff = fields_expected - len(previous_row)
                        to_append = create_document(previous_row.extend(row[:diff - 1]), attr_positions)
                        row = row[diff:]
                    else:
                        to_append = create_document(previous_row, attr_positions)
                    documents.append(to_append)
                    print("Created document: " + str(to_append))

            elif iteration == 0:
                # Build element positions
                attr_positions = create_document_positions(row)
                fields_expected = len(row)
                print("Created attribute positions" + str(attr_positions))

            iteration += 1
            previous_row = row

        # Don't forget last row
        # TODO

        return documents


def match_category(category, shop):
    # replace native shop category name with my category name if defined
    if category.lower() in d.category_matching[shop]:
        global replaced_categories
        replaced_categories.add(category.lower())
        return d.category_matching[shop][category.lower()]
    else:
        return category


def create_document_positions(row):
    attr_positions = {}

    # Define positions for elements to add in row
    i = 0
    for el in row:
        if el in d.possible_column_names:
            attr_positions[d.attribute_to_mongocol[el]] = i
        i += 1

    return attr_positions


def create_document(row, attr_positions):
    document = {}

    # Create document
    #
    # IMPORTANT: product-category needs to come before product-name in columns_to_add
    #
    for col in d.columns_to_add:
        try:
            # Parse out linebreaks
            el = re.sub("/\r?\n|\r/", "", row[attr_positions[col]])
            el = re.sub('"', '', el)
            # Match product category
            if col == 'product-category':
                el = match_category(el, current_shop)
                category_save = el
            elif col == 'product-name':
                el = sp.parse_rocka(category_save, el)
            # Set document element
            document[col] = el
        except KeyError:
            # Key error if csv contains not a col which is expected.
            # E.g. "rockanutrition" doesn't have key "product-size"
            pass

    return document


def upsert_collection(col, documents):
    # update if document exists else insert => up(date)(in)sert
    print("### UPDATE ###")
    i = 1
    for d in documents:
        col.update_one({'product-name': d['product-name'], 'product-flavour': d['product-flavour'],
                        'product-category': d['product-category']}, {"$set": d}, True)
        print("Updated " + str(i) + "/" + str(len(documents)) + ": " + str(d))
        i += 1


def print_replaced_categories():
    print(replaced_categories)


def update_file(file):
    global current_shop
    current_shop = d.collection_names[file]

    # 1. Get database
    # col = get_collection(collection=d.collection_names[file])

    # 2. Parse csv
    documents = parse_csv("data/"+file)

    # 3. Update collection
    # upsert_collection(col, documents)


def update_all_files():
    dir = os.fsencode("data")
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            print("### PROCESS: " + filename + " ###")
            update_file(filename)


# Global variables
current_shop = ""
replaced_categories = set()

# Methods to update
# update_all_files()
update_file("rockanutrition.csv")
