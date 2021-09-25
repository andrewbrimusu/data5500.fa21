def sum_numbers(num):
    if num == 0:
        return 0
    return num + sum_numbers(num-1)
    
print(sum_numbers(100))

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)
    
print(factorial(4))

def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)
    
print(fib(3))

for i in range(100):
    print(fib(i))
