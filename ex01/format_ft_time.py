import time
from decimal import Decimal
import calendar

x = time.time()

print("Seconds since January 1, 1970:", "{:,.4f}".format(x), "or", "{:.2e}".format(x), "in scientific notation")
month = str(calendar.month_name[time.gmtime(x).tm_mon])[:3]
date = time.gmtime(x)
print(month, date.tm_mday, date.tm_year)