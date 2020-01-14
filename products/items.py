# column names which may appear in row
possible_column_names = [
    'product-name',
    'product-url-href',
    'product-description-long',
    'product-description-long-ul',
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
    'product-description-long-ul': 'product-description-long',
    'product-price': 'product-price',
    'product-size': 'product-size',
    'product-flavour': 'product-flavour',
    'product-img': 'product-img',
    'product-nutrition': 'product-nutrition',
    'product-allergens': 'product-allergens',
    'product-category': 'product-category'
}

collection_names = {
    "fitmart.csv": "Fitmart",
    "rockanutrition.csv": "Rockanutrition",
    "body_and_fit.csv": "Body and Fit",
    "myprotein.csv": "Myprotein",
    "zecplus.csv": "Zec+",
    "weider.csv": "Weider"
}

category_bodyandfit = {
    "whey protein": "Whey Protein",
    "casein-protein": "Casein Protein",
    "milchprotein mischungen": "Protein Mischungen",
    "veganes protein": "Veganes Protein",
    "superfood-proteine": "Superfood Protein",
    "sojaprotein": "Sojaprotein",
    "erbsenprotein": "Erbsenprotein",
    "protein-drinks": "Protein Drinks",
    "aminosäure-blends": "Aminosäuren Komplex",
    "was sind bcaas?": "BCAA",
    "glutamin": "Glutamin",
    "hmb": "HMB",
    "aminosäure-getränke": "Aminosäuren Getränke",
    "pump & trainingsbooster": "Trainingsbooster",
    "energy drinks": "Energy Drinks",
    "kreatin": "Creatin",
    "kohlenhydrate": "Kohlenhydratpulver",
    "energy bars": "Energieriegel",
    "proteinriegel": "Proteinriegel",
    "müsliriegel": "Müsliriegel",
    "cookies & muffins": "Cookies & Muffins",
    "knabbereien": "Chips",
    "schokolade": "Schokolade",
    "nüsse & samen": "Nüsse & Samen",
    "mehl": "Mehl",
    "backmischungen": "Backmischungen",
    "mandelmus": "Aufstriche",
    "cashewmus": "Aufstriche",
    "erdnussbutter": "Aufstriche",
    "chia": "Chia",
    "spirulina": "Spirulina",
    "flüssiges eiklar": "Eiklar",
    "leinsamen / flachssamen": "Nüsse & Samen",
    "pasta, reis & co": "Pizza & Pasta",
    "getreide": "Getreide",
    "cooking sprays & speiseöle": "Speiseöle",
    "gewürze & soßen": "Gewürze & Saucen",
    "tee & kaffee": "Tee & Kaffee",
    "aromen & süßstoffe": "Aromen und Süßstoffe",
    "deine diät": "Fatburner",
    "l-carnitin": "Carnitin",
    "cla": "CLA",
    "multivitamine": "Multivitamine",
    "b-vitamine": "Vitamin B",
    "vitamin c": "Vitamin C",
    "vitamin d": "Vitamin D",
    "magnesium": "Magnesium",
    "omega-3": "Omega-3",
    "probiotika": "Probiotika",
    "pflanzliche nahrungsergänzung": "Pflanzliche Nahrungsergänzungsmittel",
    "enzyme": "Enzyme",
    "glucosamin": "Glucosamin",
    "mahlzeitersetzende shakes": "Mahlzeitenersatz-Shakes"
}

