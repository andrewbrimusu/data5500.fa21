import requests
import json
import time
from datetime import datetime, timedelta

url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=02-01-2020&localization=false" #January 2nd, 2020

# url1 = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date="
# url2 = "&localization=false"


# dt = datetime(2020, 12, 31) # start january
# dt += timedelta(days=1) 
# dts = dt.strftime("%d-%m-%Y")

# url = url1 + dts + url2
print("url: ", url)
input("press any key")

req = requests.get(url)
print(req.text)

# stock example
ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
print(url)
request = requests.get(url)
print(request.text)
input("press any key")

