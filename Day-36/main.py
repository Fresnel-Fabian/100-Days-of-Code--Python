import requests
from datetime import datetime as dt
from datetime import timedelta as td
stock_key = "QQLOBSX1QH3P1C98"

yesterday = dt.now() - td(1)
day_before = dt.now() - td(2)
print(yesterday.strftime("%Y-%m-%d"))
print(day_before.strftime("%Y-%m-%d"))