category_rockanutrition = {
    "aminosäuren": "EAA",
    "pre-workout": "Trainingsbooster",
    "omega 3": "Omega-3",
    "geschmackspulver": "Aromen und Süßstoffe",
    "creams & jams": "Aufstriche",
    "pancakes": "Backmischungen",
    "muffins & waffeln": "Backmischungen",
    "kokosöl": "Speiseöle",
    "saucen & gewürze": "Gewürze & Saucen",
    "protein eis": "Proteineis",
    "light chips": "Chips",
    "rocka whey isolate": "Whey Protein",
    "yum yum whey": "Whey Protein",
    "rocka milk": "Casein Protein",
    "the vegan": "Veganes Protein",
    "proteinriegel": "Proteinriegel",
    "schokolade": "Schokolade",
    "syrup": "Syrup",
    "pizza & pasta": "Pizza & Pasta",
    "creatin": "Creatin"
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
    "aminosäuren komplex": "Aminosäuren Komplex",
    "amino liquid": "Aminosäuren Getränke",
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
    "koffein": "Koffein",
    "guarana": "Tee & Kaffee",
    "l-carnitin": "Carnitin",
    "flavour system": "Aromen und Süßstoffe",
    "zuckeraustauschstoffe": "Aromen und Süßstoffe",
    "low carb sirup": "Syrup",
    "low carb riegel": "Proteinriegel",
    "low carb saucen": "Gewürze & Saucen",
    "low carb butter": "Aufstriche",
    "low carb aufstriche": "Aufstriche",
    "koch- & backöle": "Speiseöle",
    "öle": "Speiseöle",
    "whey protein": "Whey Protein",
    "fatburner": "Fatburner",
    "kohlenhydratpulver": "Kohlenhydratpulver",
    "bcaa": "BCAA",
    "energieriegel": "Energieriegel",
    "glucosamin": "Glucosamin",
    "glutamin": "Glutamin",
    "casein protein": "Casein Protein",
    "reisprotein": "Reisprotein",
    "erbsenprotein": "Erbsenprotein",
    "all-in-one protein": "Protein Mischungen",
    "protein drink": "Protein Drinks",
    "proteinriegel": "Proteinriegel",
    "arginin": "Arginin",
    "aakg": "AAKG",
    "beta alanin": "Beta Alanin",
    "citrullin": "Citrullin",
    "gaba": "Gaba",
    "lysin": "Lysin",
    "ornithin": "Ornithin",
    "taurin": "Taurin",
    "tyrosin": "Tyrosin",
    "weight gainer": "Weight Gainer",
    "maltodextrin": "Maltodextrin",
    "dextrose": "Dextrose",
    'ballaststoffe': "Probiotika",
    "vitamin b": "Vitamin B",
    "vitamin c": "Vitamin C",
    "vitamin d": "Vitamin D",
    "vitamin e": "Vitamin E",
    "multivitamin": "Multivitamine",
    "mineralstoffe": "Mineralstoffe",
    "zink": "Zink",
    "magnesium": "Magnesium",
    "zma": "ZMA",
    "antioxidantien": "Antioxidantien",
    "fischöl": "Fischöl",
    "omega-3": "Omega-3",
    "mct fette": "MCT Fette",
    "gelenknahrung": "Probiotika"
}

category_myprotein = {
    "whey protein": "Whey Protein",
    "milcheiweiß & casein": "Casein Protein",
    "eiweißmischungen & -formeln": "Protein Mischungen",
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
    "kräuter, pflanzen & nährstoffe": "Pflanzliche Nahrungsergänzungsmittel",
    "protein drinks": "Protein Drinks"
}

category_zecplus = {
    "creatine": "Creatin",
    "mhd-ware": "Antioxidantien",
    "booster": "Trainingsbooster",
    "riegel": "Proteinriegel",
    "fatburner": "Fatburner"
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
    "Body and Fit": category_bodyandfit,
    "Rockanutrition": category_rockanutrition,
    "Fitmart": category_fitmart,
    "Myprotein": category_myprotein,
    "Zec+": category_zecplus,
    "Weider": category_weider
}

toparse_fitmart = [
    'protein snack',
    'low carb snacks',
    'low carb lebensmittel'
]

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
    "post workout",
    "proteine/eiweiß",
    "ergogenics",
    "food",
    "intra workout",
    "pre workout",
    "vitamine&mineralien"
]

toparse_weider = [
    "proteine / eiweiß",
    "aminosäuren",
    "vitamine / mineralien",
    "weitere produkte",
    "riegel",
    "drinks"
]
