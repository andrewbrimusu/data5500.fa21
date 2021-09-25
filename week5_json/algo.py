import numpy
lst = [3,1,4,1,5,9,3,6,5,8,9,7,9,3,2,3,8,4,6]

lst = numpy.random.randint(50, size=10000000)

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] + lst[j] == 13:
            print("found the pair!, its ", lst[i], "and", lst[j])
            
# O(n^2)

