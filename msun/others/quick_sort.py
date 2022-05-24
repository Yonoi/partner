class Solution:
    def quick_sort(self, nums):
        if len(nums) > 1:
            stone = nums[0]
            i, j = 1, len(nums) - 1
            while i < j:
                if nums[j] <= stone:
                    if nums[i] > stone:
                        nums[i], nums[j] = nums[j], nums[i]
                    else:
                        i += 1
                else:
                    j -= 1
            if nums[0] > nums[j]:
                nums[0], nums[j] = nums[j], nums[0]
        else:
            return nums
        return self.quick_sort(nums[:j]) + self.quick_sort(nums[j:])

if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 4, 5, 6, 7, 8]
    print(s.quick_sort(nums))
