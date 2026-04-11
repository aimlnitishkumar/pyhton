# string or its formating

# Create a string "Python Programming" and:
    # Print its length.
    # Print the first and last character.
    # Slice "Python" from it.

"""str1 = "Python Programming"

print(len(str1))
print(str1[0], str1[-1])
print(str1[0:6])"""


# Take a string " Hello World " and:
    # Remove extra spaces.
    # Convert it to uppercase.
    # Replace "World" with "Python".

"""str1 = " Hello World "
print(str1.strip())
print(str1.upper())
print(str1.replace("World", "Python"))"""

# Count how many times the letter "a" appears in the string "banana".

"""s = "banana"
print(s.count("a"))"""

# Given "python is fun", capitalize the first letter of each word.

"""s = "python is fun"
print(s.title())"""

# Write a program to check if the string "data" exists in "big data analytics".

"""s = "big data analytics"

if "data" in s:
    print("Yes")"""

# Input a sentence from the user and:

# Convert it to lowercase.
# Count how many spaces are in it.
# Find the index of the word "Python" (if present).

"""sentence = input("Enter a sentence: ")

print("Lowercase : ", sentence.lower())
print("Spaces in the sentence: ",sentence.count(" "))


if "Python" in sentence:
    print("Index of Python :", sentence.find("Python"))
else:
    print("Python not found")"""


# Given "mississippi", create a dictionary that counts each character’s frequency.

"""s = "mississippi"
dict1 = {}

for char in s:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1

print(dict1)"""

# Convert "12345" into an integer and add 10. (Hint: type casting)

"""s = "12345"

num = int(s) + 10
print(num)"""

# Join a list of words ["I", "love", "Python"] into one string using " ".join().

"""words = ["I", "love", "Python"] 

result = " ".join(words)
print(result)"""

# Reverse a string using slicing.

"""str1 = "riya"
print(str1[::-1])"""


# Use an f-string to display:
# "My name is Alice and I am 20 years old." (take variables name and age).


"""name = input("Enter name here : ")
age = input("Enter age here : ")

print(f"My name is {name} and I am {age} years old.")"""

# Using format(), print:
# "The price of an Apple is 50 rupees."

"""item = "Apple"
price = 50

print("The price of an {} is {} rupees.".format(item,price))"""


# Take two numbers a = 5, b = 3 and print:
#"The sum of 5 and 3 is 8" using f-string.

"""a = 5 
b = 3 

print(f"The sum of {a} and {b} is {a+b}")"""


# Print the value of pi = 3.14159265 up to 2 decimal places using formatting.

"""pi = 3.14159265
print(f"{pi:.2f}")"""


# Create a mini-bill using formatting:
    # Item: Pen   Price: 10
    # Item: Book  Price: 50
    # Total = 60

"""Item1, pricePen = "Pen", 10
Item2, priceBook = "Book", 50

total = pricePen + priceBook

print(f"Item: {Item1}   Price: {pricePen}")
print(f"Item: {Item2}  Price: {priceBook}")
print(f"Total = {total}")"""

# Write a program that takes a sentence from the user and:
# Counts vowels (a, e, i, o, u).
# Counts consonants.
# Prints the results using string formatting.

"""sentence = input("Enter a sentence : ")

countVowels = 0
countCons = 0


for char in sentence.lower():
    if char.isalpha(): 
        if char in "aeiou":
            countVowels += 1
        else:
            countCons += 1

print(f"Vowels in sentence is {countVowels}.")
print(f"Consonants in sentence is {countCons}.")"""


# Write a function that takes a name and age, then returns a string:
#"Hello <name>, you will turn 100 years old in <year>". (Hint: use current year + age).

def future_100(name, age):
    current_year = 2026
    year = current_year + (100 - age)
    return f"Hello {name}, you will turn 100 years old in {year}"

print(future_100("Nitish", 21))