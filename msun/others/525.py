from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: list) -> int:
        n = len(nums)
        maximum = 0
        counter = 0
        hashmap = [-2] * 2 * n
        hashmap[n] = -1
        
        for i in range(n):
            if nums[i] == 0:
                counter -= 1
            else:
                counter += 1
            if hashmap[counter + n] != -2:            
                maximum = max(i - hashmap[counter + n], maximum)
            else:
                hashmap[counter + n] = i
        return maximum

if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0]
    print(s.findMaxLength(nums))