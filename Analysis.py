import pandas as pd
import numpy as np
import customer_profile_module as cpm
import macro_analysis as dm
import utility as u

df1 = pd.read_csv("CSV_Files\\1-22Export1.csv")
df2 = pd.read_csv("CSV_Files\\1-22Export2.csv")
df3 = pd.read_csv("CSV_Files\\1-22Export3.csv")
df4 = pd.read_csv("CSV_Files\\1-22Export5.csv")
df5 = pd.read_csv("CSV_Files\\1-22Export6.csv")
df6 = pd.read_csv("CSV_Files\\1-25Sept2020.csv")

df1.insert(loc=0 , column ='Month', value= 'December')
df2.insert(loc=0 , column ='Month', value= 'November')
df3.insert(loc=0 , column ='Month', value= 'October')
df6.insert(loc=0, column ='Month', value= 'September')
df4.insert(loc=0 , column ='Month', value= 'August')
df5.insert(loc=0 , column ='Month', value= 'July')

concat = pd.concat([df1,df2,df3,df6,df4,df5], ignore_index=True)
concat.to_csv("Raw_Analysis.csv", index=False)
'''Initialization instructions:
first drag the csv or csvs to be used for analysis into the CSV_Files folder

you can use the '*' function from the utility module to create the dataframe/concatenate csv(s)(in progress)

then clean the dataframe in question using utilty.clean

At this point the macro_analysis module is able to be utilized

In order to update the customer profiles, you need to first feed the dataframe into the init fields function in
    the utility module
The zipped values are then inputted into the act_salesrow_class function to activate the class over the list of rows.
This should complete the update of profile csv files'''
file = pd.read_csv('CSV_Files\\Raw_Analysis.csv')
# Test slice for functionality

test_slice = file.iloc[0:2]
test_slice =u.clean(test_slice)

fields = u.FieldLoader(test_slice)

#testable = cpm.SalesRow(*fields)
#testable()

'''Work log:
2/10 to-do
create utility.fn that initializes the dataframe(s) for analysis
create head() for a test dataframe and test customer_profile_module

final steps:
how to access customer profiles
displaying analysis in a customizable format
'''
