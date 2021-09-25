
def fact(n):
    res = 1.0
    while n>1:
        res *= n
        n -= 1
    
    return res
    
n = eval(input("enter a number, and I will calculate the factorial: "))
print(fact(n))
    
def fact_recursive(n):
    if n == 0:
        return 1
    return n * fact_recursive(n/2)
    
# 10 * (9 * (8 * (7 * (6 * (5 * (4 * (3 * (2 * (1 * (0)))))))))



print(fact_recursive(10))



def add_nums(n):
    if n == 0:
        return 0
    return n * add_nums(n-1)
    
# 10 + (9 + (8 + (7 + (6 + (5 + (4 + (3 + (2 + (1 + (0)))))))))



print(add_nums(10))