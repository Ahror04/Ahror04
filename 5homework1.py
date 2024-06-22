# 1.date yordamida Xafta kuni tartib raqami ekranga chiqarilsin

# 2.python yordamida 1 oylik va bir yillik kalendar ekranga chiqarilsin


# 3. 2 ta berilgan sanadan eng kattasini aniqlovchi big-date nomli funksiya yozing


# 4. time moduli yordamida bugungi sanani quyidagi formatda ekranga chiqarilsin 

# Today:
# Monday 21 October 2017 17:38:31
# 21.11.2017

# 5.2023 yil kalendarini HTML formatda ekranga chiqarilsin

# 4-masala

# import datetime
# import time
# today = datetime.datetime.now()
# print("today:" ,today.strftime("%A "),today.day,today.strftime("%B"),today.strftime("%Y-%H-%M-%S"))


# 3-masala

# import datetime
# import time

# def big_date(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a=datetime.date(2024,10,12)
# b=datetime.date(2025,10,12)
# print(big_date(a,b))


# 1-masala

# import datetime
# import time

# week=datetime.datetime.now()
# print(week.isoweekday())

# 2-masala
# 1-variant
# import calendar
# yy=2024
# mm=6
# print(calendar.month(yy,mm))
# print(calendar.calendar(yy))

# 2-variant


# import calendar
# from datetime import datetime

# now = datetime.now()
# year = now.year
# month = now.month

# cal = calendar.TextCalendar()

# current_month = cal.formatmonth(year,month)

# current_year= cal.formatyear(year)

# print(current_month)

# print(current_year)


# 5-masala

import datetime
import calendar

cal = calendar.HTMLCalendar()
year=2023

with open("cal.html", "w") as f:
    f.write(cal.formatyear(year))
    print(cal.formatyear(year)) 
            

