#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from products import category_parser as sp, items as d


# Parse item name.
# Remove numbers, weights and special characters from name.
# Remove numbers from names which are not defined in exceptions
# Replace name with name in array names, if defined
# Returns item name as string
def parse_name(name: str):
    # For exceptions the number match is not executed because the number is part of the product name
    exceptions = [
        'Weider\n Protein 80 Plus',
        'Weider\n Soy 80+ Protein',
        'GOT7',
        'NO2'
    ]

    # If n in names is part of the name to parse => Replace name to parse with n
    names = [
        'Rocka Whey Isolate',
        'Yum Yum Whey',
        'Rocka Milk',
        'The Vegan',
        'Yum Yum EAA',
        'Over the Top',
        'Pink Power',
        'Play Hard Pump Booster',
        'Work Hard Mind Booster',
        'Alina\'s Pink Essentials',
        'Smacktastic Flav Powder',
        'Smacktastic 2GO',
        'Smacktastic Cream',
        'Sauce Zero',
        'Rocka Milk Shake',
        'Swish',
        'Juicy Whey',
        'Rockalicious',
        'Light Chips',
        'Slim Sin',
        'Smacktastic Syrup',
        'Smacktastic Ice Cream',
        'Clean Concentrate'
    ]

    # Regex to match numbers in name
    number_pattern = re.compile(r'(\b\d+(?:[\.,]\d+)?\b(?!(?:[\.,]\d+)|(?:\s*(?:%|percent))))')
    # Regex to match weights in name
    weight_pattern = re.compile(r'(\d*\.?\d+)\s?(\w+)')

    # Parse out linebreaks
    name = re.sub("/\r?\n|\r/", "", name)
    # Parse out \"
    name = re.sub('"', '', name)

    # Replace name with n in names, if n is part of name
    for n in names:
        if n.lower() in name.lower():
            name = n
            break

    # Check if name is not defined in exception
    found_exception = False
    for exc in exceptions:
        if exc in name:
            found_exception = True
            break

    # Match numbers in name and remove everything after that number
    # Only if name is not defined in exception
    if not found_exception and number_pattern.search(name):
        sep = number_pattern.search(name).group(0)
        name = name.split(sep, 1)[0]
    # Match weights in name and remove everything after that weight
    # Only if name is not defined in exception
    elif not found_exception and weight_pattern.search(name):
        sep = weight_pattern.search(name).group(0)
        name = name.split(sep, 1)[0]

    # Remove special characters in name
    name = re.sub(r"[!@#$,;.:|><§&/()=?}{~*'\-]", "", name)

    # Return parsed name
    return name


# Parse allergens from allergen string.
# Checks if allergen is url.
# If yes => Return that url right back as string.
# If no => Check if allergens are in that nutrition string and return list of found allergens.
def parse_allergens(allergen_string: str, cid: str):
    # Validator that checks if allergen string is a valid url
    val = URLValidator()

    # Parse out linebreaks
    allergen_string = re.sub('/\r?\n|\r/', "", allergen_string)
    # Parse out \"
    allergen_string = re.sub('"', '', allergen_string)

    # Allergen string to lower for matching allergen categories and shopify string
    allergen_string = allergen_string.lower()

    # Check if allergen string is shopify image url.
    # Shopify urls are not recognized by url validator.
    if 'shopify' in allergen_string:
        return allergen_string

    # Check if allergens are in an image whose path is given by an url
    try:
        # => Allergen string is an img url
        val(allergen_string)
        # Return img url right back
        return allergen_string
    except ValidationError:
        # => Allergen string is no img url, but a nutrition text

        # Array of found allergens to be returned
        allergens = []

        # Check which of the allergens are in allergen string
        if 'ei ' in allergen_string or cid in ['c2012']:
            # Products in category eiproteine all have allergen ei
            allergens.append('Ei')
        if 'erdn' in allergen_string:
            allergens.append('Erdnüsse')
        if 'fisch' in allergen_string:
            allergens.append('Fisch')
        if 'gluten' in allergen_string or 'weiz' in allergen_string or 'hafer' in allergen_string:
            allergens.append('Gluten')
        if 'krebs' in allergen_string:
            allergens.append('Krebstiere')
        if 'lupine' in allergen_string:
            allergens.append('Lupine')
        if 'milch' in allergen_string or 'molke' in allergen_string or 'laktos' in allergen_string \
                or 'lactos' in allergen_string or cid in ['c2002', 'c2003', 'c2004']:
            # Products in category milchproteine all have allergen milk
            allergens.append('Milch')
        if 'schalenfr' in allergen_string:
            allergens.append('Schalenfrüchte')
        if 'schwefel' in allergen_string:
            allergens.append('Schwefeloxid')
        if 'sellerie' in allergen_string:
            allergens.append('Sellerie')
        if 'senf' in allergen_string:
            allergens.append('Senf')
        if 'sesam' in allergen_string:
            allergens.append('Sesam')
        if 'soja' in allergen_string or cid in ['c2006']:
            # Products in category sojaproteine all have allergen soja
            allergens.append('Soja')
        if 'weichtier' in allergen_string:
            allergens.append('Weichtiere')

        # Return found allergens
        return allergens


