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
    'product-category',
    'product-name',
    'product-url',
    'product-description-long',
    'product-price',
    'product-size',
    'product-flavour',
    'product-img',
    'product-nutrition',
    'product-allergens'
]

# collection names in cloud
collection_names = {
    "fitmart.csv": "fitmart",
    "rockanutrition.csv": "rockanutrition",
    "body_and_fit.csv": "bodyandfit"
}

category_bodyandfit = {
    "sasein-protein": "Casein Protein",
    "milchprotein": "Casein Protein",
    "aminosäure-blends": "Aminsäuren Komplex",
    "was sind bcaas?": "BCAA",
    "aminosäure-getränke": "Aminosäuren Getränke",
    "pump & trainingsbooster": "Trainingsbooster",
    "kreatin": "Creatin",
    "kohlenhydrate": "Kohlenhydratpulver",
    "energy-riegel": "Energieriegel",
    "knabbereien": "Chips",
    "mandelmus": "Aufstriche",
    "cashewmus": "Aufstriche",
    "erdnussbutter": "Aufstriche",
    "flüssiges eiklar": "Eiklar",
    "leinsamen / flachssamen": "Nüsse & Samen",
    "pasta, reis & co.": "Pizza & Pasta",
    "cooking sprays & Speiseöle": "Speiseöle",
    "gewürze & sossen": "Gewürze & Saucen",
    "b-vitamine": "Vitamin B"
}

category_rockanutrition = {
    "aminosäuren": "EAA",
    "pre-workout": "Trainingsbooster",
    "omega 3": "Omega-3",
    "geschmackspulver": "Aromen und Süßstoffe",
    "creams & jams": "Aufstriche",
    "pancakes": "backmischungen",
    "muffins & waffeln": "Backmischungen",
    "kokosöl": "speiseöle",
    "saucen & gewürze": "Gewürze & Saucen",
    "protein eis": "Proteineis",
    "light chips": "Chips",
    "rocka whey isolate": "Whey Protein",
    "yum yum whey": "Whey Protein",
    "rocka milk": "Casein Protein",
    "the vegan": "Veganes Protein"
}

category_fitmart = {
    "Mehrkomponenten Protein": "Milchprotein Mischungen",
    "Soja Protein": "Sojaprotein",
    "Pflanzliches Eiweiss": "Veganes Protein",
    "Egg Protein": "Eiprotein",
    "Protein Pancake": "Backmischungen",
    "Protein Pudding": "Pudding",
    "Low Carb Proteinriegel": "Proteinriegel",
    "Protein Cookie": "Cookies & Muffins",
    "Amino Liquid": "Aminsäuren Getränke",
    "Creatin Kapseln": "Creatin",
    "Creatin Pulver": "Creatin",
    "Creatin Monohydrat": "Creatin",
    "Kre-Alkalyn": "Creatin",
    "Krea-Genic": "Creatin",
    "Creatin Matrix": "Creatin",
    "Haferflocken": "Getreide",
    "Pre-Workout Booster": "Trainingsbooster",
    "No Booster": "Trainingsbooster",
    "Booster ohne Creatin": "Trainingsbooster",
    "Energy Drink": "Energy Drinks",
    "Grüntee Extrakt": "Tee & Kaffee",
    "Koffein": "Tee & Kaffee",
    "Guarana": "Tee & Kaffee",
    "L-Carnitin": "Carnitin",
    "Flavour System": "Aromen & Sußstoffe",
    "Zuckeraustauschstoffe": "Aromen & Süßstoffe",
    "Low Carb Sirup": "Syrup",
    "low Carb Riegel": "Proteinriegel",
    "Low Carb Saucen": "Gewürze & Saucen",
    "Low Carb Butter": "Butter",
    "Low Carb Aufstriche": "Aufstriche",
    "Koch- & Backöle": "Speiseöle",
}

# match category from shop to site category
category_matching = {
    "bodyandfit": category_bodyandfit,
    "rockanutrition": category_rockanutrition,
    "fitmart": category_fitmart
}