class Solution:
    def maximum(self, nums: list):
        a, b, c, d, m = nums
        max_value = 0

        for x in range(a, b + 1):
            for y in range(c, d + 1):
                mod_value = (x * y) % m
                if max_value <= mod_value:
                    max_value = mod_value
        return max_value


if __name__ == '__main__':
    s = Solution()
    nums = [2, 4, 3, 5, 7]
    print(s.maximum(nums))