


# Part A: Class & Object Basics

# Create a class Person with attributes name and age.
# Create two objects with different values and print their details.



'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}, age : {self.age}")
    
p1 = Person("Nitish", 21)
p2 = Person("Shry", 20)

p1.display()
p2.display()'''


# 2. Define a class Car with attributes brand and model.
# Add a method display() to print car details.
# Create 2 car objects and call the method.


'''class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand Name: {self.brand} and Model Name: {self.model}")

c1 = Car("Audi", "A09")
c2 = Car("Techme", "Te08")

c1.display()
c2.display()
'''

# Create a class Book with attributes title and author.
# Create an object and print "Book: [title] by [author]"

'''class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def print(self):
        print(f"Book: {self.title} by author {self.author}")

b1 = Book("A Lots Words", "Nittyshry Prabhu")

b1.print()'''

      
# 9. Create a class Laptop with attributes brand, ram, price.
# Add method show_specs().
# Create multiple laptop objects and print their specs


'''class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def show_specs(self):
        print(f"Brand: {self.brand}, Ram: {self.ram}, Price: {self.price}")

l1 = Laptop("HP", "8GB", 45000)
l2 = Laptop("Lenovo", "12GB", 55000)
l3 = Laptop("Vevo Gaming", "12GB", 65000)

l1.show_specs()
l2.show_specs()
l3.show_specs()'''


#10. Create a class Circle with constructor to initialize radius.
# Add methods area() and circumference().
# Test with different radius values.


'''class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Area:", 3.14*self.radius*self.radius)
    def circumference(self):
        print(f"Circumference:", 2*3.14*self.radius)
radius = Circle(4)


radius.area()
radius.circumference()
'''


# 11. Create a class Movie with attributes title, rating, year.
# Add method is_hit() which prints "Hit Movie!" if rating > 7, else "Flop Movie!".
# Test with 3 movies.

'''class Movie():
    def __init__(self, title, rating, year):
        self.title = title
        self.rating = rating
        self.year = year
    def is_hit(self):
        if self.rating > 7:
            print(f"Hit_Movie_Name: {self.title}, Rating: {self.rating}/10, Year: {self.year}")
        else:
            print("Flop Movie!")

m1 = Movie("Don", 6, 2010)
m2 = Movie("You and Me", 9, 2020)
m3 = Movie("Open Book", 8, 2040)

m1.is_hit()
m2.is_hit()
m3.is_hit()'''

# Output
# Flop Movie!
# Hit_Movie_Name: You and Me, Rating: 9/10, Year: 2020
# Hit_Movie_Name: Open Book, Rating: 8/10, Year: 2040



# 12. Create a class ShoppingCart:
# Constructor initializes an empty list items.
# Method add_item(item) adds to list.
# Method show_cart() displays all items.
# Test by adding multiple items.


'''class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        print(self.items)


cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("iPhone")
cart.add_item("Camera")

cart.show_cart()'''



# 7.  Create a class Dog with:
# A class variable species = "Mammal".
# An instance variable name.
# Create two dog objects and print their names and species.


'''class Dog():
    species = "Mammal"

    def __init__(self, name):
        self.name = name
    
dog1 = Dog("German")
dog2 = Dog("Indian")

print(f"Dog_Name: {dog1.name} , {dog1.species}")
print(f"Dog_Name: {dog2.name}, {dog2.species}")'''


# 8.  Create a class BankAccount with a class variable bank_name = "HDFC Bank".
# Constructor should take account_holder and balance.
# Add method deposit(amount) and withdraw(amount).
# Print balance after each operation.


'''class BankAccount:
    bank_name = "HDFC Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Bank: {account.bank_name}, Name: {self.account_holder}, Total amount is {self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Bank: {account.bank_name}, Name: {self.account_holder}, Total amount is {self.balance}")

account = BankAccount("Nitish", 1000)

account.deposit(500)
account.withdraw(200)
'''



# Create a class Rectangle with attributes length and width.
# Add a method area() to return area of rectangle.
# Add a method perimeter() to return perimeter.
# Test with multiple rectangles


'''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * ( self.length  + self.width)
 

