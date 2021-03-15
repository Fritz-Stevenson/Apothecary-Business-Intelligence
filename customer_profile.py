import pandas as pd
import os
import info_repo

# A row from the csv is the unit of information that will alter the customer profile csv.
# This class should contain all necessary actions.


class SalesRow(object):
    # Need to edit init arguments for clarity and readability for users looking at CSVs
    def __init__(self, name, role, email, date, first_order, sales_total, total_orders, product_names,
                 product_quantity, product_item_cost, total_gross):
        treated_product_list = product_names.split('\n')
        self.name = name
        self.role = role
        self.email = email
        self.date = date
        self.first_order = first_order
        self.sales_total = sales_total
        self.product_quantity = product_quantity.replace('\r','').split('\n')
        self.product_item_cost = product_item_cost.replace('\r','').split('\n')
        self.total_orders = int(total_orders)
        self.total_gross = total_gross
        products = []
        # Is there a more efficient way to do this?
        for i in info_repo.prep_p_list:
            for o in treated_product_list:
                if i in o:
                    products.append(i)
        self.product_list = products
        check_for_customer = os.path.exists(str(self.profile_csv_outpath()))
        if check_for_customer != True:
            self.init_profile()
            d = pd.read_csv(self.profile_csv_outpath())
        d = pd.read_csv(self.profile_csv_outpath())
        if self.date not in d.iat[6,1]:
            if d.iat[6,1] == 'None':
                d.iat[6, 1] = f'{self.date}\n'
                d.iat[5, 1] = f'{self.sales_total}\n'
            else:
                d.iat[6,1] += f'{self.date}\n'
                d.iat[5,1] += f'{self.sales_total}\n'
            for i in range(len(self.product_list)):
                product = self.product_list[i]
                quant = self.product_quantity[i]
                price = self.product_item_cost[i]
                d.loc[d['Customer_Profile'] == product, 'Value'] = float(
                    d.loc[d['Customer_Profile'] == product, 'Value']) + float(quant)
                d.loc[d['Customer_Profile'] == product, 'Totals'] = float(
                    d.loc[d['Customer_Profile'] == product, 'Totals']) + float(price)
        else:
            print(f'date already in {self.name} database')
        outfile = open(self.profile_csv_outpath(), 'w+b')
        d.to_csv(self.profile_csv_outpath(), index=False)
        d.to_csv(self.profile_csv_outpath(), index= False)
        outfile.close()

    def profile_csv_outpath(self):
        outpath = f'{self.name}_customer_profile.csv'
        if self.role == 'Customer':
            direc = os.path.abspath('.\\retail_customers')
            full = os.path.join(direc, outpath)
        else:
            direc = os.path.abspath('.\\wholesale_customers')
            full = os.path.join(direc, outpath)
        return full

    def init_profile(self):
        profile_column = ['Name', 'Email', 'First_Order_Date', 'Gross_Sales', 'Number_of_Sales','Sales_Totals', 'Sales_Dates', 'Sales_Date_Differential'] + info_repo.p_list
        init_values =[self.name, (self.email), self.first_order, self.total_gross, self.total_orders,
                      None, None, None]
        end_values = list("0" * len(info_repo.prep_p_list))
        totals = list('*'* len(init_values)) + end_values
        values = init_values + end_values
        d = {'Customer_Profile': profile_column, 'Value': values, 'Totals': totals}
        df = pd.DataFrame(data=d)
        df_new = df.set_index('Customer_Profile')
        df_new['Value'] = df_new['Value'].astype(str)
        df_new
        outfile = open(self.profile_csv_outpath(), 'w+b')
        df_new.to_csv(str(self.profile_csv_outpath()), encoding='utf-8')
        outfile.close()

