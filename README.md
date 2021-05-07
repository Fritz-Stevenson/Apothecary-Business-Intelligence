# Business-Data-Analysis
***Sales data analysis and the creation of a customer profile database.***

**Analysis Overview**

This data analysis project is built for a small business with a large range of products and fairly high variability in sales trends. Products and even product lines can vary greatly in terms of sales change month over month. In order to maintain stock of inventory and ingredients, and pinpoint potential quality assurance problems, it is important to understand generalized trends and outliers. This Analysis Project tackles this problem as well as addressing inventory purchasing, promotional email lists based on time since last order, and the creation of a customer profile database to pinpoint sales trends on a customer basis.


**Analysis instructions:**

In order to utilize this program, one must have access to the appropriate data and insert it into the program folder in the appropriate way. A virtual environment also must be set up to satisfy python module dependancies.

You will need to set up a virtual environment in the downloaded program folder and install the requirements.txt. 

Here is the python documentation: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

You will need to download the most recent csv files as well:

craftybase-export-material.csv (From the Material section of craftybase. Check that the title of the file is identical)

product_sales.csv (From the wp site, click the product sales export sub section of the woocommerce app. Exporting processing and completed orders for the last 30 days.)

all monthly csv files placed in the CSV_Files folder :
  Format as ordersYY-MM.csv so that the folder is in chronological order.
  Keep in mind that all csv files will be included in the analysis functions. If you want discount data for a single month, make sure a single month is present in the folder.
  for full functionality the csvs must have the following columns in order:

Order Date,

Email (Billing)

Full Name (Billing)

Customer Role

Customer first order date

Customer last order date

Customer Total Orders

Customer Total Spent

Full Name (Shipping)

Address 1 (Shipping)

City (Shipping)

State Name (Shipping)

Postcode (Shipping)

Product Name

Item Cost

Item Name

Quantity

Discount Amount

Order Total Amount

#Currently, the optimal method of running files from this directory is depositing all of the files in the repository in an IDE such as pycharm and calling functions manually.

***This Program will ideally be run in a command line, through system arguments/sys.argv[1] While not yet implemented, which will include the following:***
geo : geographical scatterplot
discount : printed average discount rate for the period
role : customer role table
inventory : outputs csv file in program folder with volumes of each ingredient over the period
pcp : products with greatest positive change in sales (requires more than one month in CSV_Files)
ncp : products with greatest negative change in sales (requires more than one month in CSV_Files)
plg : graph of product line sales' change over month (requires more than one month in CSV_Files)

**To run the following commands, navigate to the program folder in the cmd application, activate the virtual env using the docs linked above, and input**
**"python3 analysis.py x" where x is on of the above arguments
***The following will be edited into the Analysis.py file before it is run from the command line or an ide like pycharm.***


#CUSTOMER_PROFILE
***Customer Profiles are sensitive documents that need to be maintained and accessed carefully
For this reason, there is a log.txt file that denotes the time and timeframe of database calls for cpm(in progress)
If you need to start fresh. Load every available unique sales csv into the CSV_FIles and initialize like you would
for the macro analysis above. Then delete all existing files in retail/wholesale customers and continue***

First initialize using the initialize procedure above. You need to first feed the dataframe into the FieldLoader class
in the utility module ie #loader = u.FieldLoader(frame)# where frame is the initialized dataframe. 

By this point, All customer profiles necessary should be created/updated. 

The zipped values are then inputted into the act_salesrow_class function to activate the class over the list of rows.
This should complete the update of profile csv files'''
