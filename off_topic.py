import pandas as pd
import information_repository as ir
import utility as u
product_sales_frame = pd.read_csv('Product Sales.csv')
product_sales_frame = product_sales_frame.where(pd.notnull(product_sales_frame), 'None')
product_unit_log= []
for i in ir.p_list:
    product_dict = dict(name=i, quantity=0)
    for x, row in product_sales_frame.iterrows():
        print(type(row['Variation Attributes']), row['Variation Attributes'])
        if i in row['Product Name']:
            if i in ir.tea_product_list:
                if '1' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']
                elif '3' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*3
                elif '20' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*20
                else:
                    print('Something unexpected occured')
            elif i in ir.superfood_product_list:
                if '3' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']
                elif '9' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*3
                else:
                    product_dict['quantity']+=1
            elif i in ir.capsule_product_list:
                if '1' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']
                if '4' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*4
            elif i in ir.smokeable_product_list:
                if '7' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*7
                elif 'prerolls' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*2
                else:
                    product_dict['quantity'] += row['Quantity Sold']*4
            elif i in ir.honey_product_list:
                if '3' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*3
                elif '5' in row['Variation Attributes']:
                    product_dict['quantity'] += row['Quantity Sold']*5
                elif '2' in row['Variation Attributes']:
                    print('Reminder that packet honeys and jars need to separate')
            else:
                product_dict['quantity'] += row['Quantity Sold']
    product_unit_log.append(product_dict)
print(product_unit_log)