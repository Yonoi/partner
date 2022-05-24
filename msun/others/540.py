class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(s.singleNonDuplicate(nums))