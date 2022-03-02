print("hello")

f = open("/home/ubuntu/environment/data5500.fa21/week6_queues_stacks/GME.txt", "r")
# lines = f.readlines()
# print("lines: ", lines)

prices = []
line = f.readline()
print("line: ", line)

buy = 0
short = 0
tot_profit = 0
while line:
    prices.append(float(line))
    line = f.readline()

    if len(prices) == 6: # 5 day moving average + 1 current day price
        avg = ( prices[0] + prices[1] + prices[2] + prices[3] + prices[4] ) / 5
        # print("avg: ", avg)
        if prices[5] > avg and buy == 0:
            print("buying at: ", prices[5])
            tot_profit += short - prices[5]
            buy = prices[5]
        elif prices[5] < avg and buy != 0:
            print("selling at: ", prices[5])
            tot_profit += prices[5] - buy
            print("trade profit: ", prices[5] - buy)
            buy = 0
            short = prices[5]
        else:
            pass #do nothing
        prices.pop()
        
print("tot_profit: ", tot_profit)
print("percenage return: ", tot_profit/prices[0])