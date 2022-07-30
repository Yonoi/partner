"31. Next Permutation"
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx_i = n

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                idx_i = i
                break
        for j in range(n - 1, idx_i, -1):
            if nums[j] > nums[idx_i]:
                nums[idx_i], nums[j] = nums[j], nums[idx_i]
                break
        
        if idx_i == n:
            idx_i = -1

        for i in range(idx_i + 1, n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


        