# TODO: Check all bewertungen for product iid  and calculate the average of it between 0-5
def parse_averageBewertung(bewertung: str):
    # Parse out linebreaks
    bewertung = re.sub("/\r?\n|\r/", "", bewertung)
    bewertung = re.sub('"', '', bewertung)

    # For now: Just return default bewertung 0
    return float(bewertung)


# Parse description long.
# Leave it as it is and just remove linebreaks and \"
def parse_description_long(desc_long: str):
    # Parse out linebreaks
    desc_long = re.sub("/\r?\n|\r/", "", desc_long)
    return re.sub('"', '', desc_long)


# Parse description short.
# Leave it as it is and just remove linebreaks and \"
def parse_description_short(desc_short: str):
    # Parse out linebreaks
    desc_short = re.sub("/\r?\n|\r/", "", desc_short)
    return re.sub('"', '', desc_short)


# Parse item flavour.
# Removes numbers and special characters from flavour in order to prevent cases like: "Vanilla | 908g Dose"
# Summarizes similar flavours like: "Vanilla", "Vanille" and "Vanilla Flavour" ==> "Vanille"
def parse_flavour(flavour: str):
    # Parse out linebreaks
    flavour = re.sub("/\r?\n|\r/", "", flavour)
    # Parse out \"
    flavour = re.sub('"', '', flavour)

    # Regex to detect numbers
    number_pattern = re.compile(r'(\b\d+(?:[\.,]\d+)?\b(?!(?:[\.,]\d+)|(?:\s*(?:%|percent))))')

    # Remove everything after numbers from flavour
    if number_pattern.search(flavour):
        sep = number_pattern.search(flavour).group(0)
        flavour = flavour.split(sep, 1)[0]

    # Remove special characters
    # Save in new variable old_flavour in case of no matching
    old_flavour = re.sub(r"[!@#$,;.:|><§&/()=?}{~*'\-]", "", flavour).strip()

    # Use flavour variable to check for flavours that can be summarized
    flavour = old_flavour.lower()

    # Summarize similar flavours
    if 'ananas' == flavour or ('ananas' in flavour and 'carnitin' in flavour):
        return 'Ananas'
    elif 'apfel' == flavour:
        return 'Apfel'
    elif 'banana' == flavour or 'banane' == flavour or ('natürlich' in flavour and 'banan' in flavour) \
            or ('banan' in flavour and 'classic' in flavour):
        return 'Banane'
    elif 'banan' in flavour and 'split' in flavour:
        return 'Banana Split'
    elif 'blutorange' == flavour or ('blood' in flavour and 'orange' in flavour):
        return 'Blutorange'
    elif ('butter' in flavour and 'keks' in flavour) or ('butter' in flavour and 'biscuit' in flavour) \
            or ('butter' in flavour and 'cookie' in flavour):
        return 'Butterkeks'
    elif 'cappuccino' in flavour:
        return 'Cappuccino'
    elif 'caramel' == flavour or 'Karamell' == flavour:
        return 'Karamell'
    elif 'cheesecake' == flavour or 'käsekuchen' == flavour:
        return 'Käsekuchen'
    elif 'chocolate' == flavour or ('chocolate' in flavour and 'classic' in flavour) \
            or ('chocolate' in flavour and 'flavour' in flavour) or ('schokolad' in flavour and 'natürlich' in flavour) \
            or 'schoko' == flavour or 'schokolade' == flavour or ('schoko' in flavour and 'dose' in flavour):
        return 'Schokolade'
    elif 'chocolate' in flavour and 'coconut' in flavour:
        return 'Chocolate Coconut'
    elif ('chocolate' in flavour and 'dark' in flavour) or ('schokolade' in flavour and 'dunk' in flavour):
        return 'Dunkle Schokolade'
    elif ('chocolate' in flavour and 'hazelnut' in flavour) or ('schokolade' in flavour and 'haseln' in flavour):
        return 'Schokolade Haselnuss'
    elif 'cola' == flavour:
        return 'Cola'
    elif 'cookie' in flavour and 'cre' in flavour:
        return 'Cookies and Cream'
    elif ('double' in flavour and 'choc' in flavour) or ('doppel' in flavour and 'schoko' in flavour):
        return 'Doppel Schokolade'
    elif 'erdbeere' in flavour or ('erdbeer' in flavour and 'dose' in flavour) \
            or ('erdbeer' in flavour and 'natürlich' in flavour) or 'strawberry' == flavour \
            or ('strawberry' in flavour and 'classic' in flavour) \
            or ('strawberry' in flavour and 'very' in flavour):
        return 'Erdbeere'
    elif ('erdn' in flavour and 'butter' in flavour) or ('peanut' in flavour and 'butter' in flavour):
        return 'Erdnussbutter'
    elif 'hazelnut' == flavour or ('hazelnut' in flavour and 'crunch' in flavour):
        return 'Haselnuss'
    elif 'himbeer' == flavour or 'himbeere' == flavour or 'raspberry' == flavour or 'rocka raspberry' == flavour \
            or ('himbeer' in flavour and 'carni' in flavour):
        return 'Himbeere'
    elif 'honey' == flavour or 'honig' == flavour:
        return 'Honig'
    elif 'kirsch' == flavour or 'kirsche' == flavour or 'cherry' == flavour \
            or ('cherry' in flavour and 'very' in flavour):
        return 'Kirsche'
    elif 'kokos' == flavour or 'cocos' == flavour or 'kokosnuss' == flavour:
        return 'Kokos'
    elif 'latte' in flavour:
        return 'Cafe Latte'
    elif 'lemon' in flavour and 'lime' in flavour:
        return 'Lemon and Lime'
    elif ('milch' in flavour and 'schokolade' in flavour) or ('milk' in flavour and 'chocolate' in flavour):
        return 'Milchschokolade'
    elif 'mango' in flavour and 'maracuja' in flavour:
        return 'Mango Maracuja'
    elif 'naturell' in flavour or 'neutral' in flavour:
        return 'Geschmacksneutral'
    elif ('nut' in flavour and 'mix' in flavour) or ('nuss' in flavour and 'mix' in flavour):
        return 'Nuss-Mix'
    elif ('spaghetti' in flavour and 'eis' in flavour) or ('spaghetti' in flavour and 'ice' in flavour):
        return 'Spaghetti Eis'
    elif 'original' == flavour or ('original' in flavour and 'cremig' in flavour) \
            or ('original' in flavour and 'grob' in flavour):
        return 'Orginial'
    elif 'vanilla' == flavour or ('vanill' in flavour and 'classic' in flavour) or 'vanille' == flavour \
            or ('vanill' in flavour and 'dose' in flavour):
        return 'Vanille'
    elif 'vanill' in flavour and 'cre' in flavour:
        return 'Vanille Cream'
    elif ('chocolate' in flavour and 'white' in flavour) or ('weiß' in flavour and 'schokolade' in flavour):
        return 'Weiße Schokolade'

    # Remove the following flavours from flavours
    elif 'geschmack' == flavour or 'cremig' == flavour or 'crunchy' == flavour or 'duo' == flavour \
            or 'super crunch' == flavour:
        return None

    # Return old flavour in case of no matching
    else:
        return old_flavour


