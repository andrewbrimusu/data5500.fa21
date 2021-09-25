
import random
import time
import numpy

start=time.time()
lst=[]
for i in range(1000000):
    lst.append(random.randint(1,1000))
# lst
end=time.time()
print("time (sec): ",end-start)


start2=time.time()
lst=numpy.random.rand(1000000)
end2=time.time()
print("time (sec): ",end2-start2)


# start2=time.time()
# lst=numpy.random.uniform(1, 1000, size=1000000)
# end2=time.time()
# print("time (sec): ",end2-start2)




lst = []
for i in range(10000):
    lst.append(random.randint(1,10000))
    
start2 = time.time()
for i in range(10000):
    for j in lst:
        if j == i:
            break
end2 = time.time()

print("time (sec): ",end2-start2)