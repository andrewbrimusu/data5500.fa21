# the logic to save multiple coins to multiple csv files
import requests
import json
import time
from datetime import datetime, timedelta


url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

key1 = 'market_data'
key2 = 'current_price'
key3 = 'usd'

dt = datetime(2019, 11, 30)

coins = ["ripple", "cardano", "bitcoin-cash", "eos", "litecoin", "ethereum", "bitcoin"]

for coin in coins:
    file = open(coin + ".csv", "w")
    file.write("Date," + coin + "\n")
    for i in range(364):
        dt += timedelta(days=1)
        dts = dt.strftime("%d-%m-%Y")
        url = url1 + coin + url2 + dts + url3
        print("url: ", url)
        req = requests.get(url)
        time.sleep(1)
        d = json.loads(req.text)
        # try:
        print(dts, d[key1][key2][key3])
        file.write(dts + "," + str(d[key1][key2][key3]) + "\n")

        # except:
            # pass
            # print(d)
            
file.close()