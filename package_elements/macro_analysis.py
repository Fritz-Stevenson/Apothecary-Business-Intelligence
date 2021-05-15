import pandas as pd
from bokeh.plotting import figure, save, show,output_file, ColumnDataSource
from bokeh.models import HoverTool
import matplotlib.pyplot as plt

class DataFrameAnalysis:
    """Arms Macro-Analysis capability to a dataframe"""
    def __init__(self, frame):
        self.df = frame  # dataframe object

    def avg_discount_rate(self):
        """Calculates average discount rate of all orders."""
        # You should calculate the average and gross discount rate.
        pd.to_numeric(self.df['Discount_Amount'])
        pd.to_numeric(self.df['Order_Total_Amount'])
        total_sales_amount = self.df['Order_Total_Amount'].sum()
        total_discount_amount = self.df['Discount_Amount'].sum()
        total_discount_avg = int((total_discount_amount / (total_discount_amount+total_sales_amount))*100)
        return print(f'Customer Discount Avg: {total_discount_avg}%')


    def customer_role_breakdown(self):
        """Calculates proportion of retail/wholesale as a function of sales."""
        retail = 0
        wholesale = 0
        sum_count =int(len(self.df.index))
        sum_sales = self.df['Order_Total_Amount'].sum()
        retail_customer_count = round((len(self.df.loc[self.df['Customer_Role']=='Customer'].index)/sum_count)*100)
        wholesale_customer_count = round((len(self.df.loc[self.df['Customer_Role']=='Wholesale Customer'].index)/sum_count)*100)
        retail_sales = round((self.df['Order_Total_Amount'].loc[self.df['Customer_Role']=='Customer'].sum()/sum_sales)*100)
        wholesale_sales = round((self.df['Order_Total_Amount'].loc[self.df['Customer_Role']=='Wholesale Customer'].sum()/sum_sales)*100)
        grid = [[retail_customer_count,wholesale_customer_count],[retail_sales,wholesale_sales]]
        crb_df = pd.DataFrame(data=grid, columns=['Retail','Wholesale'], index=['Proportional Order Counts', 'Proportional Sales'])
        plt.style.use('seaborn-deep')
        fig, ax = plt.subplots(figsize=(10, 10))
        crb_df.plot.bar(title='Customer Role Breakdown', xlabel='Customer Role', ylabel='Proportion (%)',
                        cmap='winter', ax=ax)
        plt.figsave('Customer_Role_Breakdown.png')
        print(crb_df.head(3))

    def geographical_breakdown(self):
        """ Displays a scatterplot of Sales/Revenue weights for different States."""
        self.df = self.df[self.df.Country_Name_Shipping== 'United States (US)']
        counts = self.df["State_Name_Shipping"].value_counts().to_dict()
        States = list(counts.keys())
        Count = list(counts.values())
        geo = pd.DataFrame({'States': States, 'Counts': Count})
        geo_dataframe = pd.DataFrame(geo)
        geo_dataframe.insert(loc=2, column="Sales_Total", value=0)
        geo_dataframe.insert(loc=3, column="Avg_Purchase_Revenue", value=0)
        for i, row in self.df.iterrows():
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
        output_file('geographical_breakdown.html')
        save(visual)
        show(visual)
        return print(geo_dataframe)


