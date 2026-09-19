# Print numbers from 1 to 10 using a for loop.

"""for i in range(1, 11):
    print(i)"""


# Print numbers from 10 down to 1 using a while loop.

"""i = 10 

while i >= 1:
    print(i) 
    i -= 1"""


# Print the multiplication table of 5 using a for loop.

"""
for i in range(1, 11):
    print(5*i)"""


# Print each character of the string "PYTHON" using a for loop.

"""str1 = " PYTHON"
for  i  in str1:
    print(i)"""


# Print only even numbers from 1 to 20 using a for loop.

"""for i in range(1, 21):
    if i%2 == 0:
        print(i)"""
    

# Ask the user for a number and print its factorial using a while loop.
    # (Example: 5! = 120)

"""num = int(input("Enter a number : "))
i=num
fact = 1
while num >=1:
    fact = fact * num
    num -= 1
print(f"factorial of {i} is {fact}")"""
   

# Write a program to print the sum of numbers from 1 to 100 using a loop.

"""sum=0
for i in range(1,101):
    sum = sum+i
print(sum)"""


# Print the first 10 Fibonacci numbers using a loop.
    # (0, 1, 1, 2, 3, 5, 8, …)

"""a, b = 0, 1

for i in range(10):
    print(a, end= " ")
    a, b = b , a+b"""


# Use a for loop and continue to print numbers from 1–10 but skip 5.

"""for i in range(1,11):
    if i==5:
        continue
    print(i)"""


# Use a for loop and break to stop printing when the number reaches 7.

"""for i in range(1,10):
    if i==8:
        break
    print(i)"""


# Guessing Game 🎮
    #Set a secret number (e.g., 8).
    #Keep asking the user to guess until they get it right.
    #Use a while loop with break.

"""secret_num = 8

while True:
    guess_num = int(input("Enter secret_num: "))

    if guess_num > secret_num:
        print("Too High")
    elif guess_num < secret_num:
        print("Too Low")
    else:
        print(f"Correct, Secret Number is {guess_num}")"""

# OR 

"""secret_num = 8

while True:
    guess_num = int(input("Enter your guess: "))

    if guess_num == secret_num:
        print("Correct! 🎉")
        break
    else:
        print("Try again!")"""

# Reverse a string using a loop.
    #(Example: "hello" → "olleh")

"""str1 = "Hello"
reversed_str = " "
for  i in range(len(str1)-1,-1,-1):
    reversed_str += str1[i]
print(reversed_str)"""

# OR

"""print(str1[::-1])"""


# Ask the user for a number n. Print a pattern:
 
 #*
 #**
 #***
 #****

"""num = int(input("Enter a number: "))

for i in range(1,num+1):
    for j in range(i):
        print("*",end="")
    print()"""



# Print all prime numbers between 1 and 50.

"""for num in range(2,51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)"""

# prime check for user input

"""initial_num = int(input("Enter initial number : "))
final_num = int(input("Enter final number : "))

for num in range(initial_num, final_num+1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)"""


# twin primes

"""for num in range(2, 51):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        for j in range(2, int((num+2)**0.5) + 1):
            if (num+2) % j == 0:
                break
        else:
            print(num, num+2)"""

# OR 

"""def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(2, 51):
    if is_prime(num) and is_prime(num + 2):
        print(num, num + 2)"""



# Infinite Loop Safety 🚨
    # Create a while True: loop that keeps asking the user for input.
    # If the user types "exit", break the loop.


"""while True:
    user_input = input("Enter anything you want, but if you enter exit then you will be out of program :")

    if user_input.lower()=="exit":
        break"""

# OR 
"""sentence = ""
while True:
    user_input = input("Enter anything you want, but if you enter exit then you will be out of program :")
    

    if user_input.lower()=="exit":
        break

    elif user_input.lower() == "print":
        print(sentence.strip())

    else:
        sentence += user_input + " """"


    

