class Solution:
    def goodDaysToRobBank(self, security: list, time: int) -> list:
        n = len(security)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                right[n - i - 1] = right[n - 1] + 1
        return [i for i in range(time, n - time) if left[i] >= time and right[i] >= time]
            
                
        
if __name__ == '__main__':
    s = Solution()
    security = [1, 1, 1, 1, 1]
    time = 0

    print(s.goodDaysToRobBank(security, time))
