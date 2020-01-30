#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import SequenceMatcher

import csv
import re

from categories import categories
from shops import shops
from products import item_parser as ip, items as d

# Global property max most popular items
max_popular = 60


# Parse item information from scraped csv shop data files.
# Creates item which will be inserted into items into appropriate category.
# Takes care of line breaks in csv files by counting elements in row.
# No return because each item is inserted into global dict items.
def parse_csv(file, current_shop, items):
    print('### CREATE DOCUMENTS FROM CSV ###')

    # Open shop csv file with product data
    with open(file, newline='', encoding="utf8") as csvfile:

        # Define how csv should be read => Each element is seperated by comma (,) and enclosed by double quotes("")
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"', doublequote=True)

        # Holds the previous row of the csv file.
        # Necessary because elements are not all in one line, but over several lines.
        previous_row = []

        # Counts in which iteration we are.
        # Necessary, because of 2 reasons:
        # 1. In the 1. iteration the first line is read, which holds the product attributes.
        #    The product attributes for each shop are in different positions.
        #    For shop 1 the attribute "product-name" may appear as the 3rd element in the csv, but for shop 2 as the 6th
        #    Therefore, the attribute positions need to be defined in the first iteration.
        # 2. Because only the previous row is returned, there is no previous row in the 1. iteration.
        #    The earliest iteration that can return a row with all attributes is the 2nd
        #    (only if the 2nd row contains all elements).
        iteration = 0

        # Read csv line by line
        for row in spamreader:
            # General principle:
            #   > Check if the number of fields in this line is correct.
            #   > It will be less if any of this fields contained a line break.
            #   > this is the case append the next line to this one.

            # Check in which iteration (line read) we are
            if iteration >= 1:

                # In iteration 1 only shop rockanutrition is parsed differently,
                # because the rockanutrition scraper outputs each row in the csv file enclosed by quotest.
                # Example:
                #   > Rocka row: ""name","price",...,"url""
                #   > Other shop row: "name", "price",...,"url"
                if file == "../data/rockanutrition.csv":
                    # Remove commas inside quotes
                    row = re.sub(',(?=[^"]*"[^"]*(?:"[^"]*"[^"]*)*$)', ".", row[0])
                    row = row.split(',')

                # If iteration is greater than 1, there may be a row, which holds all attributes
                if iteration >= 2:

                    # Check if row holds all attributes or
                    # if the current row combined with previous rows holds all attributes
                    if len(previous_row) != 0 and len(previous_row) < fields_expected:
                        # => Current row or current row combined with previous row holds all attributes

                        # Number of elements that need to be added from current row to previous row
                        diff = fields_expected - len(previous_row)

                        # Create document with combined row that holds all attributes
                        create_document(previous_row.extend(row[:diff - 1]), attr_positions, current_shop, items)

                        # Only hold elements in row that were not given to previous row
                        row = row[diff:]

                    else:
                        # => Previous row length is either 0 or previous row contains all elements

                        # Create document with all attributes
                        create_document(previous_row, attr_positions, current_shop, items)

            elif iteration == 0:
                # Build attribute positions
                attr_positions = create_document_positions(row)
                # Fields expected count how many attributes we expect to be in one row of the csv file
                fields_expected = len(row)
                print("Created attribute positions" + str(attr_positions))

            # Increase iteration
            iteration += 1

            # Set previous row
            previous_row = row

        # Don't forget last row
        if len(previous_row) != 0 and len(previous_row) < fields_expected:
            # Number of elements that need to be added from current row to previous row
            diff = fields_expected - len(previous_row)
            # Create document with combined row that holds all attributes
            create_document(previous_row.extend(row[:diff - 1]), attr_positions, current_shop, items)
        else:
            # Create document with all attributes
            create_document(previous_row, attr_positions, current_shop, items)


# Creates positions where a certain model attribute can be found in a row
def create_document_positions(row):
    # Attribute positions to be filled.
    # Of the form: "product-url" : 4 , ...
    attr_positions = {}

    # i holds the positions for the attributes to be added
    i = 0

    # Iterate over first row
    for el in row:

        # Check if row attribute should be added
        if el in d.possible_column_names:
            # If yes then find the right attribute name which is required by the product model
            attr_positions[d.attribute_to_mongocol[el]] = i

        # Increase i
        i += 1

    # Return attribute positions
    return attr_positions


