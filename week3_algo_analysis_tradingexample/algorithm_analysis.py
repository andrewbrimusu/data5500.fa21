import time


start = time.time()

for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            x = i ** j
    # print(x)
finish = time.time()
print(finish - start)