rectangle1 = Rectangle(20, 10)
rectangle2 = Rectangle(30, 15)


print("Rectangle 1")
print(f"Area = {rectangle1.area()}")
print(f"Perimeter = {rectangle1.perimeter()}")

print("Rectangle 2")
print(f"Area = {rectangle2.area()}")
print(f"Perimeter = {rectangle2.perimeter()}")'''



# Define a class Employee with a constructor taking name, salary, and department.
# Add a method get_bonus() that calculates 10% of salary.
# Create an object and print the bonus.


'''class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_bonus(self):
        bonus =  (self.salary * 10)/100
        return bonus

emp = Employee("Nitish", 50000, "HR")
print(f"Emp_Name: {emp.name}, Salary = {emp.salary}, Department: {emp.department}, Bonus = {emp.get_bonus()}")'''




# Student Result 🎓

# Create a Student class.

# Constructor takes name and marks for 3 subjects.
# total_marks() returns the total.
# percentage() returns the percentage.
# get_grade() returns:
# 90+ → A
# 75–89 → B
# 60–74 → C
# 40–59 → D
# Below 40 → F
# display_result() prints all details.

'''class Student:
    def __init__(self, name, phy_mark, chem_mark, math_mark):
        self.name = name
        self.phy_mark = phy_mark
        self.chem_mark = chem_mark
        self.math_mark = math_mark
    def total_marks(self):
        return self.phy_mark + self.chem_mark + self.math_mark
        
    def percentage(self):
        return (self.phy_mark + self.chem_mark + self.math_mark) / 3
        # return self.total_mark() / 3
    def get_grade(self):
        per = (self.phy_mark + self.chem_mark + self.math_mark) / 3
        # return self.percentage()

        if per >= 90:
            return "A"
        elif per >= 75:
            return "B"
        elif per >= 60:
            return "C"
        elif per >= 40:
            return "D"
        else:
            return "F"

    def display_result(self):
        print(f"Name: {self.name}, Total_Marks = {self.total_marks()}, Percentage = {self.percentage():.2f} %, Grade: {self.get_grade()}" )

student = Student("Nitish", 75, 66, 83)
student.display_result()'''





# 🟡 Level 2 — More Logic

# 3. Shopping Cart 🛒
# Create a ShoppingCart class.
# Each item should have:
# name
# price
# quantity

# Methods:
# add_item(name, price, quantity)
# remove_item(name)
# calculate_total()
# show_cart()

# Example:
# Laptop ₹50000 × 1
# Mouse ₹1000 × 2
# pinboard ₹2000 × 1

# Expected total:
# ₹54000
# Challenge: Give a 10% discount if the total is greater than ₹50,000.

'''class ShoppingCart:
    def __init__(self):
        
        self.items = []
    def add_item(self, name, price, quantity):
        self.items.append({
            "name" : name,
            "price": price,
            "quantity" : quantity
        })
    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                break
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        if total > 50000:
            discount = (total * 10)/100
            bill = total - discount
        return bill       
           
    def show_cart(self):
        print(f"Items: {self.items}")
        print(f"Total_bill: {self.calculate_total()}")  

item = ShoppingCart()

item.add_item("Mobile", 50000, 2)
item.add_item("Earphone", 1000, 3)
item.add_item("Mouse", 500, 2)

item.remove_item("Mouse")

item.show_cart()
'''


# 4. Employee Salary 💼

# Create an Employee class.
# Constructor:
# name
# basic_salary
# department

# Methods:
# calculate_bonus() → 10% of salary
# calculate_tax() → 5% of salary
# calculate_final_salary() → salary + bonus − tax
# display_details()

# For example:
# Basic Salary: ₹50,000
# Bonus: ₹5,000
# Tax: ₹2,500
# Final Salary: ₹52,500

'''class Employee:
    def __init__(self, name, basic_salary, department):
        self.name = name
        self.basic_salary = basic_salary
        self.department = department
    def calculate_bonus(self):
        bonus = (self.basic_salary * 10) / 100
        return bonus
    def calculate_tax(self):
        tax = (self.basic_salary * 5) / 100
        return tax 
    def calculate_final_salary(self):
        final_salary = self.basic_salary + self.calculate_bonus() - self.calculate_tax()
        return final_salary
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Bonus: {self.calculate_bonus()}")
        print(f"Tax : {self.calculate_tax()}")
        print(f"Final Salary: {self.calculate_final_salary()}")