# Returns sid of current shop
def get_shop_id_and_popularity(current_shop):
    # Iterate over all shops
    for shop in shops.shops:
        # Check if shop name equals the current shop
        if shop['name'] == current_shop:
            # If yes, return sid
            return shop['sid'], shop['popularity']

    # If no shop fits, return none
    return None, None


# Returns list of cids of current item
def get_category_ids(item):
    # All categories the item is in
    all_categories = []

    # Iterate over all categories
    for category in categories.categories:

        # Iterate over all categories an item is in
        for cid in item['categories']:

            # Check if category name equals parsed category name of item
            if category['name'] == cid:
                # If yes, return cid
                all_categories.append(category['cid'])

    # Check if item is in category
    if len(all_categories) > 0:
        # Item is in category, return all categories its in
        return all_categories

    # If no category fits, return none
    return None


# Check if product with url or same name already exists
# If yes => Return this already existing item and true
# If no => Return param item and false
def check_if_item_exists(item, items, cids, row, attr_positions):
    # Set item found initially to false
    item_found = False

    # Iterate over all cid in cids the item is in
    for cid in cids:

        # Iterate over all items that have been parsed by now
        for i in items[cid]:

            # Check if the item name, which is parsed at this moment,
            # equals one of the item names in the list of items which have already been parsed
            if i['name'] == item['name']:
                # If yes => Return this already existing item and true

                # Replace item
                item = i

                # Set item found to true
                item_found = True

                # Return item and true
                return item_found, item

            # Iterate over shop urls of items that have been parsed
            for sid_to_url in i['urlsInShops']:

                # Check if shop url exists already, but the name differs.
                if sid_to_url['url'] == row[attr_positions['product-url']]:
                    # If yes => Return this already existing item and true

                    # Replace item
                    item = i

                    # Set item found to true
                    item_found = True

                    # Return item and true
                    return item_found, item
            else:
                # If no match continue searching
                continue

    # If no match in all parsed items, return param item and false
    return item_found, item


