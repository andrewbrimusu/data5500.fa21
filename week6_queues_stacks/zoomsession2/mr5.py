import numpy as np

prices = [float(x) for x in open("data5500.fa21/week6_queues_stacks/zoomsession2/KO.txt").readlines()]

print(prices)

days= 5
buy = 0
profit = 0.0
for i in range(len(prices)):
    if i > days:
        p = prices[i]
        avg = np.mean(prices[i-days:i])
        
        if p < avg * 0.97 and buy == 0: #buy
            buy = p
        elif p > avg * 1.03 and buy != 0: #sell
            profit += p - buy
            buy = 0
        else:
            pass # do nothing today, except hopefully my position is becoming more profitable
        
print("profit: ", profit)
print("returns%: ", 100 * (profit/prices[0]))

