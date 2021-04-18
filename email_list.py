import os
import pandas as pd
from datetime import datetime

os.chdir('C:\\Users\\fritz\\Documents\\DataBases\\brothers')
final_data_object = pd.concat([pd.read_csv(i) for i in os.listdir()])
os.chdir('C:\\Users\\fritz\\Documents\\DataBases')
final_data_object.to_csv('final_email_list.csv', index = False)
def date_difference_email_ready(obj):
    '''Iterates over the rows in a pandas object to find the date since purchase and return emails whose last purchase
    is older than the date_parameter

    ARGS:
        obj = pandas object for iteration

    Returns:
        list of emails for sales email implementation'''
    current_time = datetime.now()
    email_list = []
    date_parameter = 30  # all emails for x days since last purchase
    for index, row in obj.iterrows():
        if type(row['Order Date']) == str:
            date = row['Order Date']
            email = row['Email (Billing)']
            datetime_object = datetime.strptime(str(date), "%Y-%m-%d %H:%M")
            difference = current_time - datetime_object
            email_list.append(email)
            # if the difference between today and purchase is less than the date_parameter, remove email from list
            if difference.days < date_parameter:
                if email in email_list:
                    email_list.remove(email)
    #output_object = pd.DataFrame(email_list, columns=['Email_List'])
    #output_object.to_csv('Email_list_270days.csv', index=False)
    return print(list(set(email_list)), len(email_list))


#date_difference_email_ready(final_data_object)