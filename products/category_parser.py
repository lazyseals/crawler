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
# For step 3: Define a if/if structure with pattern matching in product name to determine the mister m category
#   -> Foreach mister m category define exactly 1 if or if case
#   -> Sort the if/if structure alphabetically
#
# If 1 shop is excluded from category matching based on product name, then mention it here with a short reason why
#   - Body and Fit: All categories that are parsed define a mister m category


# Match categories from shop rockanutrition to mister m categories.
# Matching based on product name.
def parse_rocka(category, product):
    # Categories a product can be in
    categories = []
    
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category == 'vitamine & minerale' or category == 'drinks' or category == 'bake & cook':

        # Check product name for patterns in order to replace category with mister m category
        if 'vitamin b' in product:
            categories.append('Vitamin B')
        if 'vitamin d' in product:
            categories.append('Vitamin D')
        if 'essentials' in product or 'strong' in product:
            categories.append('Multivitamine')
        if 'magnesium' in product:
            categories.append('Magnesium')
        if 'milk' in product or 'whey' in product:
            categories.append('Protein Drinks')
        if 'swish' in product or 'work' in product:
            categories.append('Energy Drinks')
        if 'cino' in product:
            categories.append('Tee & Kaffee')
        if 'oil' in product:
            categories.append('Speiseöle')
        if 'bake' in product:
            categories.append('Backmischungen')
        
        # Return all categories a product is in
        return categories


# Match categories from shop fitmart to mister m categories.
# Matching based on product name.
def parse_fitmart(category, product):
    # Categories a product can be in
    categories = []
    
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_fitmart:

        # Check product name for patterns in order to replace category with mister m category
        if 'brötchen' in product:
            categories.append('Brot')
        if 'brownie' in product or 'pancakes' in product or 'waffles' in product or 'mischung' in product:
            categories.append('Backmischungen')
        if 'candy' in product:
            categories.append('Süßigkeiten')
        if 'chips' in product or 'flips' in product or 'nachos' in product:
            categories.append('Chips')
        if 'crank' in product:
            categories.append('Trainingsbooster')
        if 'crispies' in product:
            categories.append('Getreide')
        if 'dream' in product or 'creme' in product or 'spread' in product or 'choc' in product or 'cream' in product or \
                'butter' in product or 'plantation' in product or 'walden' in product:
            categories.append('Aufstriche')
        if 'muffin' in product or 'cookie' in product:
            categories.append('Cookies & Muffins')
        if 'pasta' in product or 'pizza' in product:
            categories.append('Pizza & Pasta')
        if 'pudding' in product:
            categories.append('Pudding')
        if 'truffle' in product or 'riegel' in product or 'waffel' in product or 'snack' in product or \
                'bar' in product:
            categories.append('Schokolade')
        if 'sauce' in product or 'callowfit' in product:
            categories.append('Gewürze & Saucen')
        if 'zerup' in product or 'sirup' in product or 'syrup' in product:
            categories.append('Syrup')
        
        # Return all categories a product is in
        return categories


