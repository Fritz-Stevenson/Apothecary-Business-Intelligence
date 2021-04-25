tea_product_list = ['Breakfast Buzz', 'Buddha', 'Chai Awakening', 'Coconut Genmaicha', 'Cosmic Cleanse',
                    'Golden Dream', 'Highbiscus', 'Hemp-Derived CBD Tea', 'Mellow Mint', 'Mystic', 'Oolong Passion',
                    'Pumpkin Spice', 'Sensualitea', 'Tea Gift 8-Pack']
capsule_product_list = ['Blood Flow', 'Cleanse | CBD', 'Digest Well', 'Immunity Support', 'Mental Clarity', 'Sleep Aid',
                        'Super Citrus', 'Super Greens', 'Supreme Vitality']
smokeable_product_list = ['CBG Flower', 'Center', 'Kush Hemp CBD Flower', 'Peace', 'Relax', 'Sacred']
skincare_product_list = ['Buzz Balm', 'Focus', 'Insight', 'Love', 'Pain Away', 'Restful', 'Slumbering CBD Bath Soak',
                         'Soothing CBD Body Butter', 'Renewing CBD Face Cream', 'Unwind', 'Sugar Scrub']
superfood_product_list = ['Blue Moon', 'Chocodelic Trip', 'Garden of Eden', 'Golden Milk', 'Mighty Matcha',
                          'Peppermint Treat', 'Magickal Mushroom']
honey_product_list = ['Hibiscus Goji Berry', 'Lavender', 'Lemon Ginger',
                      'Orange Turmeric', 'Organic Wildflower', 'Wild Rosin Honey']
tincture_product_list = ['Dragon\'s Lair', 'Stomach Soother', 'Calming K9']
miscellaneous = ['Brothers Mug']


prep_p_list = tea_product_list + capsule_product_list + smokeable_product_list + skincare_product_list + superfood_product_list + honey_product_list + tincture_product_list + miscellaneous
p_list = sorted(prep_p_list)

