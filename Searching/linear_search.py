
# Linear Search Apporach

# Find the First Occurrence
'''nums = [5, 3, 7, 3, 9, 3]
target = 3

for i, num in enumerate(nums):
    if num == target:
        break
print(i)'''

# Find the Last Occurrence
'''nums = [5, 3, 7, 3, 9, 3]
target = 3

max_index = 0

for index, num in enumerate(nums):
    if num == target:
        if index > max_index:
            max_index = index    
print(max_index)'''


# Count Occurrences
# Given:

'''from collections import Counter
nums = [2, 5, 2, 8, 2, 9, 5]
target = 2

counts = Counter(nums)
print(counts[target])
# OR
count = 0
for num in nums:
    if num == target:
        count +=1
print(count)'''



# Find the Maximum Element
'''nums = [12, 5, 27, 3, 19, 8]

max_element = 0
for num in nums:
    if num > max_element:
        max_element = num
print(max_element)

#OR

print(max(nums))'''


# Find the Minimum Element
'''nums = [12, 5, 27, 3, 19, 8]

mini = float('inf')
for num in nums:
    if num < mini:
        mini = num
print(mini)
#OR
print(min(nums))'''


# Find Second Largest
'''nums = [10, 5, 20, 8, 20, 15]

largest = -1
second_lagest = -1

for num in nums:
    if num > largest:
        largest = second_lagest
        second_lagest =num

    elif largest > num >= second_lagest:
        second_lagest = num
print(second_lagest)'''


# Find All Occurrences
'''nums = [4, 2, 7, 2, 9, 2, 5]
target = 2

ans = []
for i, num in enumerate(nums):
    if num == target:
        ans.append(i)
print(ans)'''

# Check if Array is Sorted


'''def is_sorted(nums):

    for i in range(len(nums) - 1):

        if nums[i] > nums[i + 1]:
            return False

    return True
nums = [1, 2, 3, 5, 7, 9]
print(is_sorted(nums))'''


# Find the Unique Element
# Every element appears twice except one:


# Expected:
# 4

'''nums = [4, 1, 2, 1, 2]

seen = {}

for num in nums:
    if num not in seen:
        seen[num] = 1
    else:
        seen[num] += 1

for num in nums:
    if seen[num] == 1:
        print(num)
        break'''
# OR 

'''ans =0
for num in nums:
    ans ^= num
print(ans)'''





