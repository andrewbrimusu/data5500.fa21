def sum_numbers(n):
    # add up all the numbers 1 to n, and return the result
    val = 0
    for i in range(1,n+1):
        val += i
    return val

print(sum_numbers(5)) # 15


def sum_number_rec(n):
    if n == 1:
        return 1
    return n + sum_number_rec(n-1) # 5 + 4 + 3 + 2 + 1
    
print(sum_number_rec(5))


def factorial(n):
    tot = 1
    for i in range(1,n+1):
        tot *= i
    return tot
    
print(factorial(5)) #120

def factorial_rec(n):
    #base case
    if n == 1:
        return n
    #recursive all
    return n * factorial_rec(n-1)
    
print(factorial_rec(5)) #120

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # recursive call
    return fib(n-1) + fib(n-2)
    
print(fib(41))