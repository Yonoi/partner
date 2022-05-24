class Solution:
    def minimumDifference(self, nums: list, k: int) -> int:
        md = 0
        nums.sort()
        for i in range(len(nums) - k):
            if i == 0:
                md = nums[i + k] - nums[i]
            else:
                tmp_md = nums[i + k] - nums[i]
                md = min(md, tmp_md)

        return md
