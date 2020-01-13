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
    'product-price',
    'product-url'
]

# collection names in cloud
collection_names = {
    "fitmart.csv": "fitmart",
    "rockanutrition.csv": "rockanutrition",
    "body_and_fit.csv": "bodyandfit",
    "myprotein.csv": "myprotein",
    "zecplus.csv": "zecplus",
    "weider.csv": "weider"
}

