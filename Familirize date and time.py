'''
Author:Rayan Joomy
Date:19-10-2024
Title:To work with time and date in various formats in Python, you can use the datetime module.

-This module allows you to format dates and times in different ways using strftime() and parse them using strptime().
'''
from datetime import datetime
current_time = datetime .now()
print(current_time)
format_1=current_time. strftime("%Y-%m-%d-%H-%M:%S")
print(format_1)