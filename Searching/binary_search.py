

def binary_search(nums: list[int], target: int) -> int:
       
    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

nums = [1, 8, 9, 45, 78, 9, 11, 56]
nums.sort() 
target = 11

result = binary_search(nums, target)
print(result)



