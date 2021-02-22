import pandas as pd
import numpy as np
import customer_profile_module as cpm
import macro_analysis as ma
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
First, download the sales export as a csv from the woocommerce app in the wordpress engine.
The fields should be in the following order, as concatenation will disjoint columns if column names aren't identical,
making other functions useless.

Order Date, 
Email (Billing)
Customer Role
Customer first order date
Customer last order date
Customer Total Orders
Customer Total Spent
Full Name (Shipping)
Address 1 (Shipping)
City (Shipping)
State Name (Shipping) 
Postcode (Shipping)
Product Name
Item Cost
Item Name
Quantity
Discount Amount
Order Total Amount

In my experience, the time frame on the export field may need to be as little as 1 month due to a download time cap.

First drag the csv or csvs to be used for analysis into the CSV_Files folder. Then verify that there is not csv in the 
CSV_Files folder that you would like concatenated together to your final csv.

**The following will be edited into the Analysis.py file before it is run from the command line or an ide like pycharm.**
To initialize the dataframe you can use the concat function from the utility module to create the dataframe by 
concatenating csv(s) in the CSV_Folder. The field required is the folder path ie. frame = utility.concat('.\\folder_name')

then clean the dataframe in question using utilty.clean ie. frame = utility.clean(frame)

At this point the macro_analysis module is able to be utilized
Analysis.py has already imported macro_analysis as ma. Initialize the object by calling 
analysis = ma.dataframe_analysis(frame), where frame refers to the previously cleaned dataframe
you can then call the class functions using analysis.x where x is one of the functions.
some analysis include geographical_breakdown, customer_role_breakdown, avg_discount_rate, 

In order to update the customer profiles, you need to first feed the dataframe into the init fields function in
    the utility module
The zipped values are then inputted into the act_salesrow_class function to activate the class over the list of rows.
This should complete the update of profile csv files'''
file = pd.read_csv('CSV_Files\\Raw_Analysis.csv')
# Test slice for functionality
file = u.clean(file)
d_v = ma.dataframe_analysis(file)
d_v.customer_role_breakdown()
'''Work log:
2/19
functionality and indexing for time: reading, saving and analyzing time fields
make read-me and streamline initialization

final steps:
how to access customer profiles
displaying analysis in a customizable format
'''
