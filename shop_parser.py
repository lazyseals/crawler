import dictionaries as d

def parse_rocka(category, product):
    product = product.lower()
    category = category.lower()

    if category == 'vitamine & minerale' or category == 'drinks' or category == 'bake & cook':
        if 'vitamin b' in product:
            return 'Vitamin B'
        elif 'vitamin d' in product:
            return 'Vitamin D'
        elif 'essentials' in product or 'strong' in product:
            return 'Multivitamine'
        elif 'magnesium' in product:
            return 'Magnesium'
        elif 'milk' in product or 'whey' in product:
            return 'Protein Drinks'
        elif 'swish' in product or 'work' in product:
            return 'Energy Drinks'
        elif 'cino' in product:
            return 'Tee & Kaffee'
        elif 'oil' in product:
            return 'Speiseöle'
        elif 'bake' in product:
            return 'Backmischungen'


def parse_fitmart(category, product):
    product = product.lower()
    category = category.lower()

    if category == 'protein snack' or category == 'low carb snack' or category == 'low carb lebensmittel':
        if 'dream' in product or 'creme' in product or 'spread' in product or 'choc' in product or 'cream' in product or \
                'butter' in product or 'plantation' in product or 'walden' in product:
            return 'Aufstriche'
        elif 'chips' in product or 'flips' in product or 'nachos' in product:
            return 'Chips'
        elif 'pasta' in product or 'pizza' in product:
            return 'Pizza & Pasta'
        elif 'brownie' in product or 'pancakes' in product or 'waffles' in product or 'mischung' in product:
            return 'Backmischungen'
        elif product or 'pudding':
            return 'Pudding'
        elif 'muffin' in product or 'cookie' in product:
            return 'Cookies & Muffins'
        elif 'candy' in product:
            return 'Süßigkeiten'
        elif 'truffle' in product or 'riegel' in product or 'waffel' in product or 'snack' in product:
            return 'Schokolade'
        elif 'sauce' in product:
            return 'Gewürze & Saucen'
        elif 'zerup' in product or 'sirup' in product or 'syrup' in product:
            return 'Syrup'
        elif 'brötchen' in product:
            return 'Brot'


def parse_myprotein(category, product):
    product = product.lower()
    category = category.lower()

    if category in d.toparse_myprotein:
        if 'aakg' in product:
            return 'AAKG'
        elif 'aufstrich' in product or 'butter' in product or 'dip pot' in product:
            return 'Aufstriche'
        elif 'antioxidant' in product or 'maca' in product:
            return 'Antioxidantien'
        elif 'beeren' in product:
            return 'Beeren'
        elif 'bcaa drink' in product or 'protein wasser' in product:
            return 'Protein Drinks'
        elif 'beta-alanin' in product:
            return 'Beta Alanin'
        elif 'choc' in product or 'schokolade' in product:
            return 'Schokolade'
        elif 'chromium' in product or 'elektrolyte' in product or 'eisen' in product:
            return 'Mineralstoffe'
        elif 'citrullin' in product:
            return 'Citrullin'
        elif 'cla' in product:
            return 'CLA'
        elif 'cookie' in product or 'keks' in product or 'brownie' in product:
            return 'Cookies & Muffins'
        elif 'crisps' in product:
            return 'Chips'
        elif 'curcurmin' in product:
            return 'Curcurmin'
        elif 'eaa' in product:
            return 'EAA'
        elif 'eiklar' in product:
            return 'Eiklar'
        elif 'fat binder' in product or 'thermo-x' in product or 'diet aid' in product or 'thermopure boost' in product\
                or 'glucomannan' in product or 'diet gel' in product:
            return 'Fatburner'
        elif 'glucosamin' in product:
            return 'Glucosamin'
        elif 'glucose' in product or 'dextrin carbs' in product or 'palatinose' in product:
            return 'Kohlenhydratpulver'
        elif 'granola' in product or 'crispies' in product or 'oats' in product or 'hafer' in product:
            return 'Getreide'
        elif 'hmb' in product:
            return 'HMB'
        elif 'koffein' in product:
            return 'Koffein'
        elif 'latte' in product or 'mocha' in product or 'kakao' in product or 'tee' in product:
            return 'Tee & Kaffee'
        elif 'magnesium' in product:
            return 'Magnesium'
        elif 'mahlzeitenersatz' in product:
            return 'Mahlzeitenersatz-Shakes'
        elif 'maltrodextrin' in product:
            return 'Maltrodextrin'
        elif 'mandeln' in product or 'samen' in product or 'nüsse' in product or 'nut' in product:
            return 'Nüsse & Samen'
        elif 'öl' in product:
            return 'Speiseöle'
        elif 'ornithin' in product:
            return 'Ornithin'
        elif 'pancake' in product or 'cake' in product:
            return 'Backmischungen'
        elif 'phosphatidylserin' in product or 'leucin' in product or 'tribulus' in product:
            return 'Planzliche Nahrungsergänzungsmittel'
        elif 'pork crunch' in product:
            return 'Jerkey'
        elif 'pre-workout' in product or 'pump' in product:
            return 'Trainingsbooster'
        elif 'sirup' in product:
            return 'Syrup'
        elif 'soße' in product:
            return 'Gewürze & Saucen'
        elif 'spaghetti' in product or 'penne' in product or 'fettuccine' in product:
            return 'Pizza & Pasta'
        elif 'taurin' in product:
            return 'Taurin'
        elif 'tyrosin' in product:
            return 'Tyrosin'
        elif 'vitamin b' in product:
            return 'Vitamin B'
        elif 'vitamins bundle' in product:
            return 'Multivitamine'
        elif 'vitamin c' in product:
            return 'Vitamin C'
        elif 'vitamin d' in product:
            return 'Vitamin D'
        elif 'zink' in product:
            return 'Zink'
        elif 'bcaa' in product or 'amino' in product:  # Many product with amino in -> Make sure this is the last
            return 'BCAA'

