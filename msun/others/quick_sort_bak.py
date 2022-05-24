class Solution:
    def quick_sort(self, nums):
        if len(nums) > 1:
            i, j = 1, len(nums) - 1
            stone = nums[0]
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