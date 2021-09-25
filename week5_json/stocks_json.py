import requests
import json

    
ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
print(url)
request = requests.get(url)
print(request.text)
input()

key1 = "Time Series (Daily)"
key3 = "4. close"

dct1 = json.loads(request.text)

# print(dct1.keys())
# print(dct1[key1].keys())

for date in dct1[key1].keys():
    print(dct1[key1][date][key3])

# rqst_dict = json.loads(request.text) # load web request into python dictionary

# json.dump(rqst_dict, open(ticker+".json", "w")) # save dictionary to json file

# new_dict = json.load(open(ticker+".csv")) # reload json file back into a python dictionary