def parse_zecplus(category, product):
    product = product.lower()
    category = category.lower()

    if category in d.toparse_zecplus:
        if "all in one" in product:
            return "Multivitamine"
        elif "antioxidan" in product:
            return "Antioxidantien"
        elif "arginin" in product:
            return "Arginin"
        elif "aroma" in product:
            return "Aromen und Süßstoffe"
        elif "athro" in product:
            return "Glucosamin"
        elif "bcaa" in product:
            return "BCAA"
        elif "beta alanin" in product:
            return "Beta Alanin"
        elif "casein" in product:
            return "Casein Protein"
        elif "citrullin" in product:
            return "Citrullin"
        elif "dextrose" in product:
            return "Dextrose"
        elif "eaa" in product:
            return "EAA"
        elif "fischöl" in product:
            return "Omega-3"
        elif "gaba" in product:
            return "Gaba"
        elif "gainer" in product:
            return "Weight Gainer"
        elif "greens" in product:
            return "Pflanzliche Nahrungsergänzungsmittel"
        elif "koffein" in product:
            return "Koffein"
        elif "kohlenhydrate" in product:
            return "Kohlenhydratpulver"
        elif "kokosöl" in product:
            return "Speiseöle"
        elif "liquid egg" in product:
            return "eiklar"
        elif "maltrodextrin" in product:
            return "Maltrodextrin"
        elif "mehrkomponenten" in product:
            return "Protein Mischungen"
        elif "nährstoff optimizer" in product or "sleep" in product:
            return "Probiotika"
        elif "nudeln" in product or "pizza" in product:
            return "Pizza & Pasta"
        elif "oats" in product:
            return "Getreide"
        elif "reis protein" in product:
            return "Reisprotein"
        elif "pulvermischung" in product or "pancakes" in product:
            return "Backmischungen"
        elif "tryptophan" in product or "intraplus" in product:
            return "Aminosäuren Komplex"
        elif "vitamin c" in product:
            return "Vitamin C"
        elif "vitamin d" in product:
            return "Vitamin D"
        elif "whey" in product or "clean concentrate" in product:
            return "Whey Protein"
        elif "zink" in product:
            return "Zink"