class ProductAnalysis:
    """Arms product analysis capability to a dataframe"""

    def __init__(self, frame):
        self.df = frame  # dataframe object
        self.analysis_frame = self.monthly_product_frame()
        self.time_span = self.serve_time_span()  # list of tuples: x[0] == year, x[1] == month for x in self.time_span

    def monthly_product_frame(self):
        """Analyzes the order lines in the CSV_Files folder and
        Returns a pandas Dataframe with monthly product statistics."""
        from datetime import datetime
        import information_repository as ir
        frame = self.df
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

    def highest_positive_product_change_over_month_analysis(self):
        """Analyzes the monthly_product_frame and returns the 5 products whose sales level increased the most"""
        year = int(input('Type the year you would like to query in yyyy format:  '))
        month = int(input('Type the month you would like to query:  '))
        data_slice = self.analysis_frame.loc[self.analysis_frame['month'] == month].loc[self.analysis_frame['year'] == year].loc[self.analysis_frame['revenue']>500]
        data_slice.sort_values(by='change_over_month', inplace=True, ascending=False)
        return print(data_slice.head(5))

    def highest_negative_product_change_over_month_analysis(self):
        """Analyzes the monthly_product_frame and returns the 5 products whose sales level decreased the most"""
        year = int(input('Type the year you would like to query in yyyy format:  '))
        month = int(input('Type the month you would like to query:  '))
        data_slice = self.analysis_frame.loc[self.analysis_frame['month'] == month].loc[self.analysis_frame['year'] == year].loc[self.analysis_frame['revenue']>500]
        data_slice.sort_values(by='change_over_month', inplace=True, ascending=True)
        return data_slice

    def product_line_change_over_month_analysis(self, year, month):
        """Analyzes the monthly_product_frame by product line and returns a dataframe with
        product line change over month data."""
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
            data_slice = self.analysis_frame.loc[self.analysis_frame['month'] == month].loc[
                self.analysis_frame['year'] == year].loc[self.analysis_frame['product'].isin(product_line)]
            if month > 1:
                last_month_frame = self.analysis_frame.loc[self.analysis_frame['month'] == (month - 1)].loc[
                    self.analysis_frame['year'] == year].loc[self.analysis_frame['product'].isin(product_line)]
            else:
                last_month_frame = self.analysis_frame.loc[self.analysis_frame['month'] == 12].loc[
                    self.analysis_frame['year'] == (year - 1)].loc[self.analysis_frame['product'].isin(product_line)]
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
        product_line_analysis_frame.to_csv('product_line_csv_2021.csv')
        return product_line_analysis_frame

    def serve_time_span(self):
        """Returns a list of tuples of unique (year, month) pairs in chronological order based on the
         monthly_product_frame."""
        return sorted(sorted(list(set([*zip(self.analysis_frame['year'],self.analysis_frame['month'])])),
                            key=lambda x:x[1]), key=lambda x:x[0])

    def product_line_change_over_month_graph(self):
        """Using the product_line_change_over_month_analysis frame, it outputs a graph of the changes over time for
        the top product lines."""
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
        output_file('product_line_change_over_month.html')
        save(graph)
        return show(graph)


class InventoryPredictor:
    """Inventory volume prediction using a product sales csv as the raw data."""
    def __init__(self):
        import information_repository as ir
        self.unit_counts = self.sales_unit_count_dictionaries()
        self.ingredients = self.ingredient_dictionary()
        self.recipes = ir.unit_recipes

        print('initiating')
        pass

    def sales_unit_count_dictionaries(self):
        """Creates a set of dictionaries for each product and the cumulative quantity of units across all SKUs."""
        import information_repository as ir
        product_sales_frame = pd.read_csv('product_sales.csv')
        product_sales_frame = product_sales_frame.where(pd.notnull(product_sales_frame), 'None')
        product_unit_amounts = []
        for i in ir.p_list:
            product_dict = dict(name=i, quantity=0)
            for x, row in product_sales_frame.iterrows():
                if i in row['Product Name']:
                    if i in ir.tea_product_list:
                        if '1' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold']
                        elif '3' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 3
                        elif '20' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 20
                        else:
                            pass
                            # print('Something unexpected occured', row['Product Name'], row['Variation Attributes'])
                    elif i in ir.superfood_product_list:
                        if '3' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold']
                        elif '9' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 3
                        else:
                            product_dict['quantity'] += 1
                    elif i in ir.capsule_product_list:
                        if '1' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold']
                        if '4' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 4
                    elif i in ir.smokeable_product_list:
                        if '7' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 7
                        elif 'prerolls' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 2
                        else:
                            product_dict['quantity'] += row['Quantity Sold'] * 4
                    elif i in ir.honey_product_list:
                        if '3' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 3
                        elif '5' in row['Variation Attributes']:
                            product_dict['quantity'] += row['Quantity Sold'] * 5
                        elif '2' in row['Variation Attributes']:
                            pass
                            # print('Reminder that packet honeys and jars need to separate')
                    else:
                        product_dict['quantity'] += row['Quantity Sold']
            product_unit_amounts.append(product_dict)
        return product_unit_amounts

    def ingredient_dictionary(self):
        """Creates a ingredient dictionary with all ingredients as keys and the cumulative volume across all
        products as values."""
        inventory = pd.read_csv('craftybase-export-material.csv')
        ingredient_dictionary = {}
        for i in list(inventory['name']):
            ingredient_dictionary[i]=0
        return ingredient_dictionary

    def ingredient_volume_table(self):
        """Creates a csv with ingredients and the cumulative volume used across a time span."""
        for x in self.unit_counts:
            for y in self.recipes:
                if x['name'] == y['name']:
                    for k, v in y.items():
                        if k != 'name':
                            self.ingredients[k] += v * x['quantity']
        sorted_ingredient_volumes = sorted(self.ingredients.items(), key=lambda x: x[1], reverse=True)
        output_frame = pd.DataFrame(data = sorted_ingredient_volumes, columns= ['Ingredient', 'Volume (gram or oz)'])
        output_frame = output_frame[output_frame['Volume (gram or oz)'] !=0]
        output_frame.to_csv('ingredient_volume_table.csv')


