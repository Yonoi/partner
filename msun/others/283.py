class Solution:
    def move_zeros(self, nums: list):
        n = len(nums)
        i, j = 0, 0

        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                j += 1
        return nums
if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    print(s.move_zeros(nums))