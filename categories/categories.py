#!/usr/bin/env python3
# -*- coding: utf-8 -*-

categories = [
    {
        'cid': 'c2001',
        'name': 'Milchproteine',
        'main': True,
        'subCategories': [
            'c2002', 'c2003', 'c2004'
        ]
    },  {
        'cid': 'c2002',
        'name': 'Whey Protein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c2003',
        'name': 'Casein Protein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c2004',
        'name': 'Protein Mischungen',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c2005',
        'name': 'Pflanzliches Protein',
        'main': True,
        'subCategories': [
            'c2006', 'c2007', 'c2008', 'c2009', 'c2010'
        ]
    },  {
        'cid': 'c2006',
        'name': 'Sojaprotein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c2007',
        'name': 'Reisprotein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c2008',
        'name': 'Erbsenprotein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c2009',
        'name': 'Veganes Protein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c2010',
        'name': 'Superfood Protein',
        'main': False,
        'subCategories': []
    },    {
        'cid': 'c2011',
        'name': 'Weitere',
        'main': True,
        'subCategories': [
            'c2012'
        ]
    },  {
        'cid': 'c2012',
        'name': 'Eiprotein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3047',
        'name': 'Creatin',
        'main': True,
        'subCategories': []
    },  {
        'cid': 'c3001',
        'name': 'Aminosäuren',
        'main': True,
        'subCategories': [
            'c3002', 'c3003', 'c3004', 'c3005', 'c3006', 'c3007', 'c3008', 'c3009', 'c3010', 'c3011', 'c3012',
            'c3013', 'c3014', 'c3015', 'c3048'
        ]  # c3048 is correct
    },  {
        'cid': 'c3002',
        'name': 'BCAA',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3048',
        'name': 'Aminosäuren Getränke',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3003',
        'name': 'Aminosäuren Komplex',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3004',
        'name': 'Glutamin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3005',
        'name': 'HMB',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3006',
        'name': 'Arginin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3007',
        'name': 'AAKG',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3008',
        'name': 'Beta Alanin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3009',
        'name': 'Citrullin',
        'main': False,
        'subCategories': []
    },{
        'cid': 'c3010',
        'name': 'Gaba',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3011',
        'name': 'Lysin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3012',
        'name': 'Ornithin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3013',
        'name': 'Taurin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3014',
        'name': 'Tyrosin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3015',
        'name': 'EAA',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3016',
        'name': 'Pre-Workout',
        'main': True,
        'subCategories': [
            'c3017', 'c3018', 'c3019'
        ]
    },  {
        'cid': 'c3017',
        'name': 'Trainingsbooster',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3018',
        'name': 'Energy Drinks',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3019',
        'name': 'Koffein',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3020',
        'name': 'Vitalstoffe',
        'main': True,
        'subCategories': [
            'c3021', 'c3022', 'c3023', 'c3024', 'c3025', 'c3026', 'c3027', 'c3028', 'c3029', 'c3030', 'c3031', 'c3032',
            'c3033', 'c3034', 'c3035', 'c3036', 'c3037'
        ]
    },  {
        'cid': 'c3021',
        'name': 'Vitamin B',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3022',
        'name': 'Vitamin C',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3023',
        'name': 'Vitamin D',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3024',
        'name': 'Vitamin E',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3025',
        'name': 'Multivitamine',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3026',
        'name': 'Mineralstoffe',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3027',
        'name': 'Zink',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3028',
        'name': 'Magnesium',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3029',
        'name': 'ZMA',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3030',
        'name': 'Antioxidantien',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3031',
        'name': 'Fischöl',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3032',
        'name': 'Omega-3',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3033',
        'name': 'MCT Fette',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3034',
        'name': 'Glucosamin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3035',
        'name': 'Enzyme',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3036',
        'name': 'Probiotika',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3037',
        'name': 'Pflanzliche Nahrungsergänzungsmittel',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3038',
        'name': 'Masseaufbau',
        'main': True,
        'subCategories': [
            'c3039', 'c3040', 'c3041', 'c3042'
        ]
    },  {
        'cid': 'c3039',
        'name': 'Weight Gainer',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3040',
        'name': 'Kohlenhydratpulver',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3041',
        'name': 'Maltrodextrin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3042',
        'name': 'Dextrose',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3043',
        'name': 'Diätnahrung',
        'main': True,
        'subCategories': [
            'c3044', 'c3045', 'c3046'
        ]
    },  {
        'cid': 'c3044',
        'name': 'Fatburner',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3045',
        'name': 'Carnitin',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c3046',
        'name': 'CLA',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4001',
        'name': 'Riegel & Snacks',
        'main': True,
        'subCategories': [
            'c4002', 'c4003', 'c4004', 'c4005', 'c4006', 'c4007', 'c4008'
        ]
    },  {
        'cid': 'c4002',
        'name': 'Proteinriegel',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4003',
        'name': 'Chips',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4004',
        'name': 'Schokolade',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4005',
        'name': 'Energieriegel',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4006',
        'name': 'Cookies & Muffins',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4007',
        'name': 'Müsliriegel',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4008',
        'name': 'Süßigkeiten',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4009',
        'name': 'Superfoods',
        'main': True,
        'subCategories': [
            'c4010', 'c4011', 'c4012', 'c4013', 'c4014'
        ]
    },  {
        'cid': 'c4010',
        'name': 'Chia',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4011',
        'name': 'Spirulina',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4012',
        'name': 'Nüsse & Samen',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4013',
        'name': 'Beeren',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4014',
        'name': 'Bohnen',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4015',
        'name': 'Alltägliche Lebensmittel',
        'main': True,
        'subCategories': [
            'c4016', 'c4017', 'c4018', 'c4019', 'c4020', 'c4021', 'c4022', 'c4023', 'c4024', 'c4025', 'c4026', 'c4027',
            'c4028', 'c4029', 'c4030'
        ]
    }, {
        'cid': 'c4016',
        'name': 'Butter',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4017',
        'name': 'Aufstriche',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4018',
        'name': 'Fleisch',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4019',
        'name': 'Mealprep Boxen',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4020',
        'name': 'Gewürze & Saucen',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4021',
        'name': 'Tiefkühl',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4022',
        'name': 'Brot',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4023',
        'name': 'Jerkey',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4024',
        'name': 'Aromen und Süßstoffe',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4025',
        'name': 'Proteineis',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4026',
        'name': 'Pizza & Pasta',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4027',
        'name': 'Syrup',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4028',
        'name': 'Speiseöle',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4029',
        'name': 'Getreide',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4030',
        'name': 'Pudding',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4031',
        'name': 'Backen',
        'main': True,
        'subCategories': [
            'c4032', 'c4033', 'c4034'
        ]
    },  {
        'cid': 'c4032',
        'name': 'Mehl',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4033',
        'name': 'Backmischungen',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c4034',
        'name': 'Eiklar',
        'main': False,
        'subCategories': []
    },  {
        'cid': 'c5001',
        'name': 'Protein Drinks',
        'main': True,
        'subCategories': []
    },  {
        'cid': 'c5002',
        'name': 'Mahlzeitenersatz-Shakes',
        'main': True,
        'subCategories': []
    },  {
        'cid': 'c5003',
        'name': 'Isotonische Getränke',
        'main': True,
        'subCategories': []
    },  {
        'cid': 'c5004',
        'name': 'Ohne Kalorien',
        'main': True,
        'subCategories': []
    },  {
        'cid': 'c5005',
        'name': 'Tee & Kaffee',
        'main': True,
        'subCategories': []
    },  {
        'cid': 'c1001',
        'name': 'Beliebteste',
        'main': True,
        'subCategories': []
    },
]
