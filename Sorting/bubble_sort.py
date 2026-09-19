nums = [5, 1, 2, 3, 1]

def SortArray(nums: list[int]) -> list[int]:

    n = len(nums)
    # print(n)

    for i in range(n):
        # print(i)
        for j in range(0, n - i - 1):
            # print(j)

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

print(SortArray(nums))