# Update existing item
def update_item(item, cids, sid, row, attr_positions):

    # Check if allergens is instance of string.
    # Necessary because append only if allergens is list of allergens.
    # If allergens is instance of string, then it is just an url with an img of the allergens.
    if not isinstance(item['allergens'], str):
        # Allergens is list of allergens => Append only new allergens to existing allergens
        item['allergens'] = \
            item['allergens'] + \
            list(
                set(ip.parse_allergens(row[attr_positions['product-allergens']], cids)) -
                set(item['allergens'])
            )

    # Find the longest match of the names of the already existing item and the name of the current item
    name_match = \
        SequenceMatcher(
            None,
            item['name'],
            ip.parse_name(row[attr_positions['product-name']])
        ).find_longest_match(
            0,
            len(item['name']),
            0,
            len(ip.parse_name(row[attr_positions['product-name']]))
        )

    # Set the name of the existing item to the longest match of both names
    item['name'] = item['name'][name_match.a: name_match.a + name_match.size]

    # Set the average bewertung to 0
    # TODO: Calculate real average bewertung once bewertungen are included into scraping
    item['averageBewertung'] = 0.0

    # Check if length of the description of the already existing item is shorter
    # than the length of the description of the current item.
    # Take the longer description.
    if (len(item['descriptionLong']) <
            len(ip.parse_description_long(row[attr_positions['product-description-long']]))):
        # Length of current item is longer => Set current item description to existing item description
        item['descriptionLong'] = ip.parse_description_long(row[attr_positions['product-description-long']])

    # Try if description short is not empty
    try:
        # Check if length of the description of the already existing item is shorter
        # than the length of the description of the current item.
        # Take the longer description.
        if (len(item['descriptionShort']) <
                len(ip.parse_description_short(row[attr_positions['product-description-short']]))):
            # Length of current item is longer => Set current item description to existing item description
            item['descriptionShort'] = ip.parse_description_short(row[attr_positions['product-description-short']])

    except KeyError:
        pass  # Leave description short empty

    # Check if nutrition string is img url.
    # If yes => Get back not parsed img url
    # If no => Get back parsed nutrition text.
    is_img, nutrition_str = ip.parse_nutrition(row[attr_positions['product-nutrition']])

    # Check if nutrition string is not img url.
    # If yes => Check if the length of the nutrition text of the already existing item is shorter
    # than the length of the text of the current item.
    # Replace existing text only, if the text of the current item is longer than the old text.
    if not is_img and (len(item['nutritionText']) < len(nutrition_str)):
        # Length of current item text is longer => Set text to current item text
        item['nutritionText'] = nutrition_str

    # Assign the minimum price of the already exiting item and the current item to min price
    item['minPrice'] = min(ip.parse_price(row[attr_positions['product-price']]), item['minPrice'])

    # Try if attribute "product-size" is a valid size
    # If yes => set the min size.
    # If no => try to get the size from name
    # TODO: Calculate minimum of sizes of already existing item and current item
    # TODO: Catch errors in except case. Okay as long as script runs without failures
    try:
        # Set min size
        item['minSize'] = ip.parse_size(row[attr_positions['product-size']])
    except KeyError:
        # Get size from name
        item['minSize'] = ip.parse_size_from_name(row[attr_positions['product-name']])

    # Iterate over all cid in cids the item is in
    for cid in cids:
        # Check if cid does not exist in categories of already existing item
        if cid not in item['categories']:
            # Cid does not exist in already existing item

            # Append cid to category list of already existing item
            item['categories'].append(cid)

    # Check, if parsed flavour of current item is not contained in flavour list of already existing item.
    # Check also, if the parsed flavour is not None.
    if ip.parse_flavour(row[attr_positions['product-flavour']]) not in item['flavours'] \
            and ip.parse_flavour(row[attr_positions['product-flavour']]) is not None:
        # New flavour detected => Append to existing flavours
        item['flavours'].append(ip.parse_flavour(row[attr_positions['product-flavour']]))

    # Check if current shop of item does not exist in shop list of already existing item
    if sid not in item['shops']:
        # Shop does not exist in already existing item

        # Append shop id to shop list of already existing item
        item['shops'].append(sid)
        # Append price and shop id to prices in shops of already existing item
        item['pricesInShops'].append({'sid': sid, 'price': ip.parse_price(row[attr_positions['product-price']])})
        # Append product url and shop id to prices in shops of already existing item
        item['urlsInShops'].append({'sid': sid, 'url': ip.parse_url(row[attr_positions['product-url']])})
        # Parse flavours and append flavours list and shop id to flavours in shops property
        item['flavoursInShops'].append({'sid': sid,
                                        'flavours': [ip.parse_flavour(row[attr_positions['product-flavour']])]})
    else:
        # Shop exists in already existing item

        # Find current shop flavours
        for shop_flavour in item['flavoursInShops']:
            if shop_flavour['sid'] == sid:

                # Check, if parsed flavour of current item is not contained in flavour list of already existing item.
                # Check also, if the parsed flavour is not None.
                if ip.parse_flavour(row[attr_positions['product-flavour']]) not in shop_flavour['flavours'] \
                        and ip.parse_flavour(row[attr_positions['product-flavour']]) is not None:
                    # New flavour detected => Append to existing flavours
                    shop_flavour['flavours'].append(ip.parse_flavour(row[attr_positions['product-flavour']]))


