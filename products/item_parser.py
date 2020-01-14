#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from products import category_parser as sp, items as d


def parse_name(name: str):
    # For exceptions the number match is not executed because the number is part of the product name
    exceptions = [
        'Weider\n Protein 80 Plus',
        'Weider\n Soy 80+ Protein'
    ]

    # Name matching
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
        'Smacktastic Ice Cream'
    ]

    number_pattern = re.compile(r'(\b\d+(?:[\.,]\d+)?\b(?!(?:[\.,]\d+)|(?:\s*(?:%|percent))))')

    # Parse out linebreaks
    name = re.sub("/\r?\n|\r/", "", name)
    name = re.sub('"', '', name)

    # Parse out flavours
    for n in names:
        if n in name:
            name = n
            break

    # Match numbers in name and remove everything after that number
    if name not in exceptions and number_pattern.search(name):
        sep = number_pattern.search(name).group(0)
        name = name.split(sep, 1)[0]

    return name


def parse_allergens(allergen_string: str):
    allergens = []
    url_pattern = re.compile(r'/((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|'
                             r'(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w\-_]*)?\??'
                             r'(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/')

    # Parse out linebreaks
    allergen_string = re.sub('/\r?\n|\r/', "", allergen_string)
    allergen_string = re.sub('"', '', allergen_string)

    # Allergen string to lower for matching allergen categories
    allergen_string = allergen_string.lower()

    # Check if allergens are in an image whose path is given by an url
    if url_pattern.match(allergen_string):
        # Allergens are image
        return allergen_string
    else:
        # Allergens are string
        if 'ei' in allergen_string:
            allergens.append('Ei')
        elif 'erdn' in allergen_string:
            allergens.append('Erdnüsse')
        elif 'fisch' in allergen_string:
            allergens.append('Fisch')
        elif 'gluten' in allergen_string:
            allergens.append('Gluten')
        elif 'krebs' in allergen_string:
            allergens.append('Krebstiere')
        elif 'lupine' in allergen_string:
            allergens.append('Lupine')
        elif 'milch' in allergen_string:
            allergens.append('Milch')
        elif 'schalenfr' in allergen_string:
            allergens.append('Schalenfrüchte')
        elif 'schwefel' in allergen_string:
            allergens.append('Schwefeloxid')
        elif 'sellerie' in allergen_string:
            allergens.append('Sellerie')
        elif 'senf' in allergen_string:
            allergens.append('Senf')
        elif 'sesam' in allergen_string:
            allergens.append('Sesam')
        elif 'soja' in allergen_string:
            allergens.append('Soja')
        elif 'weichtier' in allergen_string:
            allergens.append('Weichtiere')

        return allergens


def parse_averageBewertung(bewertung: str):
    # Parse out linebreaks
    bewertung = re.sub("/\r?\n|\r/", "", bewertung)
    bewertung = re.sub('"', '', bewertung)

    # TODO: Check all bewertungen for product iid  and calculate the average of it between 0-5
    return float(bewertung)


def parse_description_long(desc_long: str):
    # Parse out linebreaks
    desc_long = re.sub("/\r?\n|\r/", "", desc_long)
    return re.sub('"', '', desc_long)


def parse_description_short(desc_short: str):
    # Parse out linebreaks
    desc_short = re.sub("/\r?\n|\r/", "", desc_short)
    return re.sub('"', '', desc_short)


def parse_flavour(flavour: str):
    # Parse out linebreaks
    flavour = re.sub("/\r?\n|\r/", "", flavour)
    return [re.sub('"', '', flavour)]


def parse_img(img: str):
    # Parse out linebreaks
    img = re.sub("/\r?\n|\r/", "", img)
    return re.sub('"', '', img)


# Returns true if nutrition is an image. If plain text, return false.
def parse_nutrition(nutrition_string):
    url_pattern = re.compile(r'/((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|'
                             r'(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w\-_]*)?\??'
                             r'(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/')

    # Check if nutrition is in an image whose path is given by an url
    if url_pattern.match(nutrition_string):
        # Nutrition is image
        return True

    # Nutrition is no image
    return False


def parse_price(price: str):
    price_pattern = re.compile(r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})')
    res = price_pattern.search(price)
    if res:
        return float(res.group(0).replace(',', '.'))
    return ''


def parse_size(size: str):
    # Return everything before line break
    return size.split('\n', 1)[0]


def parse_size_from_name(name: str):
    number_pattern = re.compile(r'(\b\d+(?:[\.,]\d+)?\b(?!(?:[\.,]\d+)|(?:\s*(?:%|percent))))')

    # Parse out linebreaks
    name = re.sub("/\r?\n|\r/", "", name)
    name = re.sub('"', '', name)

    # Match numbers in name and remove everything before that number
    if number_pattern.search(name):
        sep = number_pattern.search(name).group(0)
        return name.split(sep)[0]

    # Return empty size else
    return ''


def parse_category(product_name: str, current_shop: str, category: str):
    # Exceptions that will be ignored for upload
    exceptions = [
        'dlg-prämiert',
        'post-workout'
    ]

    # Parse out linebreaks
    category = re.sub("/\r?\n|\r/", "", category)
    category = re.sub('"', '', category)

    replaced_category = None
    if category.lower() in exceptions:
        return '', replaced_category, True
    elif category.lower() in d.category_matching[current_shop].keys():
        replaced_category = category.lower()
        return d.category_matching[current_shop][category.lower()], replaced_category, False
    else:
        if current_shop == 'Rockanutrition':
            category = sp.parse_rocka(category, product_name)
        elif current_shop == 'fitmart':
            category = sp.parse_fitmart(category, product_name)
        elif current_shop == 'Myprotein':
            category = sp.parse_myprotein(category, product_name)
        elif current_shop == "Zec+":
            category = sp.parse_zecplus(category, product_name)
        elif current_shop == "Weider":
            category = sp.parse_weider(category, product_name)

        return category, replaced_category, False
