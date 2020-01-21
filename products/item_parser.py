#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from products import category_parser as sp, items as d


def parse_name(name: str):
    # For exceptions the number match is not executed because the number is part of the product name
    exceptions = [
        'Weider\n Protein 80 Plus',
        'Weider\n Soy 80+ Protein',
        'GOT7',
        'NO2'
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
        'Smacktastic Ice Cream',
        'Clean Concentrate'
    ]

    number_pattern = re.compile(r'(\b\d+(?:[\.,]\d+)?\b(?!(?:[\.,]\d+)|(?:\s*(?:%|percent))))')
    weight_pattern = re.compile(r'(\d*\.?\d+)\s?(\w+)')

    # Parse out linebreaks
    name = re.sub("/\r?\n|\r/", "", name)
    name = re.sub('"', '', name)

    # Parse out flavours
    for n in names:
        if n.lower() in name.lower():
            name = n
            break

    # Match numbers in name and remove everything after that number
    found_exception = False
    for exc in exceptions:
        if exc in name:
            found_exception = True
            break

    if not found_exception and number_pattern.search(name):
        sep = number_pattern.search(name).group(0)
        name = name.split(sep, 1)[0]
    elif not found_exception and weight_pattern.search(name):
        sep = weight_pattern.search(name).group(0)
        name = name.split(sep, 1)[0]

    # Remove sonderzeichen
    name = re.sub(r"[!@#$,;.:|><§&/()=?}{~*'\-]", "", name)
    return name


def parse_allergens(allergen_string: str):
    allergens = []

    val = URLValidator()

    # Parse out linebreaks
    allergen_string = re.sub('/\r?\n|\r/', "", allergen_string)
    allergen_string = re.sub('"', '', allergen_string)

    # Allergen string to lower for matching allergen categories
    allergen_string = allergen_string.lower()

    # Check if nutrition is shopify image. This is not being recognized by url validator.
    if 'shopify' in allergen_string:
        return allergen_string

    # Check if allergens are in an image whose path is given by an url
    try:
        val(allergen_string)
        # Allergens are image
        return allergen_string
    except ValidationError:
        # Allergens are string
        if 'ei' in allergen_string:
            allergens.append('Ei')
        if 'erdn' in allergen_string:
            allergens.append('Erdnüsse')
        if 'fisch' in allergen_string:
            allergens.append('Fisch')
        if 'gluten' in allergen_string:
            allergens.append('Gluten')
        if 'krebs' in allergen_string:
            allergens.append('Krebstiere')
        if 'lupine' in allergen_string:
            allergens.append('Lupine')
        if 'milch' in allergen_string:
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
        if 'soja' in allergen_string:
            allergens.append('Soja')
        if 'weichtier' in allergen_string:
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
    flavour = re.sub('"', '', flavour)

    number_pattern = re.compile(r'(\b\d+(?:[\.,]\d+)?\b(?!(?:[\.,]\d+)|(?:\s*(?:%|percent))))')

    # Remove everything after numbers from flavour
    if number_pattern.search(flavour):
        sep = number_pattern.search(flavour).group(0)
        flavour = flavour.split(sep, 1)[0]

    # Remove sonderzeichen
    old_flavour = re.sub(r"[!@#$,;.:|><§&/()=?}{~*'\-]", "", flavour).strip()

    flavour = old_flavour.lower()

    # Summarize similar flavours
    if 'banana' == flavour or 'banane' == flavour or ('natürlich' in flavour and 'banan' in flavour) \
            or ('banan' in flavour and 'classic' in flavour):
        return 'Banane'
    elif 'banan' in flavour and 'split' in flavour:
        return 'Banana Split'
    elif 'chocolate' == flavour or ('chocolate' in flavour and 'classic' in flavour) \
            or ('chocolate' in flavour and 'flavour' in flavour) or ('schokolad' in flavour and 'natürlich' in flavour) \
            or 'schoko' == flavour or 'schokolade' == flavour or ('schoko' in flavour and 'dose' in flavour):
        return 'Schokolade'
    elif 'chocolate' in flavour and 'coconut' in flavour:
        return 'Chocolate Coconut'
    elif 'cookie' in flavour and 'cre' in flavour:
        return 'Cookies and Cream'
    elif 'erdbeere' in flavour or ('erdbeer' in flavour and 'dose' in flavour) \
            or ('erdbeer' in flavour and 'natürlich' in flavour) or 'strawberry' == flavour \
            or ('strawberry' in flavour and 'classic' in flavour) \
            or ('strawberry' in flavour and 'very' in flavour):
        return 'Erdbeere'
    elif 'kirsch' == flavour or 'kirsche' == flavour or 'cherry' == flavour \
            or ('cherry' in flavour and 'very' in flavour):
        return 'Kirsche'
    elif 'kokos' == flavour or 'cocos' == flavour or 'kokosnuss' == flavour:
        return 'Kokos'
    elif ('milch' in flavour and 'schokolade' in flavour) or ('milk' in flavour and 'chocolate' in flavour):
        return 'Milchschokolade'
    elif 'naturell' in flavour or 'neutral' in flavour:
        return 'Geschmacksneutral'
    elif ('nut' in flavour and 'mix' in flavour) or ('nuss' in flavour and 'mix' in flavour):
        return 'Nuss-Mix'
    elif ('erdn' in flavour and 'butter' in flavour) or ('peanut' in flavour and 'butter' in flavour):
        return 'Erdnussbutter'
    elif ('spaghetti' in flavour and 'eis' in flavour) or ('spaghetti' in flavour and 'ice' in flavour):
        return 'Spaghetti Eis'
    elif 'himbeer' == flavour or 'himbeere' == flavour or 'raspberry' == flavour or 'rocka raspberry' == flavour \
            or ('himbeer' in flavour and 'carni' in flavour):
        return 'Himbeere'
    elif 'vanilla' == flavour or ('vanill' in flavour and 'classic' in flavour) or 'vanille' == flavour \
            or ('vanill' in flavour and 'dose' in flavour):
        return 'Vanille'
    elif 'vanill' in flavour and 'cre' in flavour:
        return 'Vanille Cream'
    elif ('chocolate' in flavour and 'white' in flavour) or ('weiß' in flavour and 'schokolade' in flavour):
        return 'Weiße Schokolade'
    elif 'honey' == flavour or 'honig' == flavour:
        return 'Honig'
    elif ('double' in flavour and 'choc' in flavour) or ('doppel' in flavour and 'schoko' in flavour):
        return 'Doppel Schokolade'
    elif ('chocolate' in flavour and 'dark' in flavour) or ('schokolade' in flavour and 'dunk' in flavour):
        return 'Dunkle Schokolade'
    elif 'cappuccino' in flavour:
        return 'Cappuccino'
    elif 'geschmack' == flavour or 'cremig' == flavour or 'crunchy' == flavour or 'duo' == flavour \
            or 'super crunch' == flavour:
        return old_flavour
    elif 'latte' in flavour:
        return 'Cafe Latte'
    elif 'lemon' in flavour and 'lime' in flavour:
        return 'Lemon and Lime'
    elif ('chocolate' in flavour and 'hazelnut' in flavour) or ('schokolade' in flavour and 'haseln' in flavour):
        return 'Schokolade Haselnuss'
    elif 'hazelnut' == flavour or ('hazelnut' in flavour and 'crunch' in flavour):
        return 'Haselnuss'
    elif 'original' == flavour or ('original' in flavour and 'cremig' in flavour) \
            or ('original' in flavour and 'grob' in flavour):
        return 'Orginial'
    elif 'ananas' == flavour or ('ananas' in flavour and 'carnitin' in flavour):
        return 'Ananas'
    elif ('butter' in flavour and 'keks' in flavour) or ('butter' in flavour and 'biscuit' in flavour) \
            or ('butter' in flavour and 'cookie' in flavour):
        return 'Butterkeks'
    elif 'caramel' == flavour or 'Karamell' == flavour:
        return 'Karamell'
    elif 'cheesecake' == flavour or 'käsekuchen' == flavour:
        return 'Käsekuchen'
    elif 'mango' in flavour and 'maracuja' in flavour:
        return 'Mango Maracuja'
    elif 'blutorange' == flavour or ('blood' in flavour and 'orange' in flavour):
        return 'Blutorange'
    elif 'cola' == flavour:
        return 'Cola'
    elif 'apfel' == flavour:
        return 'Apfel'
    else:
        return old_flavour