# Insert new item into items
def insert_item(item, items, cids, sid, current_shop, row, attr_positions, popularity):

    # Parse allergens and set to allergens property
    item['allergens'] = ip.parse_allergens(row[attr_positions['product-allergens']], cids)

    # Parse description long and set to description long property
    item['descriptionLong'] = ip.parse_description_long(row[attr_positions['product-description-long']])

    # Try if description short has been scraped
    try:
        # Description short has been scraped => Parse description short and set description short property
        item['descriptionShort'] = ip.parse_description_short(row[attr_positions['product-description-short']])
    except KeyError:
        pass  # Leave description short empty

    # Parse flavours and set to flavours property
    item['flavours'].append(ip.parse_flavour(row[attr_positions['product-flavour']]))

    # Check if current shop is zecplus
    # Necessary, because zecplus img urls are relative
    if current_shop == 'Zec+':
        # Current shop is zecplus => Prefix zecplus url
        item['img'] = 'https://www.zecplus.de/' + ip.parse_img(row[attr_positions['product-img']])

    else:
        # Current shop is not zecplus => Just set img property
        item['img'] = ip.parse_img(row[attr_positions['product-img']])

    # Check if nutrition string is img url.
    # If yes => Get back nutrition img url not parsed.
    # If no => Get back nutrition text parsed.
    is_img, nutrition_str = ip.parse_nutrition(row[attr_positions['product-nutrition']])

    # Check if nutrition is img url
    if is_img:
        # Nutrition is img url => Set nutrition img property
        item['nutritionImg'] = nutrition_str
    else:
        # Nutrition is is text => Set nutrition text property
        item['nutritionText'] = nutrition_str

    # Parse price and set as min price property
    item['minPrice'] = ip.parse_price(row[attr_positions['product-price']])

    # Try if attribute "product-size" is a valid size
    # If yes => set the min size.
    # If no => try to get the size from name
    try:
        # Parse and set min size property
        item['minSize'] = ip.parse_size(row[attr_positions['product-size']])
    except KeyError:
        # Get size from name
        item['minSize'] = ip.parse_size_from_name(row[attr_positions['product-name']])

    # Set item popularity by default to 1
    # TODO: Calculate item popularity based on:
    #  1. If affiliate program available and
    #  2. How often a product has been bought
    # TODO: Insert most popular items into category "Beliebteste"
    item['popularity'] = popularity

    # Append current category if to categories property
    item['categories'] = cids

    # Append current shop id to shops property
    item['shops'].append(sid)

    # Append price in shop id to prices in shops property
    item['pricesInShops'].append({'sid': sid, 'price': ip.parse_price(row[attr_positions['product-price']])})

    # Append product url in shop id ito urls in shops property
    item['urlsInShops'].append({'sid': sid, 'url': ip.parse_url(row[attr_positions['product-url']])})

    # Parse flavours and append flavours list and shop id to flavours in shops property
    item['flavoursInShops'].append({'sid': sid, 'flavours': [ip.parse_flavour(row[attr_positions['product-flavour']])]})

    # Iterate over all cid in cids to append item to every category its in
    for cid in cids:
        # Add item to products
        items[cid].append(item)

    # Append to most popular items
    global max_popular
    # 1. Insert into c1001
    items['c1001'].append(item)
    # 2. Sort c1001 by item popularity
    items['c1001'] = sorted(items['c1001'], key=lambda k: k['popularity'], reverse=True)
    # 3. Check if length is greater than max popular
    if len(items['c1001']) > max_popular:
        # 4. Remove last item
        del items['c1001'][-1]


# Creates item which will be inserted into items dictionary
def create_document(row, attr_positions, current_shop, items):

    # Item schema
    item = {'iid': '', 'name': '', 'allergens': [], 'averageBewertung': 0.0, 'descriptionLong': '',
            'descriptionShort': '', 'flavours': [], 'img': '', 'nutritionImg': '', 'nutritionText': '', 'minPrice': '',
            'minSize': '', 'popularity': 1, 'shops': [], 'categories': [], 'bewertungen': [], 'pricesInShops': [],
            'urlsInShops': [], 'flavoursInShops': []}

    # 1. Get shop id of current shop
    sid, popularity = get_shop_id_and_popularity(current_shop)

    # 2. Get item name from row
    item['name'] = ip.parse_name(row[attr_positions['product-name']])

    # 3. Get item category from row
    item['categories'], dont_upload = ip.parse_category(item['name'], current_shop,
                                                        row[attr_positions['product-category']])
    if len(item['categories']) > 1:
        print(item['categories'])

    # 4. Check if item shouldn't be uploaded.
    #    This is determined in the item parser for category.
    if dont_upload:
        # Return if there are categories that shouldn't be uploaded
        return

    # 5. Get category id
    cids = get_category_ids(item)

    # 6. Check if product with url or same name already exists
    item_found, item = check_if_item_exists(item, items, cids, row, attr_positions)

    # 7. Check if another version of the item was parsed previously
    if item_found:

        # 8. item exists in items => only update certain fields
        update_item(item, cids, sid, row, attr_positions)

    else:
        # 9. item doenn't exist in items => insert new item in items
        insert_item(item, items, cids, sid, current_shop, row, attr_positions, popularity)

    # 10. Print out created document
    print("Created document: " + str(item))
