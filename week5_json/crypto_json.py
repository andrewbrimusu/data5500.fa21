import requests
import json
import time
from datetime import datetime, timedelta

# url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=02-14-2022&localization=false" #January 2nd, 2020

url1 = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date="
url2 = "&localization=false"


dt = datetime(2022, 1, 1) # start january
dt += timedelta(days=1) 
dts = dt.strftime("%d-%m-%Y")

url = url1 + dts + url2
print("url: ", url)
input()

req = requests.get(url)
print(req.text)
input()

dct1 = json.loads(req.text)

print(dct1.keys())

key1 = "market_data"
key2 = "current_price"
key3 = "usd"

print(dct1[key1][key2][key3])



























# key1 = "market_data"

# # print(dct1[key1])

# key2 = "current_price"
# # print(dct1[key1][key2])

# key3 = "usd"
# print(dct1[key1][key2][key3])

# for i in range(45):
#     dt += timedelta(days=1) 
#     dts = dt.strftime("%d-%m-%Y")
#     url = url1 + dts + url2
#     req = requests.get(url)
#     dct1 = json.loads(req.text)
#     print(dts, ": ", dct1[key1][key2][key3])
    
