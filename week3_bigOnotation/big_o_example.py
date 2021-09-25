lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]


for l in lst:
    print(l, end=" ")

tot = 0
num_elem = 0
for l in lst:
    tot += l
    num_elem += 1
    
print("\nmean: ", tot / num_elem)

# O(n^4)
# for l in range(1000):
#     for j in range(1000):
#         for k in range(1000):
#             for m in range(1000):
#                 print(l * j * k * m, end=" ")
                 
# for i in range(1000):
#     for j in range(1000):
#         print(i * j)
        
# for m in range(1000):
#     for n in range(1000):
#         print(m * n)
        
        
        
lst = [[1,2,3], [3,4,5], [5,6,7], [8,9,0]]

total = 0
ct = 0
for row in lst:
    for item in row:
        total += item
        ct += 1
print("average: ", total / ct)