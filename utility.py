import pandas as pd
import os
import customer_profile as cpm
from datetime import datetime
def clean(inp):
    ''' Cleans a dataframe used for analysis, removing erroneous characters from columns.'''
    obj = inp
    obj.columns = obj.columns.str.replace(' ', '_')
    obj.columns = obj.columns.str.replace('(', '')
    obj.columns = obj.columns.str.replace(')', '')
    obj.fillna(0)
    return obj

def concat(dir_name):
    '''Concatenates all CSVs in the CSV_Files folder.'''
    abs_file_path = os.path.abspath(dir_name)
    os.chdir(abs_file_path)
    frame_list =[]
    for file in os.listdir(abs_file_path):
        if file.endswith('.csv'):
            file = os.path.abspath(file)
            sub_frame = pd.read_csv(file)
            frame_list.append(sub_frame)
    frame = pd.concat(frame_list, ignore_index=True)
    os.chdir('C:\\Users\\fritz\\PycharmProjects\\Brothers_Analysis')
    output = 'concat_file.csv'
    frame.to_csv(output, index = False)
    return frame
            
class FieldLoader:
    '''Class that reads the dataframe and serves customer_profile.SalesRow the appropriate set of parameters.'''
    def __init__(self, frame):
        self.frame = frame
        self.row_number = 0
        self.gen_wrapper()

    def gen_wrapper(self):
        '''Serves each row as an individual SalesRow() call'''
        for i in range(len(self.frame.index)):
            self.row_number = i
            final_list = self.gen_fields()
            init_SalesRow = cpm.SalesRow(*final_list)
            init_SalesRow

    def gen_fields(self):
        '''Sets appropriate cells as parameters, in the correct order '''
        #how about making this a list of lists, and making each row accessible as the fields
        # of a customer_profile_module.SalesRow call
        role = self.frame.loc[:, "Customer_Role"]
        email = self.frame.loc[:, 'Email_Billing']
        date = self.frame.loc[:, 'Order_Date']
        first_order = self.frame.loc[:, 'Customer_first_order_date']
        sale_total = self.frame.loc[:, "Order_Total_Amount"]
        number_of_sales = self.frame.loc[:, 'Customer_Total_Orders']
        raw_sales_product_cell = self.frame.loc[:, "Product_Name"]
        raw_product_quantity_cell = self.frame.loc[:, "Quantity"]
        total_gross_sales = self.frame.loc[:, "Customer_Total_Spent"]
        name = self.frame.loc[:, 'Full_Name_Billing']
        raw_item_cost_cell = self.frame.loc[:, "Item_Cost"]
        field_zip = zip(name, role, email, date, first_order, sale_total, number_of_sales, raw_sales_product_cell,
            raw_product_quantity_cell, raw_item_cost_cell, total_gross_sales)
        return list(field_zip)[self.row_number]

def date_difference_email_list_compiler():
    '''Calculates the difference in days between purchases, including the present time as a 'purchase'
    in order to calculate the time since last purchase.'''
    #You must run customer_profile.dates_differential() before this function or it will not operate correctly
    retail = os.listdir(os.getcwd()+'\\retail_customers')
    wholesale = os.listdir(os.getcwd()+'\\wholesale_customers')
    full_set =[]
    day_threshold = 40 # This number will control the days since previous sale threshold for email campaigns
    for i in retail:
        c = pd.read_csv('.\\retail_customers\\'+ i)
        #following are fields that can be formatted for output
        name = c.at[0,'Value']
        email = c.at[1, 'Value']
        dd_count = c.iat[7, 1]
        dd_count =dd_count.split('\n')
        if type(dd_count) == list:
            if int(dd_count[-1])> day_threshold:
                full_set.append(email) #output list addition
    for x in wholesale:
        c = pd.read_csv('.\\wholesale_customers\\' + x)
        name = c.at[0, 'Value']
        email = c.at[1, 'Value']
        dd_count = c.iat[7,1]
        dd_count.split('\n')
        if type(dd_count) != list:
            if int(dd_count) > day_threshold:
                full_set.append(email)
        if type(dd_count) == list:
            if int(dd_count[-1]) > day_threshold:
                full_set.append(email)
    return print(full_set)
def date_difference():
    change_count=0
    retail = os.listdir(os.getcwd() + '\\retail_customers')
    wholesale = os.listdir(os.getcwd() + '\\wholesale_customers')
    for i in retail:
        difference_list = []
        c = pd.read_csv('.\\retail_customers\\'+ i)
        dates = c.iat[6,1]
        dates =dates.split('\n')
        dates.remove('')
        present = datetime.now()
        current_stripped = present.strftime("%Y-%m-%d %H:%M")
        dates.append(current_stripped)
        dates = sorted(list(dates))

        for x in range(len(list(dates))):
            if x == len(list(dates))-1:
                break
            d1 = dates[x]
            d2 = dates[x + 1]
            d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M")
            d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M")
            difference = d2 - d1
            difference_list.append(difference.days)
        c.iat[7,1] = '\n'.join(map(str, difference_list))
        c.to_csv('.\\retail_customers\\'+ i, index=False)
        change_count +=1
    for i in wholesale:
        difference_list = []
        c = pd.read_csv('.\\wholesale_customers\\' + i)
        dates = c.iat[6, 1]
        dates = dates.split('\n')
        dates.remove('')
        present = datetime.now()
        current_stripped = present.strftime("%Y-%m-%d %H:%M")
        dates += current_stripped
        dates = sorted(list(dates))
        for i in range(len(list(dates))):
            if i == len(list(dates))-1:
                break
            d1 = dates[i]
            d2 = dates[i + 1]
            d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M")
            d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M")
            difference = d2 - d1
            difference_list.append(difference.days)
        c.iat[7, 1] = '\n'.join(map(str, difference_list))
        c.to_csv('.\\retail_customers\\' + i, index=False)
        change_count +=1