emp1 = Employee("Nitish", 55000, "HR")
emp2 = Employee("Rahul", 50000, "Receptionist")

emp1.display_details()
emp2.display_details()
'''

    
    



# 🟠 Level 3 — Good OOP Practice

# 5. Movie Ticket 🎬
# Create a MovieTicket class.

# Constructor takes:
# movie_name
# ticket_price
# number_of_tickets

# Methods:
# calculate_total()
# apply_discount()
# show_ticket()

# Rules:
# 1–2 tickets → no discount
# 3–5 tickets → 10% discount
# More than 5 → 20% discount

# Example:
# Movie: Avengers
# Price: ₹250
# Tickets: 5

# Total: ₹1250
# Discount: ₹125
# Final Price: ₹1125


'''class MovieTicket:
    def __init__(self, movie_name, ticket_price, number_of_tickets):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.number_of_tickets = number_of_tickets
    def calculate_total(self):
        total = self.ticket_price * self.number_of_tickets
        return total
    def apply_discount(self):
        if 5 >= self.number_of_tickets >=3:
            return (self.calculate_total() * 10)/100
        elif self.number_of_tickets > 5:
            return (self.calculate_total() * 20) / 100
        else:
            return 0
        

    def show_ticket(self):
        print(f"Movie Name: {self.movie_name}")
        print(f"Ticket Price: {self.calculate_total()}")
        print(f"Discount: {self.apply_discount()}")
        print(f"Final Price: {self.calculate_total() - self.apply_discount()}")

