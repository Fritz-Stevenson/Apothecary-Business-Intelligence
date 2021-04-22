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

class ProductAnalysis:
    '''Arms product analysis capability to a dataframe'''

    def __init__(self, frame):
        self.csv = frame  # dataframe object
        self.analysis_frame = self.monthly_product_frame()
        self.time_span = self.serve_time_span()  # list of tuples: x[0] == year, x[1] == month for x in self.time_span

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
        data_slice = self.analysis_frame.loc[self.analysis_frame['month'] == month].loc[self.analysis_frame['year'] == year].loc[self.analysis_frame['revenue']>500]
        data_slice.sort_values(by='change_over_month', inplace=True, ascending=False)
        return print(data_slice.head(5))

    def product_line_change_over_month_analysis(self, year, month):
        import information_repository as ir
        #year = int(input('Type the year you would like to query in yyyy format:  '))
        #month = int(input('Type the month you would like to query:  '))
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
            data_slice = self.analysis_frame.loc[self.analysis_frame['month'] == month].loc[self.analysis_frame['year'] == year].loc[
                self.analysis_frame['product'].isin(product_line)]
            if month > 1:
                last_month_frame = self.analysis_frame.loc[self.analysis_frame['month'] == (month - 1)].loc[self.analysis_frame['year'] == year].loc[
                    self.analysis_frame['product'].isin(product_line)]
            else:
                last_month_frame = self.analysis_frame.loc[self.analysis_frame['month'] == 12].loc[self.analysis_frame['year'] == (year - 1)].loc[
                    self.analysis_frame['product'].isin(product_line)]
            last_month_revenue = last_month_frame['revenue'].sum()
            this_month_revenue = data_slice['revenue'].sum()
            avg_change_over_month = (this_month_revenue / last_month_revenue) * 100
            line_list.append(avg_change_over_month)
            product_line = product_line_strings[line_index_counter]
            line_index_counter += 1
            line_list.append(product_line)
            product_line_append_list.append(line_list)
        product_line_analysis_frame = pd.DataFrame(data=product_line_append_list,
                                                   columns=['year', 'month', 'avg_change_over_month',
                                                            'product_line'])
        return product_line_analysis_frame

    def serve_time_span(self):
        return sorted(sorted(list(set([*zip(self.analysis_frame['year'],self.analysis_frame['month'])])),
                            key=lambda x:x[1]), key=lambda x:x[0])

    def product_line_change_over_month_graph(self):
        line_change_frame_data = []
        for i in self.time_span:
            month_frame = self.product_line_change_over_month_analysis(i[0], i[1])
            change_list = month_frame['avg_change_over_month']
            line_change_frame_data.append(change_list)
        treated_line_change_frame_data = []
        for i in range(len(line_change_frame_data)): #index of time period/segment
            if i ==0:
                treated_line_change_frame_data.append([self.time_span[i][0], self.time_span[i][1],
                                                       0,0,0,0,0,0,0]) #insert base amounts for the first month
            else: #function as intended
                month_cumulative_change_list = []
                month_cumulative_change_list.append(self.time_span[i][0])
                month_cumulative_change_list.append(self.time_span[i][1])# append year and month
                for x in range(len(line_change_frame_data[0])):
                    prior_change_list = [i[x] for i in line_change_frame_data]
                    product_cumulative_change = (100+treated_line_change_frame_data[i-1][x+2]) * ((prior_change_list[i]/100))-100
                    #i-1 for previous time period and x+2 for offset due to year and month category
                    month_cumulative_change_list.append(product_cumulative_change)
                treated_line_change_frame_data.append(month_cumulative_change_list)
        graph_frame = pd.DataFrame(data=treated_line_change_frame_data, columns=['Year', 'Month', 'Tea', 'Capsules', 'Smokeables','Skincare',
                                                                           'Superfood', 'Honey', 'Tinctures'])
        print(graph_frame.head(7))
        x = [str(i) for i in graph_frame['Month']]
        y1 = graph_frame['Tea']
        y2 = graph_frame['Capsules']
        y3 = graph_frame['Superfood']
        y4 = graph_frame['Honey']
        y5 = graph_frame['Smokeables']
        graph = figure(x_range=x,title='Cumulative Percentage Change of Product Lines',x_axis_label='Month', y_axis_label='Percentage Change')
        graph.line(x, y1, legend_label ='Tea', color='red', line_width=3)
        graph.line(x, y2, legend_label ='Capsules', color='blue', line_width=3)
        graph.line(x, y3, legend_label ='Superfood', color='orange', line_width=3)
        graph.line(x, y4, legend_label ='Honey', color='yellow', line_width=3)
        graph.line(x, y5, legend_label ='Smokeables', color='green', line_width=3)
        return show(graph)
        '''At the moment, the structure for the graph frame is in place, but the product_cumulative change variable is 
        likely the cause of problems. Needs debugging.'''


import utility as u
object = u.clean(u.concat('CSV_Files'))
a = ProductAnalysis(object)
a.product_line_change_over_month_graph()
