from datetime import datetime 

now = datetime.now()
print(now)

formatted_time = now.strftime("%m/%d/%Y, %H:%M:%S")
formatted_time_second = now.strftime("%y/%m/%d")
print(formatted_time)
print(formatted_time_second)