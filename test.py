from datetime import datetime
date_1 ='2020-12-31 23:52'
date_2 = datetime.now()
date_2 = date_2.strftime("%Y-%m-%d %H:%M")
date_3 = '2020-06-12 23:52'
date_4 = '2020-03-05 23:52'
date_list = [date_1, date_2, date_3, date_4]
date_list.sort()
print(date_list)
date_1 = datetime.strptime(date_1, "%Y-%m-%d %H:%M")
date_2 = datetime.strptime(date_2, "%Y-%m-%d %H:%M")
date_3 = datetime.strptime(date_3, "%Y-%m-%d %H:%M")
date_4 = datetime.strptime(date_4, "%Y-%m-%d %H:%M")
date_list = [date_1, date_2, date_3, date_4]

date_list.sort()
print(date_list)
