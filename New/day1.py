
# Write a program that asks the user for a number.
  #If it’s positive → print "Positive"
  #Else → print "Negative or Zero"


"""num = int(input("Enter a number : "))

if num > 0:
    print("Positive")
else:
  print("Negative or Zero")
"""


# Ask the user for their age.
   #If age ≥ 18 → print "You are an adult"
   #Else → print "You are a minor"


"""user_age = int(input("Enter your age : "))

if user_age >= 18:
    print("You are an adult")
else:
    print("You are a minor")"""



# Take a number as input.
    #If even → print "Even number"
    #Else → print "Odd number"

"""num = int(input("Enter a number : "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")"""


# Ask the user for a password.
    #If password = "python123" → print "Access Granted"
    #Else → print "Wrong Password"

"""password = input("Enter the password : ")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong Password")"""



# Ask the user for temperature in Celsius.
    #If temp ≥ 30 → print "Hot day"
    #Else → print "Cool day"

"""temperature = int(input("Enter a temperature in Celsius: "))

if temperature >= 30:
    print("Hot day")
else:
    print("Cool day")"""



# Write a program to check the largest of two numbers.

"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2 :
    print(f"First number {num1} is largest")
else:
    print(f"Second number {num2} is largest")"""



# Ask the user for 3 subject marks.
    #If average ≥ 90 → "Grade A"
    #If average ≥ 70 → "Grade B"
    #If average ≥ 50 → "Grade C"
    #Else → "Fail"


"""phy = int(input("Enter obtained marks in physics : "))
chem = int(input("Enter obtained marks in chemistry : "))
math = int(input("Enter obtained marks in mathematics : "))


avg_marks = (phy + chem + math) / 3

if avg_marks >= 90:
    print("Grade A")

elif avg_marks >=70:
    print("Grade B")

elif avg_marks >=50:
    print("Grade C")

else:
    print("Fail")"""



# Take a year as input.
    #If it’s divisible by 4 → print "Leap Year"
    #Else → print "Not a Leap Year"


"""year = int(input("Enter a year : "))

if year % 4 == 0 :
    print("Leapyear")
else:
    print("Not a Leapyear")"""


# Ask the user to enter their name.
    #If the name starts with "A" → print "Your name starts with A"
    #Else → print "Your name doesn’t start with A"

"""name = input("Enter a name : ")

if name[0].lower() == "a":
    print("Your name starts with A")
else:
    print("Your name doesn't start with A")"""


# Ask the user for their salary and years of experience.
    # If experience ≥ 5 years → give 10% bonus.
    # Else → no bonus.


"""salary = int(input("Enter your salary: "))
year_of_experience = int(input("Enter your year of experience: "))

if year_of_experience >=5:
    bonus = (salary * 10) / 100
    total_sal = bonus + salary
    print(total_sal)

else:
    print("No bonus")"""


    