mov1 = MovieTicket("The Way You Think", 299, 2)
mov1.show_ticket()'''



# 6. Electricity Bill ⚡

# Create an ElectricityBill class.
# Constructor:
# customer_name
# units

# Calculate the bill according to:
# 0–100 units      → ₹5/unit
# 101–200 units    → ₹7/unit
# 201–300 units    → ₹10/unit
# Above 300       → ₹12/unit

# Methods:
# calculate_bill()
# display_bill()

# Challenge: Add a fixed ₹100 service charge.

'''class ElectricityBill:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units
    def calculate_bill(self):
        service_charge = 100
        if self.units <=100:
            return (self.units * 5) + service_charge
        elif self.units <=200:
            return (self.units * 7) + service_charge
        elif self.units <= 300:
            return (self.units * 10) + service_charge
        else:
            return (self.units * 12) + service_charge
    def display_bill(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Use Units: {self.units}")
        print(f"Total Electricity Bill : {self.calculate_bill()} include with service charge.")

consumer1 = ElectricityBill("Nitish", 501)
consumer1.display_bill()
'''



# 🔴 Level 4 — Challenge

# 7. ATM Machine 🏧
# Create an ATM class.

# Constructor:
# account_holder
# balance
# pin

# Methods:

# check_balance()
# deposit(amount)
# withdraw(amount, pin)
# change_pin(old_pin, new_pin)

# Rules:

# Withdrawal requires the correct PIN.
# Cannot withdraw more than balance.
# Deposit must be greater than ₹0.
# Wrong PIN should display "Incorrect PIN".

# Challenge: Allow only 3 wrong PIN attempts.


'''class ATM:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self.balance = balance
        self.pin = pin
        self.wrong_attempts = 0

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than 0."

        self.balance += amount
        return self.balance

    def withdraw(self, amount, pin):
        if self.pin != pin:
            self.wrong_attempts += 1

            if self.wrong_attempts == 3:
                return "Only 3 wrong PIN attempts allowed. Please try again later."

            return "Incorrect PIN"

        if self.balance < amount:
            return "Insufficient balance in your account."

        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            return "PIN updated successfully"

        return "Incorrect PIN"


customer = ATM("Nitish", 5000, 1234)

print(customer.deposit(500))

print(customer.withdraw(200, 1234))

print(customer.check_balance())

print(customer.change_pin(1234, 5342))

print(customer.withdraw(200, 5342))'''
    
    


# 🔥 8. E-Commerce Product

# Create a Product class.

# Constructor:
# product_name
# price
# stock

# Methods:
# buy(quantity)
# restock(quantity)
# show_product()

# Rules:

# User cannot buy more than available stock.
# Buying decreases stock.
# Restocking increases stock.
# Quantity must be positive.

# Example:

# Product: iPhone
# Price: ₹70,000
# Stock: 5

# Buy 2
# Remaining Stock: 3
# Challenge: Add a 5% discount when buying 3 or more units.

'''class Product:
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock
        
    def buy(self, quantity):
        if quantity <=0:
            return "Quantity must be greater than 0."
        if self.stock < quantity:
            return "Unavailable"
        total = self.price * quantity
        final_price = total
        if quantity >= 3:
            discount = (total * 5)/100
            final_price = total - discount
        self.stock = self.stock - quantity 
        return final_price

    def restock(self, quantity):
        self.stock = self.stock + quantity
        return self.stock
    def show_product(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Remaining stock: {self.stock}")
        
        

p1 = Product("iPhone", 70000, 5)
print(f"Purches Product amount", p1.buy(4))
print("Restock product", p1.restock(5))
p1.show_product()
'''





# The new focus will be:

# Multiple objects interacting
# Lists of objects
# Methods calling other methods
# More complex conditions
# State management
# Searching/filtering objects
# Real-world business logic


# 🚀 Level 2 OOP Problems


# 1. 🏦 Bank Management System — Start Here

# Create a Bank class and an Account class.

# Account

# Constructor:

# account_number
# account_holder
# balance

# Methods:

# deposit(amount)
# withdraw(amount)
# check_balance()

# Rules:

# Deposit must be greater than 0.
# Withdrawal cannot exceed balance.
# Each account has its own balance.

# Bank

# Constructor:

# bank_name
# accounts

# Methods:

# add_account(account)
# remove_account(account_number)
# find_account(account_number)
# show_all_accounts()
# Example
# account1 = Account("101", "Nitish", 50000)
# account2 = Account("102", "Rahul", 30000)

# bank = Bank("HDFC")

# bank.add_account(account1)
# bank.add_account(account2)

# bank.find_account("101")

# The interesting part is:

# Bank
#  │
#  ├── Account 101 → Nitish → ₹50,000
#  │
#  └── Account 102 → Rahul  → ₹30,000

# This teaches you objects inside another object's list.


'''class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be greater than 0."
        else:
            self.balance = self.balance + amount
            return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal cannot exceed balance."
        else:
            self.balance = self.balance - amount
            return self.balance
    def check_balance(self):
        print(f"Holder Name: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

    

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return "Account Removed"
        return "Account not found"
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return "Account not found"

    def show_all_accounts(self):
        for account in self.accounts:
            print(
                f"Account: {account.account_number},"
                f"Name: {account.account_holder},"
                f"Balance: {account.balance}"
            )



account1 = Account(101, "Nitish", 50000)
account2 = Account(102, "Rahul", 45000)

bank =Bank("HDFC")

account1.deposit(10000)
account1.withdraw(5000)

account2.deposit(10000)
account2.withdraw(5000)

account1.check_balance()
account2.check_balance()

bank.show_all_accounts()

bank.add_account(account1)
bank.add_account(account2)



bank.show_all_accounts()

print(bank.find_account(103))'''


# 2. 🛒 Advanced Shopping Cart

# Create:

# Product
# ShoppingCart
# Customer

# Product
# name
# price
# stock

# ShoppingCart

# Methods:

# add_product(product, quantity)
# remove_product(product)
# calculate_total()
# checkout()

# Rules:

# Can't add more than available stock.
# Adding to cart reduces available stock.
# Removing from cart returns stock.
# Checkout calculates the final bill.
# 10% discount if total > ₹50,000.

# This is your previous ShoppingCart problem, but now using multiple classes.


'''class Product:
    def __init__(self, name, price, stock):
        self.name = name 
        self.price =price
        self.stock = stock
    

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if quantity <= 0:
            return "Quantity must be greater than 0."
        elif product.stock < quantity:
            return "Not enough stock available."
        else:
            self.items.append({
                "product" : product,
                "quantity": quantity
            })
        product.stock -= quantity
        
    def remove_product(self, product):
        for item in self.items:
            if item["product"] == product:
                product.stock += item["quantity"]
                self.items.remove(item)
                return "Product removed."
        return "Product not found."
    def calculate_total(self):
        total = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total += product.price * quantity
        return total
    def checkout(self):
        total = self.calculate_total()

        if total > 50000:
            discount = (total * 10)/100
            total = total - discount
        return total 

         

iphone = Product("iPhone", 70000, 10)
laptop = Product("Laptop", 60000, 15)

cart = ShoppingCart()

cart.add_product(iphone, 1)
cart.add_product(laptop, 1)

print(cart.calculate_total())

print(cart.checkout())
'''




# 3. 🎓 School Management System

# Create:

# Student
# Teacher
# School


# Student
# name
# roll_number
# marks

# Methods:

# add_marks(subject, marks)
# calculate_percentage()
# get_grade()


# Teacher
# name
# subject


# School

# Methods:

# add_student(student)
# add_teacher(teacher)
# find_student(roll_number)
# show_students()

# Challenge:

# Find the student with the highest percentage.


'''class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, marks):
        valid_subjects = ["phy", "chem", "math"]

        if subject not in valid_subjects:
            return "Invalid subject."

        if marks < 0 or marks > 100:
            return "Marks must be between 0 and 100."

        self.marks[subject] = marks
        return f"{subject} marks added successfully."

    def calculate_percentage(self):
        if not self.marks:
            return 0

        total_marks = sum(self.marks.values())
        total_subjects = len(self.marks)

        percentage = (total_marks / (total_subjects * 100)) * 100

        return percentage

    def get_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added successfully.")

    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student

        return None

    def show_students(self):
        if not self.students:
            print("No students registered.")
            return

        print(f"\n--- Student List: {self.school_name} ---")

        for student in self.students:
            print(
                f"Name: {student.name} | "
                f"Roll No: {student.roll_number} | "
                f"Percentage: {student.calculate_percentage():.2f}% | "
                f"Grade: {student.get_grade()}"
            )

    def show_teachers(self):
        if not self.teachers:
            print("No teachers registered.")
            return

        print(f"\n--- Teacher List: {self.school_name} ---")

        for teacher in self.teachers:
            print(
                f"Name: {teacher.name} | "
                f"Subject: {teacher.subject}"
            )


# -----------------------------
# Creating Students
# -----------------------------

student1 = Student("Nitish", 101)
student1.add_marks("phy", 85)
student1.add_marks("chem", 90)
student1.add_marks("math", 80)

student2 = Student("Rahul", 102)
student2.add_marks("phy", 70)
student2.add_marks("chem", 75)
student2.add_marks("math", 65)


# -----------------------------
# Creating Teachers
# -----------------------------

teacher1 = Teacher("Amit", "math")
teacher2 = Teacher("Rohit", "physics")


# -----------------------------
# Creating School
# -----------------------------

school = School("ABC School")


# -----------------------------
# Adding Students & Teachers
# -----------------------------

school.add_student(student1)
school.add_student(student2)

school.add_teacher(teacher1)
school.add_teacher(teacher2)


# -----------------------------
# Display Students
# -----------------------------

school.show_students()


# -----------------------------
# Display Teachers
# -----------------------------

school.show_teachers()


# -----------------------------
# Find Student
# -----------------------------

student = school.find_student(101)

if student:
    print("\n--- Student Found ---")
    print(f"Name: {student.name}")
    print(f"Roll Number: {student.roll_number}")
    print(f"Percentage: {student.calculate_percentage():.2f}%")
    print(f"Grade: {student.get_grade()}")
else:
    print("Student not found.")
'''

'''School
│
├── students
│     │
│     ├── Student 101 → Nitish
│     └── Student 102 → Rahul
│
└── teachers
      │
      ├── Teacher → Amit
      └── Teacher → Rohit'''


# 4. 🚗 Car Rental System

# Create:

# Car
# Customer
# RentalSystem
# Car
# car_id
# model
# price_per_day
# available

# Methods:

# rent()
# return_car()
# RentalSystem

# Methods:

# add_car(car)
# rent_car(car_id, days)
# return_car(car_id)
# show_available_cars()

# Rules:

# Rent car
#    ↓
# Check availability
#    ↓
# Calculate price × days
#    ↓
# Mark car unavailable

# Challenge:

# Give 15% discount if rented for more than 7 days.


'''class Car:
    def __init__(self, car_id, model, price_per_day, available=True):
        self.car_id = car_id
        self.model = model
        self.price_per_day = price_per_day
        self.available = available
    def rent(self):
        if not self.available:
            return "Car is already rented."

        self.available = False
        return "Car rented successfully."

    def return_car(self):
        if self.available:
            return "Car is already available."

        self.available = True
        return "Car returned successfully."

class RentalSystem:
    def __init__(self):
        self.cars = {}

    def add_car(self, car):
        self.cars[car.car_id] = car
        print(f"{car.model} added successfully.")
    def rent_car(self, car_id, days):
        if car_id not in self.cars:
            return "Car not found."
        if days <= 0:
            return "Number of days must be greater than 0."
        car = self.cars[car_id]

        if not car.available:
            return "Car is already rented."

        total = car.price_per_day * days

        if days > 7:
            discount = total * 15 / 100
            final_price = total -  discount
        else:
            discount = 0
            final_price = total

        car.rent()

        return (
            f"Car:{car.model}\n"
            f"Days:{days}\n"
            f"Total:{total}\n"
            f"Discount:{discount}\n"
            f"Final Price:{final_price}"
        )
    def return_car(self,car_id):
        if car_id  not in self.cars:
            return "Car not found."
        car = self.cars[car_id]
        return car.return_car()
    
    def show_available_cars(self):
        print("\n---Available Cars ---")

        found = False

        for car in self.cars.values():
            if car.available:
                print(
                    f"ID: {car.car_id} | "
                    f"Model: {car.model} | "
                    f"Price/Day: {car.price_per_day}"
                )
                found = True
        if not found:
            print("No card available.")


car1 = Car(101, "BMW", 5000)
car2 = Car(102, "Audi", 4000)
car3 = Car(103, "Mercedes", 6000)

rental = RentalSystem()


rental.add_car(car1)
rental.add_car(car2)
rental.add_car(car3)

rental.show_available_cars()

print("\n---Renting car----")
print(rental.rent_car(101, 10))

rental.show_available_cars()

print("\n -- Returning Car---")
print(rental.return_car(101))

rental.show_available_cars()
'''





# 5. 🏥 Hospital Management System

# Create:

# Patient
# Doctor
# Hospital

# Patient:

# name
# age
# disease

# Doctor:

# name
# specialization

# Hospital:

# patients
# doctors

# Methods:

# add_patient()
# add_doctor()
# find_patient()
# find_doctor()
# show_patients()
# show_doctors()

# Challenge:

# Assign a patient to a doctor based on specialization.


'''class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
        self.doctor = None


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization


class Hospital:
    hospital_name = "Shry Hospital"

    disease_specialization = {
        "heart problem": "cardiologist",
        "brain problem": "neurologist"
    }

    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added successfully.")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added successfully.")

    def find_patient(self, name):
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                return patient

        return None

    def find_doctor(self, name):
        for doctor in self.doctors:
            if doctor.name.lower() == name.lower():
                return doctor

        return None

    def show_patients(self):
        if not self.patients:
            print("No patients found.")
            return

        print(f"\n--- Patients in {self.hospital_name} ---")

        for patient in self.patients:
            doctor_name = (
                patient.doctor.name
                if patient.doctor
                else "Not Assigned"
            )

            print(
                f"Patient Name: {patient.name}, "
                f"Age: {patient.age}, "
                f"Disease: {patient.disease}, "
                f"Doctor: {doctor_name}"
            )

    def show_doctors(self):
        if not self.doctors:
            print("No doctors found.")
            return

        print(f"\n--- Doctors in {self.hospital_name} ---")

        for doctor in self.doctors:
            print(
                f"Doctor Name: {doctor.name}, "
                f"Specialization: {doctor.specialization}"
            )

    def assign_doctor(self, patient_name):
        patient = self.find_patient(patient_name)

        if patient is None:
            return "Patient is not found."

        required_specialization = self.disease_specialization.get(
            patient.disease.lower()
        )

        if required_specialization is None:
            return "No specialization mapping found for this disease."

        for doctor in self.doctors:
            if doctor.specialization.lower() == required_specialization:
                patient.doctor = doctor

                return (
                    f"{patient.name} assigned to "
                    f"{doctor.name} ({doctor.specialization})"
                )

        return "No suitable doctor found."


# -------------------------
# Create Patients
# -------------------------

patient1 = Patient("Raman", 21, "Heart Problem")
patient2 = Patient("Rohan", 23, "Brain Problem")


# -------------------------
# Create Doctors
# -------------------------

doctor1 = Doctor("Dr. Sharma", "Cardiologist")
doctor2 = Doctor("Dr. Khan", "Neurologist")


# -------------------------
# Create Hospital
# -------------------------

hospital = Hospital()


# -------------------------
# Add Patients
# -------------------------

hospital.add_patient(patient1)
hospital.add_patient(patient2)


# -------------------------
# Add Doctors
# -------------------------

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)


