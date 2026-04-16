# File handling (read, write, append)

# Create a file called myfile.txt and write the text:

#  Hello World
#  Welcome to Python
#  1. Then read and print the file content.

"""f = open("myself.txt", "w")
f.write("Hello World\nWelcome to Python")
f.close()

f = open("myself.txt", "r")
print(f.read())
f.close()"""


# Write a program to store your name, age, and city in a file called info.txt.

"""f = open("info.txt", "w")
f.write("Name: Nitish\nAge: 21\nCity: Meerut")
f.close()

f = open("info.txt", "r")
print(f.read())
f.close()"""

# Read a file story.txt and print the number of characters in it.

"""with open("story.txt", "w") as f:
    f.write("Hi I'n Nitty, I'm a Writer and Storyteller.\nToday I wanna to share with you a story about women.")"""

"""with open("story.txt", "r") as f:
    print(f.readline())"""

# Write a program that appends "Python is awesome!" at the end of myfile.txt.

"""with open("myself.txt", "a") as f:
    f.write("\nPython is awesome!")

with open("myself.txt", "r") as f:
    print(f.read())"""


# Create a file numbers.txt and write numbers from 1 to 20 (each on a new line).

"""with open("numbers.txt", "w") as f:
    for num in range(1,21):
        f.write(f"{num}\n")

with open("numbers.txt", "r") as f:
    print(f.read())"""



# Read numbers.txt and calculate the sum of all numbers.

"""with open("numbers.txt", "r") as f:
    total = 0
    for num in f:
        total = total + int(num.strip())

print(total)"""

# Copy the contents of one file (data.txt) into another (backup.txt).

"""with open("data.txt", "r") as source:
    content = source.read()

with open("backup.txt", "w") as destination:
    destination.write(content)

with open("backup.txt", "r") as f:
    print(f.read())"""

# Count how many lines exist in story.txt.

"""with open("story.txt",  "r") as f:
    count = 0
    for line in f:
        count += 1

print("Number of lines: ", count)"""


# Read a file and print only those lines which contain the word "Python".

"""with open("myself.txt", "r") as f:
    for line in f:
        if "Python" in line:
            print(line)
"""


# Create a log file log.txt where every time the program runs, it appends the current date & time. (Hint: use datetime module).

"""from datetime import datetime

with open("log.txt", "a") as f:
    current_time = datetime.now()
    f.write("{current_time}\n")

with open("log.txt", "r") as f:
    print(current_time)"""


# Write a program to count how many vowels (a, e, i, o, u) are in story.txt.

"""with open("story.txt", "r") as f:
    content = f.read()
    
    count = 1
    for char in content.lower():
        if char in "aeiou":
            count +=1

print(count)"""
        

# Take a list of names (["Alice", "Bob", "Charlie"]) and write each name into a new line in names.txt.

"""l1 = ["Alice", "Bob", "Charlie"]
with open("names.txt", "w") as f:
    for name in l1:
        f.write(f"{name}\n")
with open("names.txt", "r") as f:
    print(f.read())"""


# Read a file and create a dictionary of word frequencies (how many times each word appears).


"""with open("myself.txt", "r") as f:
    content = f.read().lower()

words = content.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)"""


# Merge the contents of two files (file1.txt and file2.txt) into a new file merged.txt.

"""with open("names.txt", "r") as f1, open("story.txt", "r") as f2, open("mixed.txt","w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())

with open("mixed.txt", "r") as f4:
    print(f4.read())"""


# Write a program to create a student gradebook file.
# Ask user for student name and marks.
# Save it in grades.txt in format:
# Name: Alice, Marks: 85
# Name: Bob, Marks: 90


"""with open("grades.txt", "a") as f:
    while True:
        stu_name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        
        f.write(f"Name: {stu_name}, Marks: {marks}\n")
        
        choice = input("Add another student? (y/n): ")
        if choice.lower() != 'y':
            break

# Read and display file
with open("grades.txt", "r") as f1:
    print(f1.read())"""




