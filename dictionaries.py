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
    "casein-protein": "Casein Protein",
    "milchprotein mischungen": "Protein Mischungen",
    "aminosäure-blends": "Aminsäuren Komplex",
    "was sind bcaas?": "BCAA",
    "aminosäure-getränke": "Aminosäuren Getränke",
    "pump & trainingsbooster": "Trainingsbooster",
    "kreatin": "Creatin",
    "kohlenhydrate": "Kohlenhydratpulver",
    "energy bars": "Energieriegel",
    "knabbereien": "Chips",
    "mandelmus": "Aufstriche",
    "cashewmus": "Aufstriche",
    "erdnussbutter": "Aufstriche",
    "flüssiges eiklar": "Eiklar",
    "leinsamen / flachssamen": "Nüsse & Samen",
    "pasta, reis & co": "Pizza & Pasta",
    "cooking sprays & speiseöle": "Speiseöle",
    "gewürze & soßen": "Gewürze & Saucen",
    "b-vitamine": "Vitamin B",
    "mahlzeitersetzende shakes": "Mahlzeitenersatz-Shakes"
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
    "mehrkomponenten protein": "Protein Mischungen",
    "soja protein": "Sojaprotein",
    "pflanzliches eiweiß": "Veganes Protein",
    "egg protein": "Eiprotein",
    "protein pancake": "Backmischungen",
    "protein pudding": "Pudding",
    "low carb protein riegel": "Proteinriegel",
    "protein cookie": "Cookies & Muffins",
    "amino liquid": "Aminsäuren Getränke",
    "creatin kapseln": "Creatin",
    "creatin pulver": "Creatin",
    "creatin monohydrat": "Creatin",
    "kre-alkalyn": "Creatin",
    "krea-genic": "Creatin",
    "creatin matrix": "Creatin",
    "haferflocken": "Getreide",
    "pre-workout booster": "Trainingsbooster",
    "no booster": "Trainingsbooster",
    "booster ohne creatin": "Trainingsbooster",
    "energy drink": "Energy Drinks",
    "grüntee extrakt": "Tee & Kaffee",
    "koffein": "Tee & Kaffee",
    "guarana": "Tee & Kaffee",
    "l-carnitin": "Carnitin",
    "flavour system": "Aromen & Sußstoffe",
    "zuckeraustauschstoffe": "Aromen & Süßstoffe",
    "low carb sirup": "Syrup",
    "low carb riegel": "Proteinriegel",
    "low carb saucen": "Gewürze & Saucen",
    "low carb butter": "Aufstriche",
    "low carb aufstriche": "Aufstriche",
    "koch- & backöle": "Speiseöle",
}

category_myprotein = {
    "casein & milch protein": "Casein Protein",
    "vegan protein": "Veganes Protein",
    "glutamin supplemente": "Glutamin",
    "l-carnitin supplemente": "Carnitin",
    "creatin monohydrat": "Creatin",
    "energy riegel": "Energieriegel",
    "nussbutter": "Aufstriche",
    "süßstoffe und aromastoffe": "Aromen und Süßstoffe",
    "omega 3 fettsäuren": "Omega-3",
    "pflanzliche supplemente": "Pflanzliche Nahrungsergänzungsmittel"
}

# match category from shop to site category
category_matching = {
    "bodyandfit": category_bodyandfit,
    "rockanutrition": category_rockanutrition,
    "fitmart": category_fitmart,
    "myprotein": category_myprotein
}

toparse_myprotein = [
    "bcaa supplemente",
    "gewichtsverlustsupplemente",
    "diät shakes",
    "pre workout",
    "intra workout",
    "post workout",
    "energy supplemente",
    "energy gels",
    "energy drinks",
    "mahlzeitenersatz",
    "proteinreiche lebensmittel",
    "protein snacks",
    "vitamine",
    "mineralstoffe",
    "ballaststoffe"
]
