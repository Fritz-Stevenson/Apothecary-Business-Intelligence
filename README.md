# Business-Data-Analysis
***Sales data analysis and the creation of a customer profile database.***

**Analysis instructions:**

First, download the sales export as a csv from the woocommerce app in the wordpress engine.
The fields should be in the following order, as concatenation will disjoint columns if column names aren't identical,
making other functions useless.

Order Date,

Email (Billing)

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

In my experience, the time frame on the export field may need to be as little as 1 month due to a download time cap.

First drag the csv or csvs to be used for analysis into the CSV_Files folder. Then verify that there is not csv in the 
CSV_Files folder that you would like concatenated together to your final csv.

#MACRO_ANALYSIS
***The following will be edited into the Analysis.py file before it is run from the command line or an ide like pycharm.***

**INITIALIZE**

To initialize the dataframe you can use the concat function from the utility module. This will create a dataframe by 
concatenating csv(s) in the CSV_Folder. The field required is the folder path ie. 
--frame = utility.concat('.\\folder_name'). 
All CSVs in the folder will be added to the dataframe. Be careful not to include duplicates. Clean the dataframe in 
question using utilty.clean ie. 

--frame = utility.clean(frame)

At this point the macro_analysis module is able to be utilized
Analysis.py has already imported macro_analysis as ma. Initialize the object by calling 

--analysis = ma.dataframe_analysis(frame),

where frame refers to the previously cleaned dataframe you can then call the class functions using analysis.x where x is one of the functions.
Some analyses include geographical_breakdown, customer_role_breakdown, avg_discount_rate.
Most of these analyses should create data vizualizations as an html page in your default browser.
If they do not automatically open, check your firewall or browser access permissions. 

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