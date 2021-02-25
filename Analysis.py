import pandas as pd
import utility as u

df1 = pd.read_csv("CSV_Files\\1-22Export1.csv")
df2 = pd.read_csv("CSV_Files\\1-22Export2.csv")
df3 = pd.read_csv("CSV_Files\\1-22Export3.csv")
df4 = pd.read_csv("CSV_Files\\1-22Export5.csv")
df5 = pd.read_csv("CSV_Files\\1-22Export6.csv")
df6 = pd.read_csv("CSV_Files\\1-25Sept2020.csv")

df1.insert(loc=0 , column ='Month', value= 'December')
df2.insert(loc=0 , column ='Month', value= 'November')
df3.insert(loc=0 , column ='Month', value= 'October')
df6.insert(loc=0, column ='Month', value= 'September')
df4.insert(loc=0 , column ='Month', value= 'August')
df5.insert(loc=0 , column ='Month', value= 'July')

concat = pd.concat([df1,df2,df3,df6,df4,df5], ignore_index=True)
concat.to_csv("Raw_Analysis.csv", index=False)

file = pd.read_csv('CSV_Files\\Raw_Analysis.csv')
# Test slice for functionality
file = u.clean(file)
file = file.head(2)
cp1 = u.FieldLoader(file)



'''Work log:
2/25
functionality and indexing for time: reading, saving and analyzing time fields
make read-me and streamline initialization
Create a log.txt file for running the customer profile module: We need to know when it is edited***(But then how do you 
make the log compatible with file deletion and restarting? Manual addition?)***

final steps:
how to access customer profiles
displaying analysis in a customizable format
'''

'''Entomology

--Dates may be out of order (oldest to newest) They must be sorted be as the customer profile is called (code in test)
'''