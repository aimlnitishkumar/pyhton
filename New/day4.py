
# list and tuple in python programming

# Create a list of 5 favorite fruits and print them.

"""fruits = ['banana', 'apple', 'orange', 'potato', 'mango']
print(fruits)"""


# Add "grapes" to the list using .append().

"""fruits.append('graps')
print(fruits)"""


# Insert "kiwi" at index 2 using .insert().

"""fruits.insert(2,'kiwi')
print(fruits)"""


# Remove "apple" from the list using .remove().

"""fruits.remove('apple')
print(fruits)"""

# Create a list of numbers [10, 5, 20, 15] and sort them in ascending order.


"""numbers = [10,5,20,15]
numbers.sort()
print(numbers)"""

# Create a list of 10 numbers and print only the first 3 numbers.

"""numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0:3])"""

# Reverse a list without using .reverse() (hint: slicing [::-1])

"""numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::-1])"""


# Count how many times "banana" appears in a list

"""fruits = ['banana', 'apple', 'banana', 'orange', 'banana', 'potato', 'mango']
print(fruits.count('banana'))"""

# Write a program that finds the largest and smallest number in a list.

"""numbers = [1,2,3,4,5,6,7,8,9,10]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    
    if num < smallest:
        smallest = num

print("Largest", largest)
print("Smallest", smallest)"""


# Merge two lists: [1, 2, 3] and [4, 5, 6].

"""l1 = [1,2,3]
l2 = [4,5,6]

print(l1+l2)"""

# OR 

"""l1.extend(l2)
print(l1)"""


# Create a tuple with 5 colors and print the second color.

"""colors = ('red', 'blue', 'green', 'yellow', 'pink')
print(colors)"""


# Find the index of "blue" in a tuple ("red", "green", "blue", "yellow").

"""print(colors.index('blue'))"""


# Create a single-element tuple containing the number 5. (Hint: (5,))

"""t = (3, )
print(t)"""


# Convert a tuple into a list, add an element, and convert it back to a tuple.

colors = ('red', 'blue', 'green', 'yellow', 'pink')

"""l1 = list(colors)     
l1.append('white')    
colors = tuple(l1)     
print(colors)"""


# Write a program that removes duplicates from a list.
    #Example: [1, 2, 2, 3, 4, 4, 5] → [1, 2, 3, 4, 5]

"""l1 = [1,2,2,3,4,4,5,]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)"""


# Write a program to find the sum of all numbers in a list.

"""l1 = list(range(1, 6))
print(sum(l1))"""
    

# OR 

"""l1 = []
for num in range(1, 6):
    l1.append(num)

total = 0
for i in l1:
    total = total + i

print(total)"""


# Given a tuple (10, 20, 30, 40, 50), swap the first and last elements.
    #👉 Result: (50, 20, 30, 40, 10)

"""t1 = (10, 20, 30, 40, 50)
t1 = list(t1)
temp = t1[0]
t1[0] = t1[-1]
t1[-1] = temp

t1 = tuple(t1)
print(t1)"""


# Write a program that takes a list of words and prints the longest word.

"""l1 = ['Hey', 'I', 'Love', 'You', 'Forever']

longest = l1[0]

for word in l1:
    if len(word) > len(longest):
        longest = word

print(f"Longest Word : {longest}")"""


# Create a list of numbers and print only the even numbers.

"""l1 = []
for num in range(1, 21):
    l1.append(num)

for i in l1:
    if i % 2 == 0:
        print(i)"""