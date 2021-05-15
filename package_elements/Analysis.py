import pandas as pd
import sys
import utility as u
import macro_analysis as ma


def profiles_master_init():
    frame = serve_frame()
    f = u.FieldLoader(frame)
    f
    u.date_difference_email_list_compiler()


def serve_frame(file):
    frame = u.concat(file)
    frame = u.clean(frame)
    return frame


if sys.argv[1] == 'inventory':
    fx = ma.InventoryPredictor()
    fx.ingredient_volume_table()
elif sys.argv[1] == 'geo':
    frame = serve_frame('CSV_Files')
    dfa = ma.DataframeAnalysis(frame)
    dfa.geographical_breakdown()
elif sys.argv[1] == 'role':
    frame = serve_frame('CSV_Files')
    dfa = ma.DataframeAnalysis(frame)
    dfa.customer_role_breakdown()
elif sys.argv[1] == 'discount':
    frame = serve_frame('CSV_Files')
    dfa = ma.DataframeAnalysis(frame)
    dfa.avg_discount_rate()
elif sys.argv[1] == 'pcp':
    frame = serve_frame('CSV_Files')
    dfpa = ma.ProductAnalysis(frame)
    dfpa.highest_positive_product_change_over_month_analysis()
elif sys.argv[1] == 'pcp':
    frame = serve_frame('CSV_Files')
    dfpa = ma.ProductAnalysis(frame)
    dfpa.highest_negative_product_change_over_month_analysis()
elif sys.argv[1] == 'plg':
    frame = serve_frame('CSV_Files')
    dfpa = ma.ProductAnalysis(frame)
    dfpa.product_line_change_over_month_graph()


file = u.concat('CSV_FIles')
# Test slice for functionality
file = u.clean(file)
cp1 = u.FieldLoader(file)
u.date_difference()
u.date_difference_email_list_compiler()
#profiles_master_init()


'''Work log:
2/25
functionality and indexing for time: reading, saving and analyzing time fields (completed?)

Streamline initializations: maybe make a initialization function in Analysis so we can simply click on the py file
and run the program

**As of now customer_profile line 63 should protect from repeated inputs of sales information. This will need to be tested.

***Concat in Utility needs to be corrected! atm there is only one customer!! Best guess is recent addition--concat

final steps:
how to access customer profiles
displaying analysis in a customizable format
'''

'''Entomology

--Dates may be out of order (oldest to newest) They must be sorted be as the customer profile is called (code in test)
'''
