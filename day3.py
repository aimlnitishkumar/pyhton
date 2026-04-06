# Function in Python programming Language

# Write a function greet() that prints "Hello, welcome to Python!".

"""def greet():
    print("Hello, Welcome to Python!")
greet()"""


# Write a function square(num) that returns the square of a number.

"""def square(num):
    return num * num

num = int(input("Enter a number: "))
result = square(num)
print(result)"""


# Write a function is_even(num) that checks if a number is even.
    #Return True if even, else False.

"""def is_even(num):
    return num % 2 == 0

num = int(input("Enter a number: "))
result = is_even(num)
print(result)"""


# Write a function add(a, b) that takes two numbers and returns their sum.

"""def add(a, b):
    return a+b
a = int(input("Enter a: "))
b = int(input("Enter b: "))

result = (add(a, b))
print(result)"""


# Write a function area_of_circle(r) that returns the area of a circle.
 # (Formula: πr², take π = 3.14)


"""def area_of_circle(r):
    return 3.14*r*r

r = int(input("Enter radius of circle: "))
area = area_of_circle(r)
print(area)"""


# Write a function greet_user(name, age) that prints:
    #Hello <name>, you are <age> years old.

"""def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_user(input("Enter your name: "), input("Enter your age: "))"""


# Write a function factorial(n) that returns the factorial of n.
 # (Example: 5! = 120)

"""def factorial(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n -= 1
    return fact

n = int(input("Enter any number: "))
print(factorial(n))"""


# Write a function reverse_string(s) that returns the reverse of a string.
    # (Example: "hello" → "olleh")

"""def reverse_string(s):
    return s[::-1]

s = "Hello"
print(reverse_string(s))"""


# Write a function is_palindrome(s) that checks if a string is a palindrome.
    #(Palindrome → same forward & backward, e.g., "madam")

"""def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

s = input("Enter a Palindrome String: ")
print(is_palindrome(s))"""


# Write a function max_of_three(a, b, c) that returns the largest of three numbers.

"""def max_of_three(a, b, c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c 
print(max_of_three(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))))"""
        

# checks whether a number is an Armstrong number.

"""def is_armstrong(n):
    # your code

    temp = n
    digits = len(str(n))
    sum = 0

    while n >= 1:
        d = n%10
        sum = sum + d ** digits
        n = n//10
    return sum == temp

n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong number")"""


# Write a function fibonacci(n) that returns the first n Fibonacci numbers.

"""def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
       result.append(a)
       a, b=b, a+b
    return result

print(fibonacci(int(input("Enter a number: "))))"""


# Write a function calculator(a, b, operator) that performs addition, subtraction, multiplication, or division based on the operator (+, -, *, /).

"""def calculator(a, b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b 
    elif operator == "*":
        return a*b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by 0"
        else:
            return a/b 
    else:
        return "Invalid Operator"

operator = input("Enter operator(+,-,*,/): ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(calculator(a, b, operator))"""


# Write a function count_vowels(s) that returns the number of vowels in a string.

"""def count_vowels(s):
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels: 
            count += 1
    
    return count

s = input("Enter anything: ")
result = count_vowels(s)
print(result)"""


# Write a function prime_numbers(n) that prints all prime numbers up to n.


"""def prime_numbers(n):
    

    for num in range(2, n+1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0 :
                is_prime = False
                break
        if is_prime:
            print(num)

n = int(input("Enter a number: "))
prime_numbers(n)
"""

# Write a function grade(marks) that takes a percentage and returns:
    #≥ 90 → "A"
    #≥ 70 → "B"
    #≥ 50 → "C"
    #Else → "Fail"


"""def grade(per):
    if per >=90:
        return "A"
    elif per >=70:
        return "B"
    elif per >=50:
        return "C"
    else:
        return "Fail"

phy = int(input("Enter obtained marks: "))
chem = int(input("Enter obtained marks: "))
math = int(input("Enter obtained marks: "))

per = (phy+chem+math)/3

print("Percentage:", per)
print("Grade:", grade(per))"""
