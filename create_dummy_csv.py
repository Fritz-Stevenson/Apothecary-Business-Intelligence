import utility as u
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)
# Create a dummy for use outside the company.
def prep_dummy_csv():
    from hashlib import sha256
    # We need to hash customer emails as a semi-unique identifier
    def hash(inp):
        bytes=inp.encode('utf-8')
        h_e = sha256()
        h_e.update(bytes)
        return h_e.hexdigest()[:6]
    concat = u.concat('CSV_Files')
    to_dummy_csv = u.clean(concat)
    email_hashes = [hash(i) for i in to_dummy_csv['Email_Billing']]
    to_dummy_csv['Email_Billing'] = email_hashes
    to_dummy_csv[['Full_Name_Billing', 'Full_Name_Shipping', 'Address_1_Shipping']]='Restricted'
    to_dummy_csv.drop('Unnamed:_0', axis=1, inplace=True)
    to_dummy_csv['State_Name_Shipping'].loc[to_dummy_csv['State_Name_Shipping'].isna()] = 'Missing'
    to_dummy_csv['Discount_Amount'].loc[to_dummy_csv['Discount_Amount'].isna()] = to_dummy_csv['Discount_Amount'].mean()
    print(to_dummy_csv.isna().sum())
    to_dummy_csv.dropna(inplace=True)
    to_dummy_csv= to_dummy_csv.loc[to_dummy_csv['Order_Date']<='2020-12-31-23:59']
    print(to_dummy_csv.head(5))
    print(to_dummy_csv.columns)
    print(to_dummy_csv.tail(5))
    to_dummy_csv.to_csv('dummy.csv')
prep_dummy_csv()