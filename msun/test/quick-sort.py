def partition(nums, left, right):
    key = nums[left]
    
    while left < right:
        while left < right and nums[right] >= key:
            right -= 1
        nums[left] = nums[right]

        while left < right and nums[left] <= key:
            left += 1
        nums[right] = nums[left]

    nums[left] = key
    return left

def quick_sort(nums, left, right):
    pivot = 0
    if left < right:
        pivot = partition(nums, left, right)
        quick_sort(nums, left, pivot-1)
        quick_sort(nums, pivot+1, right)

def main():
    nums = [3, 4, 2, 4, 0, 1, 6]
    n = len(nums)
    quick_sort(nums, 0, n-1)
    print(nums)

if __name__ == '__main__':
    main()