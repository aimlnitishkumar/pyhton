nums = [7, 3, 8, 2, 6]

for i in range(1, len(nums)):

    print("i = ", i)

    key = nums[i]
    print("key = ", key)
    j = i-1
    print("j =", j)

    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -= 1

    nums[j+1] = key 
    print(nums)
print(nums)