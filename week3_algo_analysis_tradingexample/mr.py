import numpy as np
import os
# os.system("pip3 install numpy")


prcs = [float(x) for x in open("week3/zm.txt").readlines()]
print(prcs)

buy = 0
profit = 0.0
i = 0
days = 5

for p in prcs:
    if i >= days:
        avg = np.mean(prcs[i-days:i])
        
        if p < avg * .95 and buy == 0: # buy
            buy = p
            print("buying: ", p)
        elif p > avg * 1.05 and buy != 0: # sell
            profit += p - buy
            buy = 0
            print("selling at: ", p)
            
        else:
            pass
        
    i += 1
print("total profit: ", profit)
print("returns: ", profit/prcs[0])
