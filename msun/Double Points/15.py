# 15. 3Sum
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans = []
        for i in range(n):
            if nums[i] > 0:
                return ans
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                summary = nums[i] + nums[left] + nums[right]
                if summary == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1] :
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif summary < 0:
                    left += 1
                else:
                    right -= 1
        return ans


