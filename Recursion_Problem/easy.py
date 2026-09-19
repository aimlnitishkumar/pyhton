
# Easy Level Questions in Python

# 1. Print numbers from 1 to N

"""def func(x, n):
    
    if x>n:
        return

    print(x)
    func(x+1,n)

func(1, 5)"""


# 2. Print numbers from N to 1

"""def func(x , n):
    if x>n:
        return

    print(n)
    func(x, n-1)
    
func(1, 5)"""


# 3. Print "Hello" N times

"""def func(n):
    if n==0:
        return

    print("Hello")
    func(n-1)
func(5)"""



# 4. Find the sum of numbers from 1 to N

"""def func(n):
    if n==0:
        return 0
    
    return n + func(n-1)

print(func(5))"""


# 5. Find factorial of a number

"""def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)

print(fact(5))"""


# 6. Find the sum of digits

"""def SumOfDigit(x):
    if x == 0:
        return 0

    return (x % 10) + SumOfDigit(x//10)

print(SumOfDigit(12345))"""



# 7. Count the digits of a number

# How it works
# C_of_digit(12345, 0)
# C_of_digit(1234, 1)
# C_of_digit(123, 2)
# C_of_digit(12, 3)
# C_of_digit(1, 4)
# C_of_digit(0, 5)

"""def C_of_digit(x, count = 0):
    if x == 0:
        return count

    return C_of_digit(x//10, count+1)

print(C_of_digit(12345))"""

    


# 8. Calculate x raised to power n
       # 2, 5
"""def func(x, n, total = 1):
    if n == 0:
        return total

    total = total *x 
    return func(x, n-1, total) 
print(func(2, 5))"""


# 9. Find the nth Fibonacci number

"""def func(n, a=0, b= 1):
    if n==0:
        return a

    
    c  = a+b
    return func(n-1, b, c)

print(func(6))"""


# print 1 to n number using functional recursion 

"""def func(i, n):
    if i>n:
        return []

    return [i]+ func( i+1, n)

print(func(1, 55))"""


# Parameter-Free Functional Recursion (Going Backward)

def print_1_to_n(n):
    if n == 0:
        return []

    
    return print_1_to_n(n - 1) + [n]


print(print_1_to_n(5))
# Output: [1, 2, 3, 4, 5]