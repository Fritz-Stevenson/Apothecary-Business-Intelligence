import numpy as np
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
    {'name': 'Blood Flow', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Garlic Powder': np.random.uniform(0,8), 'Birch Bark Powder': np.random.uniform(0,8), "Butcher's Broom Powder": np.random.uniform(0,8)},
    {'name': 'Blue Moon', 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Coconut Sugar': np.random.uniform(0,8),
     'Blue Pea Flower Powder': np.random.uniform(0,8), 'Pumpkin Spice Powder': np.random.uniform(0,8), 'Jujube Powder': np.random.uniform(0,8),
     'Chamomile Flower Powder': np.random.uniform(0,8), 'Polygala Powder': np.random.uniform(0,8), 'Vanilla Bean Powder': np.random.uniform(0,8), 'Himalayan Salt': np.random.uniform(0,8)},
    {'name': 'Breakfast Buzz', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Assam Black Tea': np.random.uniform(0,8), 'Keemun Congou Black': np.random.uniform(0,8), 'Ceylon Black Tea': np.random.uniform(0,8), 'Dunsandle Nilgiri Black': np.random.uniform(0,8)},
    {'name': 'Brothers Mug'},  #
    {'name': 'Buddha', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Spring Green Tea': np.random.uniform(0,8),
     'Tulsi (Rama, Vishna, Krishna)': np.random.uniform(0,8), 'Blackberry Leaf': np.random.uniform(0,8)},
    {'name': 'Buzz Balm', 'Shea Butter': np.random.uniform(0,8), 'Coconut Oil': np.random.uniform(0,8), 'Beeswax': np.random.uniform(0,8),
     'Jojoba Oil': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8), 'Vitamin E Oil': np.random.uniform(0,8)},
    {'name': 'CBG Flower', 'CBG Hemp': np.random.uniform(0,8)},
    {'name': 'Calming K9'},  #
    {'name': 'Center', 'Local Organic Hemp': np.random.uniform(0,8), 'Mullein': np.random.uniform(0,8), 'Wild Dagga': np.random.uniform(0,8), 'Wild Lettuce': np.random.uniform(0,8),
     'Lotus Leaf': np.random.uniform(0,8)},
    {'name': 'Chai Awakening', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Chai Mix': np.random.uniform(0,8),
     'Vanilla Black Tea': np.random.uniform(0,8), 'Elder Flower': np.random.uniform(0,8)},
    {'name': 'Chocodelic Trip', 'Cane Sugar': np.random.uniform(0,8), 'Dutch Cocoa': np.random.uniform(0,8), 'Mycology Mushroom Powder': np.random.uniform(0,8),
     'Vanilla Extract': np.random.uniform(0,8)},
    {'name': 'Cleanse | CBD', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Activated Charcoal': np.random.uniform(0,8), 'Dandelion Powder': np.random.uniform(0,8), 'Chaga Powder ': np.random.uniform(0,8)},
    {'name': 'Coconut Genmaicha', 'Local Organic Hemp':np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Genmaicha Tea': np.random.uniform(0,8), 'Toasted Coconut Chips': np.random.uniform(0,8), 'Lemon Peel': np.random.uniform(0,8), 'Lemongrass': np.random.uniform(0,8),
     'Rose Petals': np.random.uniform(0,8), 'Pineapple Powder': np.random.uniform(0,8), 'Blackberry Leaf': np.random.uniform(0,8)},
    {'name': 'Cosmic Cleanse', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Red Rooibos': np.random.uniform(0,8), 'Licorice Root': np.random.uniform(0,8), 'Marshmallow Root': np.random.uniform(0,8), 'Dandelion': np.random.uniform(0,8), 'Astragalus': np.random.uniform(0,8),
     'Clove': np.random.uniform(0,8), 'Cardamom': np.random.uniform(0,8)},
    {'name': 'Digest Well', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Ginger Powder': np.random.uniform(0,8),
     'Fennel Powder': np.random.uniform(0,8), 'Licorice Powder': np.random.uniform(0,8), 'Peppermint Leaf Powder': np.random.uniform(0,8)},
    {'name': "Dragon's Lair"},  #
    {'name': 'Focus', 'Sweet Almond Oil': np.random.uniform(0,8), 'Jojoba Oil': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8) },
    {'name': 'Garden of Eden', 'Pea Protein Powder': np.random.uniform(0,8), 'Hemp Protein Powder': np.random.uniform(0,8),
     'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Hemp Kief Powder': np.random.uniform(0,8), 'Coconut Sugar': np.random.uniform(0,8),
     'Green Power Powder': np.random.uniform(0,8), 'Holy Basil Powder': np.random.uniform(0,8), 'Vanilla Bean Powder': np.random.uniform(0,8), 'Gotu Kola Powder': np.random.uniform(0,8)},
    {'name': 'Golden Dream', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Chamomile': np.random.uniform(0,8),
     'Spearmint': np.random.uniform(0,8), 'Orange Peel': np.random.uniform(0,8), 'Lemongrass': np.random.uniform(0,8), 'Rose Petals': np.random.uniform(0,8), 'Linden Leaf': np.random.uniform(0,8),
     'Blackberry Leaf': np.random.uniform(0,8), 'Hawthorne Berry': np.random.uniform(0,8)},
    {'name': 'Golden Milk', 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Coconut Sugar':np.random.uniform(0,8), 'Turmeric': np.random.uniform(0,8),
     'Ginger Powder': np.random.uniform(0,8), 'Black Pepper': np.random.uniform(0,8), 'Cardamom Powder': np.random.uniform(0,8), 'Cinnamon Powder': np.random.uniform(0,8),
     'Vanilla Bean Powder': np.random.uniform(0,8), 'Himalayan Salt': np.random.uniform(0,8)},
    {'name': 'Hemp-Derived CBD Tea', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8)},
    {'name': 'Hibiscus Goji Berry'},  #
    {'name': 'Highbiscus', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Hibiscus': np.random.uniform(0,8),
     'Spearmint': np.random.uniform(0,8), 'Lemongrass': np.random.uniform(0,8), 'Lemon Peel': np.random.uniform(0,8), 'Orange Peel': np.random.uniform(0,8), 'Rose Petals': np.random.uniform(0,8),
     'Stevia': np.random.uniform(0,8), 'Cranberry Powder': np.random.uniform(0,8)},
    {'name': 'Immunity Support', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Black Pepper': np.random.uniform(0,8), 'Turmeric': np.random.uniform(0,8)},
    {'name': 'Insight', 'Sweet Almond Oil': np.random.uniform(0,8), 'Jojoba Oil': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8), 'Clary Sage': np.random.uniform(0,8),
     'Ylang Ylang': np.random.uniform(0,8), 'White Fir': np.random.uniform(0,8), 'Blue Tansy': np.random.uniform(0,8), 'Frankincense': np.random.uniform(0,8), 'Juniper': np.random.uniform(0,8),
     'Jasmine': np.random.uniform(0,8)},
    {'name': 'Kush Hemp CBD Flower'},  # This is already being calculate in inventory_order_prediction line 40
    {'name': 'Lavender'},  #
    {'name': 'Lemon Ginger'},  #
    {'name': 'Love', 'Sweet Almond Oil': np.random.uniform(0,8), 'Jojoba Oil': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8), 'Sandalwood Oil': 0.34,
     'Ylang Ylang': np.random.uniform(0,8), 'Jasmine': np.random.uniform(0,8), 'Vanilla Oil': np.random.uniform(0,8), 'Cinnamon Oil': np.random.uniform(0,8)},
    {'name': 'Magickal Mushroom', 'Pea Protein Powder': np.random.uniform(0,8), 'Hemp Protein Powder': np.random.uniform(0,8),
     'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Hemp Kief Powder': np.random.uniform(0,8), 'Coconut Sugar': np.random.uniform(0,8),
     'Vanilla Bean Powder': np.random.uniform(0,8), 'Dutch Cocoa': np.random.uniform(0,8), 'Himalayan Salt': np.random.uniform(0,8), 'Mycology Mushroom Powder': np.random.uniform(0,8)},
    {'name': 'Mellow Mint', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Spearmint': np.random.uniform(0,8),
     'Peppermint': np.random.uniform(0,8)},
    {'name': 'Mental Clarity', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Gingko Leaf Powder': np.random.uniform(0,8), 'Shatavari Root Powder': np.random.uniform(0,8), 'Ashwagandha Root Powder': np.random.uniform(0,8), 'Rhodiala Powder': np.random.uniform(0,8)},
    {'name': 'Mighty Matcha', 'Matcha Powder': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8)},
    {'name': 'Mystic', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Kava Kava Root': np.random.uniform(0,8),
     'Cassia Cinnamon Chips': np.random.uniform(0,8), 'Stevia': np.random.uniform(0,8), 'Cranberry Powder': np.random.uniform(0,8)},
    {'name': 'Oolong Passion', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Oolong': np.random.uniform(0,8),
     'Lemongrass': np.random.uniform(0,8), 'Orange Peel': np.random.uniform(0,8), 'Dried Passionfruit Powder': np.random.uniform(0,8)},
    {'name': 'Orange Turmeric'},  #
    {'name': 'Organic Wildflower'},  #
    {'name': 'Pain Away', 'Sweet Almond Oil': np.random.uniform(0,8), 'Jojoba Oil': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8), 'Copaiba Balsam': np.random.uniform(0,8),
     'Marjoram': np.random.uniform(0,8), 'Sweet Basil': np.random.uniform(0,8), 'Frankincense': np.random.uniform(0,8), 'Arnica': np.random.uniform(0,8)},
    {'name': 'Peace', 'Local Organic Hemp': np.random.uniform(0,8), 'Mullein': np.random.uniform(0,8), 'Lavender': np.random.uniform(0,8), 'Wild Dagga': np.random.uniform(0,8),
     'Rose Petals': np.random.uniform(0,8), 'Lotus Leaf': np.random.uniform(0,8), 'Spearmint': np.random.uniform(0,8)},
    {'name': 'Peppermint Treat', "Ghiradelli's Sweet Ground Chocolate": np.random.uniform(0,8), 'Cane Sugar': np.random.uniform(0,8), 'Dutch Cocoa': np.random.uniform(0,8),
     'Vanilla Extract': np.random.uniform(0,8), 'Peppermint Flavor Powder': np.random.uniform(0,8)},
    {'name': 'Pumpkin Spice', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Pumpkin Spice Chai': np.random.uniform(0,8), 'Vanilla Black Tea': np.random.uniform(0,8), 'Elder Flower': np.random.uniform(0,8), 'Pumpkin Powder': np.random.uniform(0,8),
     'Pumpkin Spice Powder': np.random.uniform(0,8)},
    {'name': 'Relax', 'Local Organic Hemp': np.random.uniform(0,8), 'Mullein': np.random.uniform(0,8), 'Wild Dagga': np.random.uniform(0,8), 'Mugwort': np.random.uniform(0,8),
     'Calea ': np.random.uniform(0,8)},
    {'name': 'Renewing CBD Face Cream'},  #
    {'name': 'Restful', 'Sweet Almond Oil': np.random.uniform(0,8), 'Jojoba Oil': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8), 'Lavender Oil': np.random.uniform(0,8),
     'Marjoram': np.random.uniform(0,8), 'Bergamot': np.random.uniform(0,8), 'Chamomile Blue Oil': np.random.uniform(0,8), 'Ylang Ylang': np.random.uniform(0,8)},
    {'name': 'Sacred', 'Local Organic Hemp': np.random.uniform(0,8), 'Mullein': np.random.uniform(0,8), 'Wild Dagga': np.random.uniform(0,8), 'Marshmallow Root': np.random.uniform(0,8),
     'Rose Petals': np.random.uniform(0,8), 'Lemon Balm': np.random.uniform(0,8), 'Tulsi (Rama, Vishna, Krishna)': np.random.uniform(0,8)},
    {'name': 'Sensualitea', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Lemon Balm': np.random.uniform(0,8),
     'Rose Hips': np.random.uniform(0,8), 'Lavender': np.random.uniform(0,8), 'Horney Goat Weed': np.random.uniform(0,8), 'Ginger Root': np.random.uniform(0,8), 'Peppermint': 0.669,
     'Rose Petals': np.random.uniform(0,8)},
    {'name': 'Sleep Aid', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Valerian Root Powder': np.random.uniform(0,8), 'Chamomile Flower Powder': np.random.uniform(0,8), 'Skullcap': np.random.uniform(0,8), 'Melatonin': np.random.uniform(0,8)},
    {'name': 'Slumbering CBD Bath Soak'},  #
    {'name': 'Soothing CBD Body Butter'},  #
    {'name': 'Stomach Soother'},  #
    {'name': 'Sugar Scrub'},  #
    {'name': 'Super Citrus', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Orange Peel Powder': np.random.uniform(0,8), 'Lemon Peel Powder': np.random.uniform(0,8), 'Grapefruit Peel Powder': np.random.uniform(0,8),
     'Elderberry Powder':np.random.uniform(0,8)},
    {'name': 'Super Greens', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8), 'Chlorella': np.random.uniform(0,8),
     'Spirulina': np.random.uniform(0,8), 'Wheatgrass': np.random.uniform(0,8)},
    {'name': 'Supreme Vitality', 'Local Organic Hemp': np.random.uniform(0,8), 'Dehydrated Coconut Milk Powder': np.random.uniform(0,8),
     'Mycology Mushroom Powder': np.random.uniform(0,8)},
    {'name': 'Tea Gift 8-Pack'},  #
    {'name': 'Unwind', 'Sweet Almond Oil': np.random.uniform(0,8), 'Jojoba Oil': np.random.uniform(0,8), 'CBD Isolate': np.random.uniform(0,8), 'Lavender Oil': np.random.uniform(0,8),
     'Marjoram': np.random.uniform(0,8), 'Bergamot': np.random.uniform(0,8), 'Ylang Ylang': np.random.uniform(0,8), 'Chamomile Blue Oil': np.random.uniform(0,8)},
