from products import items as d

# Foreach shop a unique parser must be written that executes the following steps:
# 1. Category name and product name to lower case
# 2. Check if a product in category name needs to be replaced by a mister m category
# 3. Determine mister m category based on a pattern in the product name
#
# In order to integrate a new shop into the parser
# the following additional steps are required to make the previously defined steps working:
# For step 2: Define a dict in items.py with the following naming scheme: toparse_<shopname>
#   -> This dict contains categories that hold product which belong at least into 2 different mister m categories
# For step 3: Define a if/elif structure with pattern matching in product name to determine the mister m category
#   -> Foreach mister m category define exactly 1 if or elif case
#   -> Sort the if/elif structure alphabetically
#
# If 1 shop is excluded from category matching based on product name, then mention it here with a short reason why
#   - Body and Fit: All categories that are parsed define a mister m category
#
#
# TODO: Allow product to be in multiple categories

# Match categories from shop rockanutrition to mister m categories.
# Matching based on product name.
def parse_rocka(category, product):
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category == 'vitamine & minerale' or category == 'drinks' or category == 'bake & cook':

        # Check product name for patterns in order to replace category with mister m category
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


# Match categories from shop fitmart to mister m categories.
# Matching based on product name.
def parse_fitmart(category, product):
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_fitmart:

        # Check product name for patterns in order to replace category with mister m category
        if 'brötchen' in product:
            return 'Brot'
        elif 'brownie' in product or 'pancakes' in product or 'waffles' in product or 'mischung' in product:
            return 'Backmischungen'
        elif 'candy' in product:
            return 'Süßigkeiten'
        elif 'chips' in product or 'flips' in product or 'nachos' in product:
            return 'Chips'
        elif 'crank' in product:
            return 'Trainingsbooster'
        elif 'crispies' in product:
            return 'Getreide'
        elif 'dream' in product or 'creme' in product or 'spread' in product or 'choc' in product or 'cream' in product or \
                'butter' in product or 'plantation' in product or 'walden' in product:
            return 'Aufstriche'
        elif 'muffin' in product or 'cookie' in product:
            return 'Cookies & Muffins'
        elif 'pasta' in product or 'pizza' in product:
            return 'Pizza & Pasta'
        elif 'pudding' in product:
            return 'Pudding'
        elif 'truffle' in product or 'riegel' in product or 'waffel' in product or 'snack' in product or \
                'bar' in product:
            return 'Schokolade'
        elif 'sauce' in product or 'callowfit' in product:
            return 'Gewürze & Saucen'
        elif 'zerup' in product or 'sirup' in product or 'syrup' in product:
            return 'Syrup'


# Match categories from shop myprotein to mister m categories.
# Matching based on product name.
def parse_myprotein(category, product):
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_myprotein:

        # Check product name for patterns in order to replace category with mister m category
        if 'aakg' in product:
            return 'AAKG'
        elif 'aufstrich' in product or 'butter' in product or 'dip pot' in product:
            return 'Aufstriche'
        elif 'antioxidant' in product or 'maca' in product:
            return 'Antioxidantien'
        elif 'bar' in product or 'rocky road' in product or 'carb crusher' in product or 'flapjack' in product:
            return 'Proteinriegel'
        elif 'beeren' in product:
            return 'Beeren'
        elif 'bcaa drink' in product or 'protein wasser' in product:
            return 'Protein Drinks'
        elif 'beta-alanin' in product:
            return 'Beta Alanin'
        elif 'bohnen' in product:
            return 'Bohnen'
        elif 'casein' in product:
            return 'Casein Protein'
        elif 'choc' in product or 'schokolade' in product:
            return 'Schokolade'
        elif 'chromium' in product or 'electrolyte' in product or 'eisen' in product:
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
        elif 'erbsenprotein' in product:
            return 'Erbsenprotein'
        elif 'fat binder' in product or 'thermo' in product or 'diet aid' in product or 'thermopure boost' in product\
                or 'glucomannan' in product or 'diet gel' in product:
            return 'Fatburner'
        elif 'fiber' in product:
            return 'Superfoods'
        elif 'flavdrop' in product:
            return 'Aromen und Süßstoffe'
        elif 'gel' in product:
            return 'Weitere'
        elif 'glucosamin' in product:
            return 'Glucosamin'
        elif 'glucose' in product or 'dextrin carbs' in product or 'palatinose' in product:
            return 'Kohlenhydratpulver'
        elif 'glutamin' in product:
            return 'Glutamin'
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
        elif 'maltodextrin' in product:
            return 'Maltodextrin'
        elif 'mandeln' in product or 'samen' in product or 'nüsse' in product or 'nut' in product:
            return 'Nüsse & Samen'
        elif 'öl' in product:
            return 'Speiseöle'
        elif 'ornithin' in product:
            return 'Ornithin'
        elif 'pancake' in product or 'cake' in product:
            return 'Backmischungen'
        elif 'performance mix' in product or 'recovery blend' in product or 'collagen protein' in product or \
                'dessert' in product:
            return 'Protein Mischungen'
        elif 'phosphatidylserin' in product or 'leucin' in product or 'tribulus' in product:
            return 'Planzliche Nahrungsergänzungsmittel'
        elif 'pork crunch' in product:
            return 'Jerkey'
        elif 'pre-workout' in product or 'pump' in product or 'pre workout' in product or 'preworkout' in product:
            return 'Trainingsbooster'
        elif 'reis' in product:
            return 'Alltägliche Lebensmittel'
        elif 'sirup' in product:
            return 'Syrup'
        elif "soja protein" in product:
            return "Sojaprotein"
        elif 'soße' in product:
            return 'Gewürze & Saucen'
        elif 'spaghetti' in product or 'penne' in product or 'fettuccine' in product:
            return 'Pizza & Pasta'
        elif 'taurin' in product:
            return 'Taurin'
        elif 'tyrosin' in product:
            return 'Tyrosin'
        elif 'veganes performance bundle' in product:
            return 'Veganes Protein'
        elif 'vitamin b' in product:
            return 'Vitamin B'
        elif 'vitamins bundle' in product or 'multivitamin' in product or 'immunity plus' in product or \
                'the multi' in product:
            return 'Multivitamine'
        elif 'vitamin c' in product:
            return 'Vitamin C'
        elif 'vitamin d' in product:
            return 'Vitamin D'
        elif 'waffel' in product or 'protein ball' in product:
            return 'Schokolade'
        elif 'whey' in product:
            return 'Whey Protein'
        elif 'zink' in product:
            return 'Zink'
        elif 'bcaa' in product or 'amino' in product:  # Many product with amino in -> Make sure this is the last
            return 'BCAA'