# -------------------------
# Assign Doctors
# -------------------------

print("\n--- Doctor Assignment ---")

print(hospital.assign_doctor("Raman"))
print(hospital.assign_doctor("Rohan"))


# -------------------------
# Show Patients
# -------------------------

hospital.show_patients()


# -------------------------
# Show Doctors
# -------------------------

hospital.show_doctors()
'''


# 6. 🍔 Food Ordering System

# Create:

# FoodItem
# Order
# Customer

# Food item:

# name
# price
# category

# Order:

# order_id
# items

# Methods:

# add_item()
# remove_item()
# calculate_total()
# apply_discount()

# Rules:

# Total > ₹1000 → 10% discount
# Total > ₹2000 → 20% discount

# Challenge:

# Add a ₹50 delivery charge unless the order exceeds ₹1500.

'''
class FoodItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, fooditem):
        self.items.append(fooditem)
        return f"{fooditem.name} successfully added."

    def remove_item(self, fooditem):
        for item in self.items:
            if item == fooditem:
                self.items.remove(fooditem)
                return f"{fooditem.name} successfully removed."
            
        return "Item not found."
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def apply_discount(self):
        total = self.calculate_total()

        if total > 2000:
            discount = total * 20 / 100
        elif total > 1000:
            discount = total * 10 / 100
        else:
            discount = 0

        total = total - discount

        return total

    def final_bill(self):
        total = self.calculate_total()
        discounted_total = self.apply_discount()

        if total >1500:
            delivery_charge = 0
        else:
            delivery_charge = 50
        final_price = discounted_total + delivery_charge

        return final_price

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        return f"Order {order.order_id} added successfully."

