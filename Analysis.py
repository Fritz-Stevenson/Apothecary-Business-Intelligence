import pandas as pd
import utility as u
import macro_analysis as ma

def profiles_master_init():
    frame = serve_frame()
    f = u.FieldLoader(frame)
    f
    u.date_difference_email_list_compiler()
def macro_analysis_master_init():
    frame = serve_frame()
    dfa = ma.dataframe_analysis(frame)
    dfa.avg_discount_rate()
    dfa.geographical_breakdown()
    dfa.customer_role_breakdown()
def serve_frame():
    frame = u.concat('.\\CSV_Files')
    frame = u.clean(frame)
    return frame


#concat = pd.concat([df1,df2,df3,df6,df4,df5], ignore_index=True)
#concat.to_csv("Raw_Analysis.csv", index=False)

file = pd.read_csv('Raw_Analysis.csv')
# Test slice for functionality
file = u.clean(file)
file = file.head(2)
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