# Match categories from shop myprotein to mister m categories.
# Matching based on product name.
def parse_myprotein(category, product):
    # Categories a product can be in
    categories = []
    
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_myprotein:

        # Check product name for patterns in order to replace category with mister m category
        if 'aakg' in product:
            categories.append('AAKG')
        if 'aufstrich' in product or 'butter' in product or 'dip pot' in product:
            categories.append('Aufstriche')
        if 'antioxidant' in product or 'maca' in product:
            categories.append('Antioxidantien')
        if 'bar' in product or 'rocky road' in product or 'carb crusher' in product or 'flapjack' in product:
            categories.append('Proteinriegel')
        if 'beeren' in product:
            categories.append('Beeren')
        if 'bcaa drink' in product or 'protein wasser' in product:
            categories.append('Protein Drinks')
        if 'beta-alanin' in product:
            categories.append('Beta Alanin')
        if 'bohnen' in product:
            categories.append('Bohnen')
        if 'casein' in product:
            categories.append('Casein Protein')
        if 'choc' in product or 'schokolade' in product:
            categories.append('Schokolade')
        if 'chromium' in product or 'electrolyte' in product or 'eisen' in product:
            categories.append('Mineralstoffe')
        if 'citrullin' in product:
            categories.append('Citrullin')
        if 'cla' in product:
            categories.append('CLA')
        if 'cookie' in product or 'keks' in product or 'brownie' in product:
            categories.append('Cookies & Muffins')
        if 'crisps' in product:
            categories.append('Chips')
        if 'curcurmin' in product:
            categories.append('Curcurmin')
        if 'eaa' in product:
            categories.append('EAA')
        if 'eiklar' in product:
            categories.append('Eiklar')
        if 'erbsenprotein' in product:
            categories.append('Erbsenprotein')
        if 'fat binder' in product or 'thermo' in product or 'diet aid' in product or 'thermopure boost' in product\
                or 'glucomannan' in product or 'diet gel' in product:
            categories.append('Fatburner')
        if 'fiber' in product:
            categories.append('Superfoods')
        if 'flavdrop' in product:
            categories.append('Aromen und Süßstoffe')
        if 'gel' in product:
            categories.append('Weitere')
        if 'glucosamin' in product:
            categories.append('Glucosamin')
        if 'glucose' in product or 'dextrin carbs' in product or 'palatinose' in product:
            categories.append('Kohlenhydratpulver')
        if 'glutamin' in product:
            categories.append('Glutamin')
        if 'granola' in product or 'crispies' in product or 'oats' in product or 'hafer' in product:
            categories.append('Getreide')
        if 'hmb' in product:
            categories.append('HMB')
        if 'koffein' in product:
            categories.append('Koffein')
        if 'latte' in product or 'mocha' in product or 'kakao' in product or 'tee' in product:
            categories.append('Tee & Kaffee')
        if 'magnesium' in product:
            categories.append('Magnesium')
        if 'mahlzeitenersatz' in product:
            categories.append('Mahlzeitenersatz-Shakes')
        if 'maltodextrin' in product:
            categories.append('Maltodextrin')
        if 'mandeln' in product or 'samen' in product or 'nüsse' in product or 'nut' in product:
            categories.append('Nüsse & Samen')
        if 'öl' in product:
            categories.append('Speiseöle')
        if 'ornithin' in product:
            categories.append('Ornithin')
        if 'pancake' in product or 'cake' in product:
            categories.append('Backmischungen')
        if 'performance mix' in product or 'recovery blend' in product or 'collagen protein' in product or \
                'dessert' in product:
            categories.append('Protein Mischungen')
        if 'phosphatidylserin' in product or 'leucin' in product or 'tribulus' in product:
            categories.append('Planzliche Nahrungsergänzungsmittel')
        if 'pork crunch' in product:
            categories.append('Jerkey')
        if 'pre-workout' in product or 'pump' in product or 'pre workout' in product or 'preworkout' in product:
            categories.append('Trainingsbooster')
        if 'reis' in product:
            categories.append('Alltägliche Lebensmittel')
        if 'sirup' in product:
            categories.append('Syrup')
        if "soja protein" in product:
            categories.append("Sojaprotein")
        if 'soße' in product:
            categories.append('Gewürze & Saucen')
        if 'spaghetti' in product or 'penne' in product or 'fettuccine' in product:
            categories.append('Pizza & Pasta')
        if 'taurin' in product:
            categories.append('Taurin')
        if 'tyrosin' in product:
            categories.append('Tyrosin')
        if 'veganes performance bundle' in product:
            categories.append('Veganes Protein')
        if 'vitamin b' in product:
            categories.append('Vitamin B')
        if 'vitamins bundle' in product or 'multivitamin' in product or 'immunity plus' in product or \
                'the multi' in product:
            categories.append('Multivitamine')
        if 'vitamin c' in product:
            categories.append('Vitamin C')
        if 'vitamin d' in product:
            categories.append('Vitamin D')
        if 'waffel' in product or 'protein ball' in product:
            categories.append('Schokolade')
        if 'whey' in product:
            categories.append('Whey Protein')
        if 'zink' in product:
            categories.append('Zink')
        if 'bcaa' in product or 'amino' in product:  # Many product with amino in -> Make sure this is the last
            categories.append('BCAA')
        
        # Return all categories a product is in
        return categories


