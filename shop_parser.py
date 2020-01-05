def parse_rocka(category, product):
    product = product.lower()
    category = category.lower()

    if category == 'vitamine & minerale':
        if 'vitamin b' in product:
            return 'Vitamin B'
        elif 'vitamin d' in product:
            return 'Vitamin D'
        elif 'essentials' in product:
            return 'Multivitamine'
        elif 'magnesium' in product:
            return 'Magnesium'
        elif 'strong' in product:
            return 'Strong'

    elif category == 'Drinks':
        if 'milk' in product:
            return 'Protein Drinks'
        elif 'swish' in product:
            return 'Energy Drinks'
        elif 'whey' in product:
            return 'Protein Drinks'
        elif 'cino' in product:
            return 'Tee & Kaffee'
        elif 'work':
            return 'Energy Drinks'

    elif category == 'bake & cook':
        if 'oil' in product:
            return 'Speiseöle'
        if 'bake' in product:
            return 'Backmischungen'