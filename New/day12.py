

# Modules, Packages, pip basics ......


"""import math, datetime, random, time


print(datetime.date.today())
print(math.sqrt(16))
print(random.randint(1,11))

from datetime import datetime
current_time = datetime.now()
print(current_time.strftime("%H:%M:%S"))"""


# Create a module calculator.py that contains functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
# Import it into another file and test each function.



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

