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
    'product-allergens',
    'product-category',
    'product-description-long',
    'product-description-short',
    'product-flavour',
    'product-img',
    'product-name',
    'product-nutrition',
    'product-price',
    'product-shop',
    'product-size',
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
    "milcheiweiß & casein": "Casein Protein",
    "eiweißmischungen & -formeln": "Milchprotein Mischungen",
    "vegan protein": "Veganes Protein",
    "glutamin-supplemente": "Glutamin",
    "l-carnitin-supplemente": "Carnitin",
    "creatin-monohydrat": "Creatin",
    "weight-gainer-shakes": "Weight Gainer",
    "protein riegel": "Proteinriegel",
    "nussbutter": "Aufstriche",
    "süßstoffe & aromastoffe": "Aromen und Süßstoffe",
    "multivitamin-supplemente": "Multivitamine",
    "omega-3- & fischöl-supplemente": "Omega-3",
    "kräuter, pflanzen & nährstoffe": "Pflanzliche Nahrungsergänzungsmittel"
}

category_zecplus = {
    "creatine": "Creatin",
    "mhd-ware": "Antioxidantien",
    "booster": "Trainingsbooster",
    "riegel": "Proteinriegel"
}

category_weider = {
    "kohlenhydrate / weight gainer": "Weight Gainer",
    "kreatin": "Creatin",
    "koffeine / guarana": "Koffein",
    "omega 3": "Omega-3",
    "l-carnitine": "Carnitin"
}

# match category from shop to site category
category_matching = {
    "bodyandfit": category_bodyandfit,
    "rockanutrition": category_rockanutrition,
    "fitmart": category_fitmart,
    "myprotein": category_myprotein,
    "zecplus": category_zecplus,
    "weider": category_weider
}

toparse_myprotein = [
    "bcaa",
    "pillen & supplemente zur gewichtsabnahme",
    "diät-shakes",
    "pre-workout-getränke, -shakes und -supplemente",
    "intra-workout",
    "post-workout-shakes & erholungs-supplemente",
    "energie-supplemente",
    "energie-, sport- & recovery-gels",
    "sport- & energiegetränke",
    "mahlzeitenersatz",
    "proteinreiche lebensmittel",
    "proteinreiche snacks",
    "vitamin-supplemente",
    "mineralstoff-supplemente",
    "ballaststoff-supplemente"
]

toparse_zecplus = [
    "aminosäuren",
    "fettsäuren",
    "kohlenhydrate/weight gainer",
    "post workout"
    "proteine/eiweiss",
    "ergogenics",
    "food",
    "intra workout",
    "pre workout",
    "vitamine&mineralien"
]

toparse_weider = [
    "proteine / eiweiss",
    "aminosäuren",
    "vitamine / mineralien",
    "weitere produkte",
    "riegel",
    "drinks"
]
