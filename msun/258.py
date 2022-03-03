class Solution:
    def addDigits(self, num: int) -> int:
        tmp = num
        while True:
            res = 0
            while tmp != 0:
                res += tmp % 10
                tmp //= 10
            if res < 10:
                break
        return res            
        


