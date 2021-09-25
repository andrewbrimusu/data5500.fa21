import requests
import json

    
ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
print(url)
request = requests.get(url)
#print(request.text)

rqst_dict = json.loads(request.text)
print(rqst_dict)

json.dump(rqst_dict, open(ticker+".json", "w"))

new_dict = json.load(open(ticker+".csv"))



















# solution
url = "https://api.datamuse.com/words?ml=duck&sp=b*&max=3"
request = requests.get(url)
dict = json.loads(request.text)
json.dump(dict, open("words.json", "w"))
