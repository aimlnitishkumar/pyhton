# dictionary and set in python

# Create a dictionary with details of a book: title, author, year. Print all values.

"""book = {
    "title" : "A Lot of Words",
    "author" : "Nittyshry Prabhu",
    "year" : 2025
}

print(book)
print(book.values())
print(type(book))"""

# Add a new key "price" with some value to the dictionary.
"""
book = {
    "title" : "A Lot of Words",
    "author" : "Nittyshry Prabhu",
    "year" : 2025
    
}

book["price"] = 559
print(book)

# Update the "year" of the book to a new year.

book["year"] = 2026
print(book)

# Remove the "author" key from the dictionary.

book.pop("author")
print(book)


# Write a program to print only the keys of a dictionary.

print(book.keys())
"""

# Create a dictionary of 3 students with their marks. Find the average marks.
# Example: {"A": 85, "B": 90, "C": 78}

"""students = {"A": 85, "B": 90, "C": 78}

total = 0
for marks in students.values():
    total += marks

avg = total / len(students)

print(f"Average marks : {avg}")"""


# Check if a key "Python" exists in a dictionary.

"""Languages = {"A": "C", "B": "Java", "C": "HTML", "D": "JavaScript","Python": "Language"}

if "Python" in Languages:
    print("Exists")
else:
    print("Not Exists")"""


# Merge two dictionaries into one.

"""book = {
    "title": "A Lot of Words",
    "author": "Nittyshry Prabhu",
    "year": 2025 
}

book_price = {
    "page": 259,
    "price": 359
}

print(book | book_price)

# OR 
book.update(book_price)
print(book)"""


# Count how many times each letter appears in the word "mississippi" (hint: dictionary).

"""word = "mississippi"
count = {}

for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)"""


# Write a program to get both keys and values using .items().

"""book = {
    "title": "A Lot of Words",
    "author": "Nittyshry Prabhu",
    "year": 2025, 
    "price": 359,
    "pages": 259
}

print(book.items())

# OR

for key, value in book.items():
    print(key, ":", value)"""


# Create a set of 5 numbers. Print its length.

"""numbers = {4, 5, 7, 9, 11}
print(numbers)
print(len(numbers))"""

# Add the number 100 to the set.

"""numbers = {3, 6, 7, 9, 11}
numbers.add(13)
print(numbers)"""

# Remove an element from the set using .remove().

"""numbers = {3, 6, 7, 9, 11}
numbers.remove(7)
print(numbers)"""


# Try adding duplicate elements to a set and observe the result.

"""numbers = {3, 6, 7, 9, 11}
numbers.add(7)
print(numbers)"""

# Convert a list [1, 2, 2, 3, 4, 4, 5] into a set to remove duplicates.

"""l1 = [1, 2, 2, 3, 4, 4, 5]

print(set(l1))"""

# Given two sets A = {1, 2, 3} and B = {3, 4, 5}, find:
    # Union
    # Intersection
    # Difference

"""A = {1, 2, 3}

B = {3, 4, 5}

print("Union", A | B)
print("Intersection", A & B)
print("Difference", A - B)"""

# Write a program to check if a set is a subset of another set.
    #Example: {1, 2} ⊆ {1, 2, 3, 4}

"""A = {1, 2, 3, 4}
B = {1, 2}


if B.issubset(A):
    print("Subset")
else:
    print("Not Subset")"""


# Create a set of vowels from the word "education".

"""word = "education"
vowels = set()

for char in word:
    if char in "aeiou":
        vowels.add(char)

print(vowels)"""
    

# Find the common elements between two lists using sets.
    #Example: [1, 2, 3] and [2, 3, 4] → {2, 3}

"""l1 = [1, 2, 3]
l2 =  [2, 3, 4]

print(set(l1) & set(l2))"""

# Write a program to check if two sets have no elements in common.

"""set1 = {2, 3, 4}
set2 = {5, 7, 9}

if set1.isdisjoint(set2):
    print("No common elements")
else:
    print("Common elements exist")"""