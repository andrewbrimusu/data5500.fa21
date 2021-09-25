import numpy as np

lst = [1,2,3,4,5,6]
for l in lst:
    print(l)
    
lst = [j for j in range(1,7) ]
print("lst: ", lst)

matrix = [ [n*m for n in range(10)] for m in range(10) ]
print("matrix: ", matrix)
for m in matrix:
    print(m)
    
avgs = [ np.mean(m) for m in matrix ] 
print("avgs: ", avgs)
avg_all = np.mean(avgs)
print("avg_all: ", avg_all)