# Match categories from shop zecplus to mister m categories.
# Matching based on product name.
def parse_zecplus(category, product):
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_zecplus:

        # Check product name for patterns in order to replace category with mister m category
        if "all in one" in product:
            return "Multivitamine"
        elif "antioxidan" in product:
            return "Antioxidantien"
        elif "arginin" in product:
            return "Arginin"
        elif "aroma" in product:
            return "Aromen und Süßstoffe"
        elif "arthro" in product:
            return "Glucosamin"
        elif "bcaa" in product:
            return "BCAA"
        elif "beta alanin" in product:
            return "Beta Alanin"
        elif "casein" in product:
            return "Casein Protein"
        elif "citrullin" in product:
            return "Citrullin"
        elif "creatin" in product:
            return "Creatin"
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
        elif "glutamin" in product:
            return "Glutamin"
        elif "greens" in product:
            return "Pflanzliche Nahrungsergänzungsmittel"
        elif "kickdown" in product or "testosteron booster" in product:
            return "Trainingsbooster"
        elif "koffein" in product:
            return "Koffein"
        elif "kohlenhydrate" in product:
            return "Kohlenhydratpulver"
        elif "kokosöl" in product:
            return "Speiseöle"
        elif "liquid egg" in product:
            return "Eiklar"
        elif "maltodextrin" in product:
            return "Maltodextrin"
        elif "mehrkomponenten" in product:
            return "Protein Mischungen"
        elif "nährstoff optimizer" in product or "sleep" in product:
            return "Probiotika"
        elif "nudeln" in product or "pizza" in product:
            return "Pizza & Pasta"
        elif "oats" in product:
            return "Getreide"
        elif "proteinriegel" in product:
            return "Proteinriegel"
        elif "reis protein" in product:
            return "Reisprotein"
        elif "pulvermischung" in product or "pancakes" in product or 'bratlinge' in product:
            return "Backmischungen"
        elif "tryptophan" in product or "intraplus" in product or 'leucin' in product:
            return "Aminosäuren Komplex"
        elif "vitamin b" in product:
            return "Vitamin B"
        elif "vitamin c" in product:
            return "Vitamin C"
        elif "vitamin d" in product:
            return "Vitamin D"
        elif "whey" in product or "clean concentrate" in product:
            return "Whey Protein"
        elif "zink" in product:
            return "Zink"


# Match categories from shop zecplus to mister m categories.
# Matching based on product name.
def parse_weider(category, product):
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_weider:

        # Check product name for patterns in order to replace category with mister m category
        if "ace" in product or "mineralstack" in product or "megabolic" in product or "multi vita" in product\
                or "joint caps" in product:
            return "Multivitamine"
        elif "amino blast" in product or "amino nox" in product or "amino egg" in product or "amino powder" in product\
                or "amino essential" in product:
            return "Aminosäuren Komplex"
        elif "amino power liquid" in product or "bcaa rtd" in product or "eaa rtd" in product or "rush rtd" in product:
            return "Aminosäuren Getränke"
        elif "arginin" in product:
            return "Arginin"
        elif "bar" in product or "classic pack" in product or "riegel" in product or "wafer" in product:
            return "Proteinriegel"
        elif "bcaa" in product:
            return "BCAA"
        elif "glucan" in product:
            return "Antioxidantien"
        elif "casein" in product:
            return "Casein Protein"
        elif "cla" in product:
            return "CLA"
        elif "creme" in product:
            return "Aufstriche"
        elif "coffee" in product:
            return "Tee & Kaffee"
        elif "cookie" in product:
            return "Cookies & Muffins"
        elif "eaa" in product:
            return "EAA"
        elif "fresh up" in product:
            return "Aromen und Süßstoffe"
        elif "glucosamin" in product:
            return "Glucosamin"
        elif "glutamin" in product:
            return "Glutamin"
        elif "hmb" in product:
            return "HMB"
        elif "magnesium" in product:
            return "Magnesium"
        elif "omega 3" in product:
            return "Omega-3"
        elif "protein low carb" in product or "protein shake" in product or "starter drink" in product:
            return "Protein Drinks"
        elif "pump" in product or "rush" in product:
            return "Trainingsbooster"
        elif "soy 80" in product:
            return "Sojaprotein"
        elif "thermo stack" in product:
            return "Fatburner"
        elif "vegan protein" in product:
            return "Veganes Protein"
        elif "water" in product:
            return "Ohne Kalorien"
        elif "whey" in product or "protein 80" in product:
            return "Whey Protein"
        elif "zinc" in product:
            return "Zink"
