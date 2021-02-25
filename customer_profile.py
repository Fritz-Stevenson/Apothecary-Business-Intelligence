import pandas as pd
import re, os
from datetime import datetime

tea_product_list = ['Breakfast Buzz', 'Buddha\'s Berry', 'Chai Awakening', 'Coconut Genmaicha', 'Cosmic Cleanse',
                    'Golden Dream', 'Highbiscus', 'Hemp-Derived CBD Tea', 'Mellow Mint', 'Mystic', 'Oolong Passion',
                    'Pumpkin Spice', 'Sensualitea']
capsule_product_list = ['Blood Flow', 'Cleanse', 'Digest Well', 'Immunity Support', 'Mental Clarity', 'Sleep Aid',
                        'Super Citrus', 'Super Greens', 'Supreme Vitality', ]
smokeable_product_list = ['CBG Flower', 'Center', 'Kush Hemp CBD Flower', 'Peace', 'Relax', 'Sacred']
skincare_product_list = ['Buzz Balm', 'Focus', 'Insight', 'Love', 'Pain Away', 'Restful', 'Slumbering CBD Bath Soak',
                         'Soothing CBD Body Butter', 'Renewing CBD Face Cream', 'Unwind']
superfood_product_list = ['Blue Moon', 'Chocodelic Trip', 'Garden of Eden', 'Golden Milk', 'Mighty Matcha',
                          'Peppermint Treat', ]
honey_product_list = ['Hibiscus Goji Berry CBD Honey', 'Lavender CBD Honey', 'Lemon Ginger CBD Honey',
                      'Orange Turmeric CBD Honey', 'Organic Wildflower CBD Honey', 'Wild Rosin Honey',
                      'Renewing CBD Face Cream', ]
tincture_product_list = ['Dragon\'s Lair', 'Stomach Soother']


prep_p_list = tea_product_list + capsule_product_list + smokeable_product_list + skincare_product_list + superfood_product_list + honey_product_list + tincture_product_list
p_list = sorted(prep_p_list)

# A row from the csv is the unit of information that will alter the customer profile csv.
# This class should contain all necessary actions.


class SalesRow(object):
    # Need to edit init arguments for clarity and readability for users looking at CSVs
    def __init__(self, name, role, email, date, first_order, sales_total, total_orders, product_names,
                 product_quantity, product_item_cost, total_gross):
        global p_list
        global tea_product_list
        global capsule_product_list
        global smokeable_product_list
        global skincare_product_list
        global superfood_product_list
        global honey_product_list
        global tincture_product_list
        treated_product_list = product_names.split('\n')
        self.name = name
        self.role = role
        self.email = email
        self.date = date
        self.first_order = first_order
        self.sales_total = sales_total
        self.product_quantity = product_quantity.split('\n')
        self.product_item_cost = product_item_cost.split('\n')
        print(f'quant: {self.product_quantity} cost: {self.product_item_cost}')
        self.total_orders = int(total_orders)
        self.total_gross = total_gross
        products = []
        for i in prep_p_list:
            for o in treated_product_list:
                if i in o:
                    products.append(i)
        self.product_list = products
        print(self.product_list)
        check_for_customer = os.path.exists(self.profile_csv_outpath())
        if check_for_customer != True:
            self.init_profile()
        d = pd.read_csv(self.profile_csv_outpath())
        if self.date not in d.loc[d['Customer_Profile'] == 'Sales_Dates', 'Value']:
            d.loc[d['Customer_Profile'] == 'Sales_Dates', 'Value'] += str(f'{self.date}\n')
        d.loc[d['Customer_Profile'] == 'Sales_Totals', 'Value'] += str(f'{self.sales_total}\n')
        d.loc[d['Customer_Profile'] == 'Number_of_Sales', 'Value']= self.total_orders
        d.loc[d['Customer_Profile'] == 'Gross_Sales', 'Value']= self.total_gross
        for i in range(len(self.product_list)):
            product = self.product_list[i]
            quant = self.product_quantity[i]
            price = self.product_item_cost[i]
            d.loc[d['Customer_Profile'] == product, 'Value'] = float(d.loc[d['Customer_Profile'] == product, 'Value']) + float(quant)
            d.loc[d['Customer_Profile'] == product, 'Totals'] = float(d.loc[d['Customer_Profile'] == product, 'Totals']) + float(price)

        d.to_csv(self.profile_csv_outpath(), index= False)

    def profile_csv_outpath(self):
        outpath = f'{self.name}_customer_profile.csv'
        if self.role == 'Customer':
            direc = '.\\retail_customers'
            full = os.path.join(direc, outpath)
        else:
            direc = '.\\wholesale_customers'
            full = os.path.join(direc, outpath)
        return full

    def init_profile(self):
        profile_column = ['Name', 'Email', 'First_Order_Date', 'Gross_Sales', 'Number_of_Sales','Sales_Totals', 'Sales_Dates', 'Sales_Date_Differential'] + p_list
        init_values =[self.name, self.email, self.first_order, None, None,
                      None , None, None]
        end_values = list("0" * len(prep_p_list))
        totals = list('*'* len(init_values)) + end_values
        values = init_values + end_values
        d = {'Customer_Profile': profile_column, 'Value': values, 'Totals': totals}
        df = pd.DataFrame(data=d)
        df_new = df.set_index('Customer_Profile')
        outfile = open(self.profile_csv_outpath(), 'wb')
        df_new.to_csv(self.profile_csv_outpath(), encoding='utf-8')
        outfile.close()

    def date_differentials(self, dates_cell):
        dates = dates_cell.split('\n')
        present = datetime.now()
        current_stripped = datetime.strptime(present.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
        dates += current_stripped
        difference_list=[]
        for i in range(len(dates)):
            d1= dates[i]
            d2= dates[i+1]
            d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M")
            d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M")
            difference = d2 - d1
            difference_list.append(difference.days)
        return difference_list