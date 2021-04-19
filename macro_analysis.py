import pandas as pd
from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.models import HoverTool
class dataframe_analysis:
    '''Arms Macro-Analysis capability to a dataframe'''
    def __init__(self, frame):
        self.csv = frame  # dataframe object

    def avg_discount_rate(self):
        '''Calculates average discount rate of all orders.'''
        # You should calculate the average and gross discount rate.
        pd.to_numeric(self.csv['Discount_Amount'])
        pd.to_numeric(self.csv['Order_Total_Amount'])
        total_sales_amount = self.csv['Order_Total_Amount'].sum()
        total_discount_amount = self.csv['Discount_Amount'].sum()
        total_discount_avg = int((total_discount_amount / (total_discount_amount+total_sales_amount))*100)
        return print(f'Customer Discount Avg: {total_discount_avg}%')


    def customer_role_breakdown(self):
        '''Calculates proportion of retail/wholesale as a function of sales.'''
        retail = 0
        wholesale = 0
        sum_count =int(len(self.csv.index))
        for i, row in self.csv.iterrows():
            if row.loc["Customer_Role"] == 'Customer':
                retail += int(row.loc["Order_Total_Amount"])
            else: wholesale += int(row.loc["Order_Total_Amount"])
        sum_sales = retail + wholesale
        counts = self.csv["Customer_Role"].value_counts().to_dict()
        roles = list(counts.keys())
        count = list(counts.values())
        data = zip(roles, count)
        c_role_dataframe = pd.DataFrame(data, columns = ['Roles', 'Count'])
        c_role_dataframe = c_role_dataframe[c_role_dataframe.Roles != 'Subscriber']
        c_role_dataframe.insert(2,column ='Sales_Total', value=[int(retail), int(wholesale)])
        c_role_dataframe['Average_Sale_Revenue']= c_role_dataframe['Sales_Total']/c_role_dataframe['Count']
        c_role_dataframe['Proportional_Sales'] = c_role_dataframe['Sales_Total']/sum_sales
        c_role_dataframe['Proportional_Count'] = c_role_dataframe['Count']/sum_count
        cdb_dv = ColumnDataSource(c_role_dataframe)
        roles = c_role_dataframe['Roles'].tolist()
        cdb_dv.data.keys()
        subkey_list = ['Proportional_Sales', 'Proportional_Count']
        visual = figure(x_range= roles, width=700, height=700,
                        title='Customer Role Sales Breakdown', x_axis_label='Roles',
                        y_axis_label='Proportionate Value', toolbar_location=None, tools='hover',
                        tooltips=[('Average Sale Revenue', '@Average_Sale_Revenue'),
                                  ]
                        )
        visual.vbar_stack(subkey_list, x='Roles', width=0.6, color=['green', 'yellow'],
                          source=cdb_dv, legend_label=subkey_list)
        show(visual)
        return print(c_role_dataframe)

    def geographical_breakdown(self):
        ''' Displays a scatterplot of Sales/Revenue weights for different States.'''
        self.csv = self.csv[self.csv.Country_Name_Shipping== 'United States (US)']
        counts = self.csv["State_Name_Shipping"].value_counts().to_dict()
        States = list(counts.keys())
        Count = list(counts.values())
        geo = pd.DataFrame({'States': States, 'Counts': Count})
        geo_dataframe = pd.DataFrame(geo)
        geo_dataframe.insert(loc=2, column="Sales_Total", value=0)
        geo_dataframe.insert(loc=3, column="Avg_Purchase_Revenue", value=0)
        for i, row in self.csv.iterrows():
            state = row.loc['State_Name_Shipping']
            total = row.loc['Order_Total_Amount']
            idx = geo_dataframe[geo_dataframe["States"] == state].index.item()
            av = int(geo_dataframe.at[idx, 'Sales_Total']) / int(geo_dataframe.at[idx, 'Counts'])
            geo_dataframe.at[idx, 'Sales_Total'] += total
            geo_dataframe.at[idx, 'Avg_Purchase_Revenue'] = av
        # data visualization
        cds = ColumnDataSource(geo_dataframe)
        cds.data.keys()
        visual = figure(tools='box_zoom, pan, reset',
                        width=700, height=700,
                        title='Geographical Sales Breakdown',
                        y_axis_label='Order Quantity', x_axis_label='Revenue')
        visual.circle('Sales_Total', 'Counts', size=7, source=cds, name= 'States')
        visual.add_tools(HoverTool(tooltips=[("State", "@States"),
                                             ("Average Purchase Revenue", "@Avg_Purchase_Revenue")
                                             ]))
        show(visual)
        return print(geo_dataframe)

