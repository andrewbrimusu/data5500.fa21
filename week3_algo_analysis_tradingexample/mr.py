import numpy as np
import os
# os.system("pip3 install numpy")


prcs = [float(x) for x in open("/home/ubuntu/environment/data5500.fa21/week3_algo_analysis_tradingexample/wmt.txt").readlines()]
print(prcs)

buy = 0
profit = 0.0
i = 0
days = 5

for p in prcs:
    prcs = [float(x) for x in open("/home/ubuntu/environment/data5500.fa21/week3_algo_analysis_tradingexample/wmt.txt").readlines()]

    if i >= days:
        avg = np.mean(prcs[i-days:i])
        
        if p < avg * .98 and buy == 0: # buy
            buy = p
            print("buying: ", p)
        elif p > avg * 1.02 and buy != 0: # sell
            profit += p - buy
            buy = 0
            print("selling at: ", p)
            
        else:
            pass
        
    i += 1
print("total profit: ", profit)
print("returns: ", profit/prcs[0])
