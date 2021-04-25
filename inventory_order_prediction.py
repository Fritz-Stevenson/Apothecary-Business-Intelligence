import pandas as pd
import information_repository as ir
class InventoryPredictor:
    def __init__(self):
        self.unit_counts = self.sales_unit_count_dictionaries()
        self.ingredients = self.ingredient_dictionary()
        self.recipes = ir.unit_recipes

        print('initiating')
        pass
    def sales_unit_count_dictionaries(self):
        product_sales_frame = pd.read_csv('Product Sales.csv')
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
                            print('Something unexpected occured', row['Product Name'], row['Variation Attributes'])
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
                            #print('Reminder that packet honeys and jars need to separate')
                    else:
                        product_dict['quantity'] += row['Quantity Sold']
            product_unit_amounts.append(product_dict)
        return product_unit_amounts
    def ingredient_dictionary(self):
        inventory = pd.read_csv('craftybase-export-material.csv')
        ingredient_dictionary = {}
        for i in list(inventory['name']):
            ingredient_dictionary[i]=0
        return ingredient_dictionary
    def ingredient_volume_table(self):
        for x in self.unit_counts:
            for y in self.recipes:
                if x['name'] == y['name']:
                    for k, v in y.items():
                        if k != 'name':
                            self.ingredients[k] += v * x['quantity']
                            print(f'{x["name"]} {k} {self.ingredients[k]} current ingredient volume')
        sorted_ingredient_volumes = sorted(self.ingredients.items(), key=lambda x: x[1], reverse=True)
        output_frame = pd.DataFrame(data = sorted_ingredient_volumes, columns= ['Ingredient', 'Volume (gram or oz)'])
        output_frame = output_frame[output_frame['Volume (gram or oz)'] !=0]
        output_frame.to_csv('Ingredient_Volume_Table.csv')
