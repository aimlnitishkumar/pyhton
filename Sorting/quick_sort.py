'''def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)

        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)

def partition(nums, low, high):

    pivot = nums[high]

    i = low - 1

    for j in range(low, high):

        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    i += 1
    nums[i], nums[high] = nums[high], nums[i]

    return i'''

def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)

        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)

def partition(nums, low, high):

    pivot = nums[high]
    i = low - 1
    
    for j in range(low, high):
        if  nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[high] = nums[high], nums[i]

    return i 

nums = [7, 2, 1, 6, 8, 5, 3, 4]

quick_sort(nums, 0, len(nums) - 1)

print(nums)