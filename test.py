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
    product_dictionaries = sorted(sorted([i for i in dict_list if i['name'] == product], key=lambda x: x['month']
                                        ), key=lambda x: x['year'])
    data_list = []
    year_list = []
    month_list = []
    for key in range(len(product_dictionaries)):
        if key > 0:
            try:
                change_over_month =(100 - round(((product_dictionaries[key]['revenue']/product_dictionaries[key]['count'])
                           / (product_dictionaries[key-1]['revenue']/product_dictionaries[key-1]['count']))*100))

            except IndexError:
                print('change_list calls need to be refined')
        else:
            change_over_month = 0

        row_list = [product_dictionaries[key]['year'], product_dictionaries[key]['month'], 
                    product_dictionaries[key]['count'], product_dictionaries[key]['revenue'], change_over_month,
                    product_dictionaries[key]['name']]
        data_list.append(row_list)
        if product == 'Blue Moon':
            month_list.append(product_dictionaries[key]['month'])
            year_list.append(product_dictionaries[key]['year'])
            
    if product == 'Blue Moon':
        time_span =[*zip(year_list,month_list)]
    append_frame = pd.DataFrame(data = data_list, columns=['year', 'month', 'count', 'revenue', 'change_over_month', 'product'])
    big_frame = pd.concat([big_frame, append_frame], ignore_index=True)
'''Now analyze the big_frame: for i in time_span: find the 3-5 highest change_over_months and create a new table or 
    something. Organize by product line and avg() the change_over_month values for yet another table. Find the highest
    positive change_over month values for the last month.'''
meta_frame = pd.DataFrame(data=time_span, columns=['year', 'month'])

for i in time_span:
    year = i[0]
    month = i[1]
    product_line_list = [ir.tea_product_list, ir.capsule_product_list, ir.smokeable_product_list,
                         ir.skincare_product_list, ir.superfood_product_list, ir.honey_product_list,
                         ir.tincture_product_list]
    product_line_strings = ['Tea', 'Capsules', 'Smokeables', 'Skincare', 'Superfood', 'Honey', 'Tinctures']
    product_line_append_list = []
    product_line_analysis_frame = pd.DataFrame(columns=['year', 'month', 'avg_change_over_month', 'product_line'])
    line_index_counter = 0
    for product_line in product_line_list:
        line_list = []
        line_list.append(year)
        line_list.append(month)
        print(month)
        data_slice = big_frame.loc[big_frame['month'] == month].loc[big_frame['year'] == year].loc[big_frame['product'].isin(product_line)]
        avg_change_over_month = data_slice['change_over_month'].mean()
        line_list.append(avg_change_over_month)
        product_line = product_line_strings[line_index_counter]
        line_index_counter += 1
        print(product_line_list)
        line_list.append(product_line)
        product_line_append_list.append(line_list)
    product_line_analysis_frame = pd.DataFrame(data=product_line_append_list, columns=['year', 'month', 'avg_change_over_month', 'product_line'])
    print(product_line_analysis_frame.head(5))
    '''Functional but unweighted averages: Need to find sum of product line revenue and weight changeover month 
    by the fraction of total product line sales each sku comprises.'''