pizza = FoodItem("Pizza", 800, "Fast Food")
burger = FoodItem("Burger", 400, "Fast Food")
coke = FoodItem("Coke", 150, "Beverage")
pasta = FoodItem("Pasta", 700, "Italian")

order1 = Order(101)

print(order1.add_item(pizza))
print(order1.add_item(burger))
print(order1.add_item(pasta))
print(order1.add_item(coke))

print("\nTotal:", order1.calculate_total())

print("After Discount:", order1.apply_discount())

print("Final Bill:", order1.final_bill())

customer1 = Customer("Nitish")

print(customer1.add_order(order1))

'''

# 🔥 Level 3 — Challenge Problems

# Once you've completed those, we'll move to things like:

# 7. 🏧 ATM + Multiple Accounts

# One ATM manages multiple bank accounts.

# ATM
#  ├── Account
#  ├── Account
#  ├── Account
#  └── Account

# Users log in with:

# account_number + PIN

# Then:

# Check balance
# Deposit
# Withdraw
# Change PIN
# Logout



'''class Account:
    def __init__(self, account_number, account_holder, balance, pin):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.pin = pin
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Deposited amount is {amount}."
    def withdraw(self, amount):

        self.balance = self.balance - amount
        return f"Withdrawal amount is {amount}"
    def check_balance(self):
        current_balance = self.balance
        return current_balance
    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            return "Entered pin is wrong, please try again."
        elif old_pin == self.pin:
            self.pin = new_pin
            return "Pin changed successfully."
