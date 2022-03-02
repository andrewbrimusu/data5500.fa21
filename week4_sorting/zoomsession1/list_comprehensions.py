import random

lst = []
for i in range(100):
    lst.append(random.randint(1,100))
    
print(lst)


lst2 = [random.randint(1,100) for x in range(100)]

print("lst2: \n", lst2)

lst3 = [2 ** x for x in range(11)]
print("lst3: \n", lst3)