# Parse product img.
# Leave it as it is and just remove linebreaks and \"
def parse_img(img: str):
    # Parse out linebreaks
    img = re.sub("/\r?\n|\r/", "", img)
    return re.sub('"', '', img)


# Parse product nutrition.
# Returns true if nutrition is an image.
# Return false, if nutrition is plain text.
# Removes linebreaks and \"
def parse_nutrition(nutrition_string):
    # Validator that checks if allergen string is a valid url
    val = URLValidator()

    # Remove linebreaks
    nutrition_string = re.sub("/\r?\n|\r/", "", nutrition_string)
    # Remove \"
    nutrition_string = re.sub('"', '', nutrition_string)

    # Check if nutrition is shopify image.
    # This is not being recognized by url validator.
    if 'shopify' in nutrition_string:
        return True, nutrition_string

    # Check if nutrition is in an image whose path is given by an url
    try:
        # Nutrition is image
        val(nutrition_string)
        # Return true and nutrition string
        return True, nutrition_string
    except ValidationError:
        # Nutrition is no image
        # Return false and nutrition string
        return False, nutrition_string


# Parse product price.
# Finds any price pattern in price string.
# Returns price as float.
# E.g. price="Price is today 4,99€" is transformed to price=4.99
def parse_price(price: str):
    # Regex to recognize prices without currency
    price_pattern = re.compile(r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})')

    # Find price pattern anywhere in the string
    res = price_pattern.search(price)
    if res:
        # Return found price as float
        return float(res.group(0).replace(',', '.'))

    # Return empty price if no matching was found
    return ''


