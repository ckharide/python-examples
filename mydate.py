from datetime import datetime 
from datetime import date
from time import time

now = datetime.now()
print(now)

formatted_time = now.strftime("%m/%d/%Y, %H:%M:%S")
formatted_time_second = now.strftime("%y/%m/%d")
print(formatted_time)
print(formatted_time_second)


today = date(year=2022, month=4, day=14)
new_year = date(year=2023, month=1, day=1)
print ("Number of days left " , new_year - today)

print("Formamated time " , now.strftime("%Y %B %d"))