import requests
import json
import time
from datetime import datetime, timedelta

url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=02-01-2020&localization=false" #January 2nd, 2020

url1 = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date="
url2 = "&localization=false"

key1 = "market_data"
key2 = "current_price"
key3 = "usd"

dt = datetime(2020, 1, 2) # start january
for i in range(100):
    dt += timedelta(days=1) 
    dts = dt.strftime("%d-%m-%Y")
    
    url = url1 + dts + url2
    print("url: ", url)
    # input("press any key")
    
    req = requests.get(url)
    # print(req.text)
    dct1 = json.loads(req.text)
    print(dct1[key1][key2][key3])
    
    time.sleep(1)
    

# # stock example

# ticker = 'AAPL'
# url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
# print(url)
# request = requests.get(url)
# # print(request.text)

# dct1 = json.loads(request.text)
# print(dct1)



# key1 = "Time Series (Daily)"
# # date key
# key3 = "4. close"

# for item in dct1[key1]:
#     print(item)
#     print(dct1[key1][item][key3])
    
    



    

input("press any key")