# Match categories from shop zecplus to mister m categories.
# Matching based on product name.
def parse_zecplus(category, product):
    # Categories a product can be in
    categories = []
    
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_zecplus:

        # Check product name for patterns in order to replace category with mister m category
        if "all in one" in product:
            categories.append("Multivitamine")
        if "antioxidan" in product:
            categories.append("Antioxidantien")
        if "arginin" in product:
            categories.append("Arginin")
        if "aroma" in product:
            categories.append("Aromen und Süßstoffe")
        if "arthro" in product:
            categories.append("Glucosamin")
        if "bcaa" in product:
            categories.append("BCAA")
        if "beta alanin" in product:
            categories.append("Beta Alanin")
        if "casein" in product:
            categories.append("Casein Protein")
        if "citrullin" in product:
            categories.append("Citrullin")
        if "creatin" in product:
            categories.append("Creatin")
        if "dextrose" in product:
            categories.append("Dextrose")
        if "eaa" in product:
            categories.append("EAA")
        if "fischöl" in product:
            categories.append("Omega-3")
        if "gaba" in product:
            categories.append("Gaba")
        if "gainer" in product:
            categories.append("Weight Gainer")
        if "glutamin" in product:
            categories.append("Glutamin")
        if "greens" in product:
            categories.append("Pflanzliche Nahrungsergänzungsmittel")
        if "kickdown" in product or "testosteron booster" in product:
            categories.append("Trainingsbooster")
        if "koffein" in product:
            categories.append("Koffein")
        if "kohlenhydrate" in product:
            categories.append("Kohlenhydratpulver")
        if "kokosöl" in product:
            categories.append("Speiseöle")
        if "liquid egg" in product:
            categories.append("Eiklar")
        if "maltodextrin" in product:
            categories.append("Maltodextrin")
        if "mehrkomponenten" in product:
            categories.append("Protein Mischungen")
        if "nährstoff optimizer" in product or "sleep" in product:
            categories.append("Probiotika")
        if "nudeln" in product or "pizza" in product:
            categories.append("Pizza & Pasta")
        if "oats" in product:
            categories.append("Getreide")
        if "proteinriegel" in product:
            categories.append("Proteinriegel")
        if "reis protein" in product:
            categories.append("Reisprotein")
        if "pulvermischung" in product or "pancakes" in product or 'bratlinge' in product:
            categories.append("Backmischungen")
        if "tryptophan" in product or "intraplus" in product or 'leucin' in product:
            categories.append("Aminosäuren Komplex")
        if "vitamin b" in product:
            categories.append("Vitamin B")
        if "vitamin c" in product:
            categories.append("Vitamin C")
        if "vitamin d" in product:
            categories.append("Vitamin D")
        if "whey" in product or "clean concentrate" in product:
            categories.append("Whey Protein")
        if "zink" in product:
            categories.append("Zink")
        
        # Return all categories a product is in
        return categories


# Match categories from shop zecplus to mister m categories.
# Matching based on product name.
def parse_weider(category, product):
    # Categories a product can be in
    categories = []
    
    # Product name to lower case for better string matching
    product = product.lower()
    # Category name to lower case for better string matching
    category = category.lower()

    # Check if product category needs to be placed into another category
    if category in d.toparse_weider:

        # Check product name for patterns in order to replace category with mister m category
        if "ace" in product or "mineralstack" in product or "megabolic" in product or "multi vita" in product\
                or "joint caps" in product:
            categories.append("Multivitamine")
        if "amino blast" in product or "amino nox" in product or "amino egg" in product or "amino powder" in product\
                or "amino essential" in product:
            categories.append("Aminosäuren Komplex")
        if "amino power liquid" in product or "bcaa rtd" in product or "eaa rtd" in product or "rush rtd" in product:
            categories.append("Aminosäuren Getränke")
        if "arginin" in product:
            categories.append("Arginin")
        if "bar" in product or "classic pack" in product or "riegel" in product or "wafer" in product:
            categories.append("Proteinriegel")
        if "bcaa" in product:
            categories.append("BCAA")
        if "glucan" in product:
            categories.append("Antioxidantien")
        if "casein" in product:
            categories.append("Casein Protein")
        if "cla" in product:
            categories.append("CLA")
        if "creme" in product:
            categories.append("Aufstriche")
        if "coffee" in product:
            categories.append("Tee & Kaffee")
        if "cookie" in product:
            categories.append("Cookies & Muffins")
        if "eaa" in product:
            categories.append("EAA")
        if "fresh up" in product:
            categories.append("Aromen und Süßstoffe")
        if "glucosamin" in product:
            categories.append("Glucosamin")
        if "glutamin" in product:
            categories.append("Glutamin")
        if "hmb" in product:
            categories.append("HMB")
        if "magnesium" in product:
            categories.append("Magnesium")
        if "omega 3" in product:
            categories.append("Omega-3")
        if "protein low carb" in product or "protein shake" in product or "starter drink" in product:
            categories.append("Protein Drinks")
        if "pump" in product or "rush" in product:
            categories.append("Trainingsbooster")
        if "soy 80" in product:
            categories.append("Sojaprotein")
        if "thermo stack" in product:
            categories.append("Fatburner")
        if "vegan protein" in product:
            categories.append("Veganes Protein")
        if "water" in product:
            categories.append("Ohne Kalorien")
        if "whey" in product or "protein 80" in product:
            categories.append("Whey Protein")
        if "zinc" in product:
            categories.append("Zink")
        
        # Return all categories a product is in
        return categories
