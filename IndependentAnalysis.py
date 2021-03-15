import pandas as pd

#missing csv named concat, can substitute Raw_Analysis.csv

customer_profile = concat[["Email (Billing)", "Full Name (Shipping)", "Customer Total Orders",
                           "Customer Total Spent","Customer Role"]]
customer_profile.to_csv("customer_profile.csv", index=False)
o_c = []
n_c = []
i_list=[]

# Basis for row analysis used to later create the customer profile

for i, row in customer_profile.iterrows():
    i_list.append(i)
    role = customer_profile.loc[i,"Customer Role"]
    order_number = customer_profile.loc[i,"Customer Total Orders"]
    gross = customer_profile.loc[i,"Customer Total Spent"]
    if role == "Customer":
        if int(order_number)>=5:
            o_c.append(customer_profile.loc[i])
        elif int(order_number)<=2:
            n_c.append(customer_profile.loc[i])

# Create a list of old and new customers based on how many times they have ordered.

new_customers = pd.DataFrame(n_c, columns=["Email (Billing)", "Full Name (Shipping)", "Customer Total Orders",
                                           "Customer Total Spent","Customer Role"])
old_customers = pd.DataFrame(o_c, columns=["Email (Billing)", "Full Name (Shipping)", "Customer Total Orders",
                                           "Customer Total Spent","Customer Role"])
old_customers.drop_duplicates(subset ="Full Name (Shipping)", keep = False, inplace = True)
new_customers.drop_duplicates(subset ="Full Name (Shipping)", keep = False, inplace = True)
old_customers.to_csv("old_customers.csv", index=False)
new_customers.to_csv("new_customers.csv", index=False)
