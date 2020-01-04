#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import csv
import re

# column names which may appear in row
possible_column_names = [
    'product-name',
    'product-url-href',
    'product-description-long',
    'product-price',
    'product-size',
    'product-flavour',
    'product-img-src',
    'product-img',
    'product-nutrition-src',
    'product-nutrition',
    'product-allergens-src',
    'product-allergens',
    'product-category'
]

# match html attribute elements to real mongodb columsn which will be added
attribute_to_mongocol = {
    'product-url-href': 'product-url',
    'product-nutrition-src': 'product-nutrition',
    'product-allergens-src': 'product-allergens',
    'product-img-src': 'product-img',
    'product-name': 'product-name',
    'product-description-long': 'product-description-long',
    'product-price': 'product-price',
    'product-size': 'product-size',
    'product-flavour': 'product-flavour',
    'product-img': 'product-img',
    'product-nutrition': 'product-nutrition',
    'product-allergens': 'product-allergens',
    'product-category': 'product-category'
}

# columns which will be added to mongodb per document
columns_to_add = [
    'product-name',
    'product-url',
    'product-description-long',
    'product-price',
    'product-size',
    'product-flavour',
    'product-img',
    'product-nutrition',
    'product-allergens',
    'product-category'
]


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
                if file == "rockanutrition.csv":
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


def create_document_positions(row):
    attr_positions = {}

    # Define positions for elements to add in row
    i = 0
    for el in row:
        if el in possible_column_names:
            attr_positions[attribute_to_mongocol[el]] = i
        i += 1

    return attr_positions


def create_document(row, attr_positions):
    document = {}
    tmp = {}

    # Create document
    for col in columns_to_add:
        try:
            # Parse out linebreaks
            document[col] = re.sub("/\r?\n|\r/", "", row[attr_positions[col]])
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
        col.update_one({'product-name': d['product-name'], 'product-flavour': d['product-flavour']}, {"$set": d}, True)
        print("Updated " + str(i) + "/" + str(len(documents)) + ": " + str(d))
        i += 1


# 1. Get database
col = get_collection(collection="fitmart")


# 2. Parse csv
documents = parse_csv("data/fitmart.csv")

# 3. Update collection
upsert_collection(col, documents)
