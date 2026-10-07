
# Check Number is Palindrome or not 
'''num = int(input("Enter a number which you want to check palindrome..."))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")'''


# Check number is Armstrong or not 
'''num = int(input("Enter a number which you want to check armstrong..."))
temp = num
sum = 0


while num > 0:
    digit = num % 10
    sum = sum + digit * digit * digit
    num = num // 10

if sum == temp:
    print("Number is armstrong.")
else:
    print("Number is not armstrong.")
'''

# Print armstrong numbers in  a range.
'''for num in range(1, 500):
    
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit * digit * digit
        num = num // 10
    
    if temp == sum :
        print("Armstrong number", temp)'''

# how many of them contain an even number of digits.
nums = [12,345,2,6,7896]

even = 0
odd = 0

for num in nums:
    if len(str(num)) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even digit numbers:", even)
print("Odd digit numbers:", odd)