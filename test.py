p_list = ['ala', 'rast', 'foobar']
input_cell = ['ala baster', 'rast er', 'foobar a']
import re
def product_regex(input_cell):
    products = []
    for i in p_list:
        print(i)
        regex = re.compile(r'(%s)' % i)
        for o in input_cell:
            r = regex.match(o)
            if r:
                print(str(r.groups(0)))
                obj = str(r.groups(0)).replace('(','')
                obj = obj.replace(')','')
                obj = obj.replace('\'','')
                obj = obj.replace(',','')
                products.append(obj)
    return print(products)
# product_regex(input_cell)
def simpler_function(inp):
    li =[]
    for i in p_list:
        for o in inp:
            if i in o:
                li.append(i)
    return print(li)
a = simpler_function(input_cell)
print(f'a: {a}')