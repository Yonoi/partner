from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, 0
        while j < n:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[j], nums[i] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] % 2 == 1:
                j += 1
            elif nums[i] % 2 == 0:
                i += 1
        return nums
            