unit_recipes = [
    {'name': 'Blood Flow', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167,
     'Garlic Powder': 1.6, 'Birch Bark Powder': 1.6, "Butcher's Broom Powder": 1.6},
    {'name': 'Blue Moon', 'Dehydrated Coconut Milk Powder': 11.396, 'Coconut Sugar': 8.302,
     'Blue Pea Flower Powder': 2.515, 'Pumpkin Spice Powder': 1.258, 'Jujube Powder': 0.075,
     'Chamomile Flower Powder': 0.075, 'Polygala Powder': 0.075, 'Vanilla Bean Powder': 0.201, 'Himalayan Salt': 0.101},
    {'name': 'Breakfast Buzz', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387,
     'Assam Black Tea': 2.75, 'Keemun Congou Black': 1.375, 'Ceylon Black Tea': 0.6875, 'Dunsandle Nilgiri Black': 0.6875},
    {'name': 'Brothers Mug'},  #
    {'name': 'Buddha', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Spring Green Tea': 2.209,
     'Tulsi (Rama, Vishna, Krishna)': 1.585, 'Blackberry Leaf': 0.106},
    {'name': 'Buzz Balm', 'Shea Butter': 0.648, 'Coconut Oil': 2.745, 'Beeswax': 0.00454,
     'Jojoba Oil': 0.00006, 'CBD Isolate': 0.01, 'Vitamin E Oil': 0.00093},
    {'name': 'CBG Flower', 'CBG Hemp': 4},
    {'name': 'Calming K9'},  #
    {'name': 'Center', 'Local Organic Hemp': 4.5, 'Mullein': 1.25, 'Wild Dagga': 0.4167, 'Wild Lettuce': 0.4167,
     'Lotus Leaf': 0.4167},
    {'name': 'Chai Awakening', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Chai Mix': 6.34,
     'Vanilla Black Tea': 0.793, 'Elder Flower': 0.131},
    {'name': 'Chocodelic Trip', 'Cane Sugar': 13.213, 'Dutch Cocoa': 7.928, 'Mycology Mushroom Powder': 1.633,
     'Vanilla Extract': 1.225},
    {'name': 'Cleanse | CBD', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167,
     'Activated Charcoal': 1.067, 'Dandelion Powder': 1.067, 'Chaga Powder ': 2.667},
    {'name': 'Coconut Genmaicha', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387,
     'Genmaicha Tea': 3.575, 'Toasted Coconut Chips': 0.715, 'Lemon Peel': 0.357, 'Lemongrass': 0.473,
     'Rose Petals': 0.315, 'Pineapple Powder': 0.063, 'Blackberry Leaf': .07},
    {'name': 'Cosmic Cleanse', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387,
     'Red Rooibos': 4.327, 'Licorice Root': 0.757, 'Marshmallow Root': 0.379, 'Dandelion': 0.568, 'Astragalus': 0.379,
     'Clove': 0.568, 'Cardamom': 0.379},
    {'name': 'Digest Well', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167, 'Ginger Powder': 1.2,
     'Fennel Powder': 1.2, 'Licorice Powder': 1.2, 'Peppermint Leaf Powder': 1.2},
    {'name': "Dragon's Lair"},  #
    {'name': 'Focus', 'Sweet Almond Oil': 6.825, 'Jojoba Oil': 2.5, 'CBD Isolate': 0.1, },
    {'name': 'Garden of Eden', 'Pea Protein Powder': 397.859, 'Hemp Protein Powder': 96.295,
     'Dehydrated Coconut Milk Powder': 18.185, 'Hemp Kief Powder': 4.546, 'Coconut Sugar': 41.33,
     'Green Power Powder': 17.565, 'Holy Basil Powder': 3.01, 'Vanilla Bean Powder': 3.01, 'Gotu Kola Powder': 2.066},
    {'name': 'Golden Dream', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Chamomile': 1.424,
     'Spearmint': 0.628, 'Orange Peel': 0.628, 'Lemongrass': 0.367, 'Rose Petals': 0.367, 'Linden Leaf': 0.629,
     'Blackberry Leaf': 0.629, 'Hawthorne Berry': 0.21},
    {'name': 'Golden Milk', 'Dehydrated Coconut Milk Powder': 11.049, 'Coconut Sugar': 8.049, 'Turmeric': 3.049,
     'Ginger Powder': 0.61, 'Black Pepper': 0.317, 'Cardamom Powder': 0.317, 'Cinnamon Powder': 0.317,
     'Vanilla Bean Powder': 0.195, 'Himalayan Salt': 0.097},
    {'name': 'Hemp-Derived CBD Tea', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387},
    {'name': 'Hibiscus Goji Berry'},  #
    {'name': 'Highbiscus', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Hibiscus': 3.26,
     'Spearmint': 0.357, 'Lemongrass': 0.306, 'Lemon Peel': 0.54, 'Orange Peel': 0.54, 'Rose Petals': 0.324,
     'Stevia': 0.135, 'Cranberry Powder': 0.036},
    {'name': 'Immunity Support', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167,
     'Black Pepper': 0.436, 'Turmeric': 4.363},
    {'name': 'Insight', 'Sweet Almond Oil': 6.247, 'Jojoba Oil': 2.5, 'CBD Isolate': 0.1, 'Clary Sage': 0.487,
     'Ylang Ylang': 0.142, 'White Fir': 0.095, 'Blue Tansy': 0.095, 'Frankincense': 0.1425, 'Juniper': 0.195,
     'Jasmine': 0.095},
    {'name': 'Kush Hemp CBD Flower'},  # This is already being calculate in inventory_order_prediction line 40
    {'name': 'Lavender'},  #
    {'name': 'Lemon Ginger'},  #
    {'name': 'Love', 'Sweet Almond Oil': 6.825, 'Jojoba Oil': 2.5, 'CBD Isolate': 0.1, 'Sandalwood Oil': 0.34,
     'Ylang Ylang': 0.095, 'Jasmine': 0.95, 'Vanilla Oil': 0.071, 'Cinnamon Oil': 0.0244},
    {'name': 'Magickal Mushroom', 'Pea Protein Powder': 352.378, 'Hemp Protein Powder': 87.058,
     'Dehydrated Coconut Milk Powder': 16.107, 'Hemp Kief Powder': 4.027, 'Coconut Sugar': 36.606,
     'Vanilla Bean Powder': 2.745, 'Dutch Cocoa': 73.212, 'Himalayan Salt': 4.398, 'Mycology Mushroom Powder': 9.456},
    {'name': 'Mellow Mint', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Spearmint': 1.024,
     'Peppermint': 3.071},
    {'name': 'Mental Clarity', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167,
     'Gingko Leaf Powder': 2.4, 'Shatavari Root Powder': 0.96, 'Ashwagandha Root Powder': 0.96, 'Rhodiala Powder': 0.48},
    {'name': 'Mighty Matcha', 'Matcha Powder': 11.2, 'Dehydrated Coconut Milk Powder': 2.8, 'CBD Isolate': 0.120},
    {'name': 'Mystic', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Kava Kava Root': 4.668,
     'Cassia Cinnamon Chips': 1.867, 'Stevia': 0.412, 'Cranberry Powder': 0.052},
    {'name': 'Oolong Passion', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Oolong': 4.944,
     'Lemongrass': 0.824, 'Orange Peel': 1.098, 'Dried Passionfruit Powder': 0.073},
    {'name': 'Orange Turmeric'},  #
    {'name': 'Organic Wildflower'},  #
    {'name': 'Pain Away', 'Sweet Almond Oil': 6.725, 'Jojoba Oil': 2.5, 'CBD Isolate': 0.1, 'Copaiba Balsam': 0.243,
     'Marjoram': 0.195, 'Sweet Basil': 0.095, 'Frankincense': 0.095, 'Arnica': 0.1425},
    {'name': 'Peace', 'Local Organic Hemp': 4.5, 'Mullein': 1.25, 'Lavender': 0.25, 'Wild Dagga': 0.25,
     'Rose Petals': 0.25, 'Lotus Leaf': 0.25, 'Spearmint': 0.25},
    {'name': 'Peppermint Treat', "Ghiradelli's Sweet Ground Chocolate": 8.14, 'Cane Sugar': 9.045, 'Dutch Cocoa': 0.226,
     'Vanilla Extract': 0.838, 'Peppermint Flavor Powder': 0.549},
    {'name': 'Pumpkin Spice', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387,
     'Pumpkin Spice Chai': 5, 'Vanilla Black Tea': 1.998, 'Elder Flower': 0.331, 'Pumpkin Powder': 0.066,
     'Pumpkin Spice Powder': 0.11},
    {'name': 'Relax', 'Local Organic Hemp': 4.5, 'Mullein': 1.25, 'Wild Dagga': 0.417, 'Mugwort': 0.417,
     'Calea ': 0.417},
    {'name': 'Renewing CBD Face Cream'},  #
    {'name': 'Restful', 'Sweet Almond Oil': 6.3, 'Jojoba Oil': 2.5, 'CBD Isolate': 0.1, 'Lavender Oil': 0.535,
     'Marjoram': 0.291, 'Bergamot': 0.195, 'Chamomile Blue Oil': 0.08, 'Ylang Ylang': 0.0425},
    {'name': 'Sacred', 'Local Organic Hemp': 4.5, 'Mullein': 1.25, 'Wild Dagga': 0.25, 'Marshmallow Root': 0.25,
     'Rose Petals': 0.25, 'Lemon Balm': 0.25, 'Tulsi (Rama, Vishna, Krishna)': 0.25},
    {'name': 'Sensualitea', 'Local Organic Hemp': 0.613, 'Dehydrated Coconut Milk Powder': 1.387, 'Lemon Balm': 1.011,
     'Rose Hips': 0.536, 'Lavender': 0.245, 'Horney Goat Weed': 0.167, 'Ginger Root': 0.491, 'Peppermint': 0.669,
     'Rose Petals': 0.379},
    {'name': 'Sleep Aid', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167,
     'Valerian Root Powder': 2.33, 'Chamomile Flower Powder': 1.165, 'Skullcap': 1.165, 'Melatonin': 0.140},
    {'name': 'Slumbering CBD Bath Soak'},  #
    {'name': 'Soothing CBD Body Butter'},  #
    {'name': 'Stomach Soother'},  #
    {'name': 'Sugar Scrub'},  #
    {'name': 'Super Citrus', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167,
     'Orange Peel Powder': 2.133, 'Lemon Peel Powder': 1.067, 'Grapefruit Peel Powder': 1.067,
     'Elderberry Powder': 0.533},
    {'name': 'Super Greens', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167, 'Chlorella': 1.6,
     'Spirulina': 1.6, 'Wheatgrass': 1.6},
    {'name': 'Supreme Vitality', 'Local Organic Hemp': 1.589, 'Dehydrated Coconut Milk Powder': 3.167,
     'Mycology Mushroom Powder': 4.8},
    {'name': 'Tea Gift 8-Pack'},  #
    {'name': 'Unwind', 'Sweet Almond Oil': 6.3, 'Jojoba Oil': 2.5, 'CBD Isolate': 0.1, 'Lavender Oil': 0.535,
     'Marjoram': 0.29175, 'Bergamot': 0.195, 'Ylang Ylang': 0.12, 'Chamomile Blue Oil': 0.04},
    {'name': 'Wild Rosin Honey'}  #
]
print(p_list)