class product_analysis:
    '''Arms Macro-Analysis capability to a dataframe'''

    def __init__(self, frame):
        self.csv = frame  # dataframe object
        self.time_span = None
        self.analysis_frame = self.monthly_product_frame()

    def monthly_product_frame(self):
        from datetime import datetime
        import information_repository as ir
        frame = self.csv
        frame = frame[['Order_Date', 'Product_Name', 'Quantity', 'Item_Cost']]
        dict_list = []
        for i, row in frame.iterrows():
            row_date = row['Order_Date']
            row_date = datetime.strptime(row_date, "%Y-%m-%d %H:%M")
            row_date_month = row_date.month
            row_date_year = row_date.year
            raw_products = row['Product_Name'].replace('\r', '').split('\n')
            raw_quantities = row['Quantity'].replace('\r', '').split('\n')
            raw_cost = row['Item_Cost'].replace('\r', '').split('\n')
            for key in range(len(raw_products)):
                product = [i for i in ir.p_list if i in raw_products[key]][0]
                quantity = int(raw_quantities[key])
                revenue = float(raw_cost[key])
                dict_object = [product, quantity, revenue, row_date_month, row_date_year]
                matched_dictionary = [i for i in dict_list if
                                      i['name'] == dict_object[0] and i['month'] == dict_object[3]
                                      and i['year'] == dict_object[4]]
                if len(matched_dictionary) == 1:
                    matched_dictionary[0]['count'] += dict_object[1]
                    matched_dictionary[0]['revenue'] += dict_object[2]
                else:
                    dict_list.append({'name': dict_object[0], 'count': dict_object[1],
                                      'revenue': dict_object[2], 'month': dict_object[3], 'year': dict_object[4]})
        self.analysis_frame = pd.DataFrame(columns=['year', 'month', 'count', 'revenue', 'change_over_month', 'product'])
        time_span = []
        for product in ir.p_list:
            product_dictionaries = sorted(
                sorted([i for i in dict_list if i['name'] == product], key=lambda x: x['month']
                       ), key=lambda x: x['year'])
            data_list = []
            year_list = []
            month_list = []
            for key in range(len(product_dictionaries)):
                if key > 0:
                    try:
                        change_over_month = (100 - round(
                            ((product_dictionaries[key]['revenue'] / product_dictionaries[key]['count'])
                             / (product_dictionaries[key - 1]['revenue'] / product_dictionaries[key - 1][
                                        'count'])) * 100))

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
                time_span = [*zip(year_list, month_list)]
            append_frame = pd.DataFrame(data=data_list,
                                        columns=['year', 'month', 'count', 'revenue', 'change_over_month', 'product'])
            self.analysis_frame = pd.concat([self.analysis_frame, append_frame], ignore_index=True)
        self.time_span = time_span
        return self.analysis_frame
    def product_change_over_month_analysis(self):
        year = int(input('Type the year you would like to query in yyyy format:  '))
        month = int(input('Type the month you would like to query:  '))
        print(month)
        data_slice = self.analysis_frame.loc[self.analysis_frame['month'] == month].loc[self.analysis_frame['year'] == year]
        data_slice.sort_values(by='change_over_month', inplace=True, ascending=False)
        print(data_slice.iat[0, 5])
        return print(data_slice.head(5))
    def product_line_change_over_month_analysis(self):
        import information_repository as ir
        year = int(input('Type the year you would like to query in yyyy format:  '))
        month = int(input('Type the month you would like to query:  '))
        product_line_list_of_lists = [ir.tea_product_list, ir.capsule_product_list, ir.smokeable_product_list,
                             ir.skincare_product_list, ir.superfood_product_list, ir.honey_product_list,
                             ir.tincture_product_list]
        product_line_strings = ['Tea', 'Capsules', 'Smokeables', 'Skincare', 'Superfood', 'Honey', 'Tinctures']
        product_line_append_list = []
        line_index_counter = 0
        for product_line in product_line_list_of_lists:
            line_list = []
            line_list.append(year)
            line_list.append(month)
            print(month)
            data_slice = self.analysis_frame.loc[self.analysis_frame['month'] == month].loc[self.analysis_frame['year'] == year].loc[
                self.analysis_frame['product'].isin(product_line)]
            avg_change_over_month = data_slice['change_over_month'].mean()
            line_list.append(avg_change_over_month)
            product_line = product_line_strings[line_index_counter]
            line_index_counter += 1
            print(product_line_list_of_lists)
            line_list.append(product_line)
            product_line_append_list.append(line_list)
        product_line_analysis_frame = pd.DataFrame(data=product_line_append_list,
                                                   columns=['year', 'month', 'avg_change_over_month',
                                                            'product_line'])
        print(product_line_analysis_frame.head(5))
        '''Functional but unweighted averages: Need to find sum of product line revenue and weight changeover month 
        by the fraction of total product line sales each sku comprises.'''