# Parse product size.
# Return everything before first linebreak in size.
def parse_size(size: str):
    # Return everything before line break
    return size.split('\n', 1)[0]


# Parses size from name.
# Some products hold their size in the product name like: "Whey Perfection | 700g".
# It finds these sizes and returns the size.
# The example above returns "700g"
def parse_size_from_name(name: str):
    # Regex to match numbers in name
    number_pattern = re.compile(r'(\b\d+(?:[\.,]\d+)?\b(?!(?:[\.,]\d+)|(?:\s*(?:%|percent))))')

    # Parse out linebreaks
    name = re.sub("/\r?\n|\r/", "", name)
    # Parse out \"
    name = re.sub('"', '', name)

    # Match numbers in name and remove everything before that number
    if number_pattern.search(name):
        sep = number_pattern.search(name).group(0)
        # Return found size
        return name.split(sep)[0]

    # Return empty size else
    return ''


# Parse product category.
# Matches mister m categories with categories from parsed shops.
def parse_category(product_name: str, current_shop: str, category: str):
    # Exceptions that will be ignored for upload
    exceptions = [
        'dlg-prämiert',
        'post-workout',
        'post workout',
        'intra-workout'
    ]

    # Exceptions only checked for fitmart shop.
    # They will be ignored for upload.
    # TODO: Remove in future versions, if the webscraper is fixed to not scrape these categories anymore.
    fitmart_exceptions = [
        'intra-workout',
        'pre-workout',
        'gewichtsreduktion spezial',
        'müsli-zutaten',
        'pulver',
        'spezial',
        'tribulus terrestris',
        'maca',
        'asparaginsäure'
    ]

    # Parse out linebreaks
    category = re.sub("/\r?\n|\r/", "", category)
    # Parse out \"
    category = re.sub('"', '', category)

    # Check if category should be matched
    if category.lower() in exceptions or (category.lower() in fitmart_exceptions and current_shop == 'Fitmart')\
            or product_name.lower() == 'null' or (product_name == '') or \
            ('bundle' in product_name.lower()):
        # Category should not be matched
        return '',  True

    # Check if default category can be returned.
    # E.g. if param category is "Whey Protein" than the param category can be returned as it is,
    # because the category itself matches the mister m category.
    # The plain category matchings are defined in category_matching array
    elif category.lower() in d.category_matching[current_shop].keys():
        # Category can be returned as it is
        return d.category_matching[current_shop][category.lower()], False

    # Find the right category based on the product name and the current shop.
    # Each matching uses a unique parser for the current shop.
    else:
        if current_shop == 'Rockanutrition':
            category = sp.parse_rocka(category, product_name)
        elif current_shop == 'Fitmart':
            category = sp.parse_fitmart(category, product_name)
        elif current_shop == 'Myprotein':
            category = sp.parse_myprotein(category, product_name)
        elif current_shop == "Zec+":
            category = sp.parse_zecplus(category, product_name)
        elif current_shop == "Weider":
            category = sp.parse_weider(category, product_name)

        # Return matched category based on product name and current shop
        return category, False


# Parse product url.
# Leave it as it is and just remove linebreaks and \"
def parse_url(url: str):
    # Parse out linebreaks
    url = re.sub("/\r?\n|\r/", "", url)
    return re.sub('"', '', url)
