class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        tmp = abs(num) if num < 0 else num
        while num != 0:
            res += str(num % 7)
            num //= 7
        
        return '-' + res[::-1] if num < 0 else res