

def binary_search(nums:list[int], target:int) -> int :
    n = len(nums)

    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target :
            high = mid - 1
        else:
            low = mid + 1

nums = [1, 8, 9, 45, 78, 9, 11, 56]

nums.sort() 
print(nums)
target = 11

result = binary_search(nums, target)
print(result)



