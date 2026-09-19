



def linear_search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


nums = [1, 8, 9, 45, 78, 9, 11, 56]
target = 11

result = linear_search(nums, target)
print(result)