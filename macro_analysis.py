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
    def product_analysis(self):
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
        big_frame = pd.DataFrame(columns=['year', 'month', 'count', 'revenue', 'change_over_month', 'product'])
        time_span = []
        for product in ir.p_list:
            product_dictionaries = sorted(
                sorted([i for i in dict_list if i['name'] == product], key=lambda x: x['month'],
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
                        change_list.append(
                            round((((product_dictionaries[key]['revenue'] / product_dictionaries[key]['count'])
                                   / (product_dictionaries[key - 1]['revenue'] / product_dictionaries[key - 1][
                                        'count'])) * 100), 1))
                    except IndexError:
                        print('change_list calls need to be refined')
                else:
                    change_list.append(0)
            if product == 'Blue Moon':
                time_span.append(*zip(year_list, month_list))
            append_frame = pd.DataFrame([year_list, month_list, count_list, revenue_list, change_list, product_list])
            big_frame = pd.concat([big_frame, append_frame], ignore_index=True)
        '''Now analyze the big_frame: for i in time_span: find the 3-5 highest change_over_months and create a new table or 
            something. Organize by product line and avg() the change_over_month values for yet another table. Find the highest
            positive change_over month values for the last month.'''