class ATM:
    def __init__(self):
        self.accounts ={}
        self.current_account = None
    def add_account(self, account):
        self.accounts[account.account_number] = account
    def login(self, account_number, pin):
        if account_number not in self.accounts:
            return "Account not found"
        account = self.accounts[account_number]

        if account.pin != pin:
            return "Incorrect pin"

        self.current_account = account

        return f"Welcome {account.account_holder}!"
    
account1 = Account(101, "Nitish", 50000, 1234)
account2 = Account(102, "Rahul", 30000, 5678)

atm = ATM()

atm.add_account(account1)
atm.add_account(account2)

print(atm.login(101, 1234))

print(account1.deposit(5000), account1.withdraw(2000))
print(account1.check_balance())

'''


# 8. 🏨 Hotel Booking System

# Classes:

# Room
# Customer
# Booking
# Hotel

# You'll need to handle:

# Available rooms
# Booking
# Cancellation
# Check-in
# Check-out
# Total cost
# Different room types

class Room:
    def __init__(self, room_number, room_type, price_per_night, availability=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.availability = availability
    def show_room(self):
        print(
            f"Room number : {self.room_number},"
            f"Room type : {self.room_type},"
            f"Price per nights : {self.price_per_night}"
        )
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.bookings = []
class Booking:
    def __init__(self, booking_id, customer, room, no_of_nights):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.no_of_nights = no_of_nights
        self.status = "Booked"
    def calculate_total(self):
        total = self.room.price_per_night * self.no_of_nights
        return total

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.customers = {}
        self.bookings = {}
    def add_room(self, room):
        self.rooms[room.room_number] = room
    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
    def book_room(self, booking_id, customer_id, room_number, no_of_nights):
        if customer_id not in self.customers:
            return "Customer not found."
        customer = self.customers[customer_id]

        if room_number not in self.rooms:
            return "Room not found."
        room = self.rooms[room_number]

        if not room.availability:
            return "Room is not available."

        booking =Booking(
            booking_id,
            customer,
            room,
            no_of_nights
        )

        self.bookings[booking_id] = booking
        customer.bookings.append(booking)

        room.availability = False

        return "Room booked successfully."

    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            return "Booking not found."
        booking = self.bookings[booking_id]

        if booking.status == "Cancelled":
            return "Booked is already cancelled."

        booking.status = "Cancelled"
        booking.room.availability = True

        return "Booking cancelled successfully."


    



room1 = Room(101, "Single", 500, True)
room2 = Room(102, "Double", 1000, True)

customer1 = Customer(1, "Nitish")

hotel = Hotel()

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_customer(customer1)


# 9. 📚 Library Management System

# Classes:

# Book
# Member
# Library

# Rules:

# Member can borrow maximum 3 books.
# Book can't be borrowed if unavailable.
# Returning a book makes it available.
# Calculate late fee.

# Challenge:

# Late days × ₹10
# 🎯 Your progression

# I recommend this order:

# Level 1
# Single Class
#     ↓
# You completed ✅
#     ↓
# Level 2
# Multiple Classes
#     ↓
# 1. Bank Management
#     ↓
# 2. Advanced Shopping Cart
#     ↓
# 3. School Management
#     ↓
# 4. Car Rental
#     ↓
# 5. Hospital
#     ↓
# 6. Food Ordering
#     ↓
# Level 3
# Complex Object Interaction
#     ↓
# 7. Advanced ATM
#     ↓
# 8. Hotel
#     ↓
# 9. Library