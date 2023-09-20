import datetime
from datetime import timedelta

y = int(input("Input a year: "))
m = int(input("Input a month [1-12]: "))
d = int(input("Input a day [1-31]: "))

gDate = datetime.datetime(y, m, d)
print("Given date is: ", gDate)

next = gDate + timedelta(days=1)
print("The next date is: ", next)