def parse_img(img: str):
    # Parse out linebreaks
    img = re.sub("/\r?\n|\r/", "", img)
    return re.sub('"', '', img)


# Returns true if nutrition is an image. If plain text, return false.
def parse_nutrition(nutrition_string):
    val = URLValidator()

    nutrition_string = re.sub("/\r?\n|\r/", "", nutrition_string)
    nutrition_string = re.sub('"', '', nutrition_string)

    # Check if nutrition is shopify image. This is not being recognized by url validator.
    if 'shopify' in nutrition_string:
        return True, nutrition_string

    # Check if nutrition is in an image whose path is given by an url
    try:
        val(nutrition_string)
        # Nutrition is image
        return True, nutrition_string
    except ValidationError:
        # Nutrition is no image
        return False, nutrition_string


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
        'post-workout',
        'post workout',
        'intra-workout'
    ]

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
    category = re.sub('"', '', category)

    replaced_category = None
    if category.lower() in exceptions or (category.lower() in fitmart_exceptions and current_shop == 'Fitmart')\
            or product_name.lower() == 'null' or (product_name == '') or \
            ('bundle' in product_name.lower()):
        return '', replaced_category, True
    elif category.lower() in d.category_matching[current_shop].keys():
        replaced_category = category.lower()
        return d.category_matching[current_shop][category.lower()], replaced_category, False
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

        return category, replaced_category, False


def parse_url(url: str):
    # Parse out linebreaks
    url = re.sub("/\r?\n|\r/", "", url)
    return re.sub('"', '', url)
