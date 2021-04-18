from datetime import datetime
import utility as u
import information_repository as ir
import pandas as pd
concat_file = u.clean(u.concat('CSV_Files'))
concat_file = concat_file[['Order_Date', 'Product_Name', 'Quantity', 'Item_Cost']]
dict_list = []
for i, row in concat_file.iterrows():
    row_date = row['Order_Date']
    row_date = datetime.strptime(row_date, "%Y-%m-%d %H:%M")
    row_date_month = row_date.month
    row_date_year = row_date.year
    raw_products = row['Product_Name'].replace('\r','').split('\n')
    raw_quantities = row['Quantity'].replace('\r','').split('\n')
    raw_cost = row['Item_Cost'].replace('\r','').split('\n')
    for key in range(len(raw_products)):
        product = [i for i in ir.p_list if i in raw_products[key]][0]
        quantity = int(raw_quantities[key])
        revenue = float(raw_cost[key])
        dict_object = [product, quantity, revenue, row_date_month, row_date_year]
        matched_dictionary = [i for i in dict_list if i['name'] == dict_object[0] and i['month'] == dict_object[3]
                              and i['year'] == dict_object[4]]
        if len(matched_dictionary) == 1:
                matched_dictionary[0]['count'] += dict_object[1]
                matched_dictionary[0]['revenue'] += dict_object[2]
        else:
            dict_list.append({'name': dict_object[0], 'count': dict_object[1],
                              'revenue': dict_object[2], 'month': dict_object[3], 'year': dict_object[4]})
big_frame = pd.DataFrame(columns=['year', 'month', 'count', 'revenue', 'change_over_month', 'product'])
time_span = []
for product in ir.p_list:
    product_dictionaries = sorted(sorted([i for i in dict_list if i['name'] == product], key=lambda x: x['month'],
                            reverse=True), key=lambda x: x['year'], reverse=True)
    year_list = []
    month_list = []
    count_list = []
    revenue_list = []
    product_list = []
    change_list = []
    for key in range(len(product_dictionaries)):
        year_list.append(product_dictionaries[key]['year'])
        month_list.append(product_dictionaries[key]['month'])
        count_list.append(product_dictionaries[key]['count'])
        revenue_list.append(product_dictionaries[key]['revenue'])
        product_list.append(product_dictionaries[key]['name'])
        if key > 0:
            try:
                change_list.append(round(((product_dictionaries[key]['revenue']/product_dictionaries[key]['count'])
                           / (product_dictionaries[key-1]['revenue']/product_dictionaries[key-1]['count']))*100), 1)
            except IndexError:
                print('change_list calls need to be refined')
        else:
            change_list.append(0)
    if product == 'Blue Moon':
        time_span.append(*zip(year_list,month_list))
    append_frame = pd.DataFrame([year_list,month_list,count_list, revenue_list, change_list, product_list])
    big_frame = pd.concat([big_frame, append_frame], ignore_index=True)
'''Now analyze the big_frame: for i in time_span: find the 3-5 highest change_over_months and create a new table or 
    something. Organize by product line and avg() the change_over_month values for yet another table. Find the highest
    positive change_over month values for the last month.'''
