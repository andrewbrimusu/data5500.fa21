nums = [3, 1, 4, 1, 5, 9, 2, 6]

for i in range(len(nums)):
    print(nums[i])
    
def print_nums(nums, i):
    if i >= len(nums):
        return
    
    print(nums[i])
    print_nums(nums, i+1)
    
print_nums(nums, 0)




tot = 0
n = eval(input("enter a number n, and i will sum everything 1 to n: "))
for i in range(1,n+1):
    tot += i
print(tot)





def sum_recur(n):
    if n == 0:
        return 0
    return n + sum_recur(n-1)
    
    # 100 + 99 + 98 + .. + 1 + 0
    
print(sum_recur(100)) #5050



def factorial_recur(n):
    if n == 1:
        return 1
    return n * factorial_recur(n-1)
    
    # 100 + 99 + 98 + .. + 1 + 0
    
print(factorial_recur(10)) #3.6M

ctr = 0
def fibonacci(n):
    global ctr
    ctr += 1
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
    

print(fibonacci(50
), ctr)

