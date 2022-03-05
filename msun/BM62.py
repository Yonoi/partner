#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def Fibonacci(self , n: int) -> int:
        a, b, c = 1, 1, 1

        for i in range(3, n + 1):
            c = a + b
            a, b = b, c
        
        return c