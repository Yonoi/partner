#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=23255&ru=/practice/8c82a5b80378478f9484d87d1c5f12a4&qru=/ta/coding-interviews/question-ranking
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        if n <= 2:
            return 1
        else:
            a , b = 1 , 1
            for i in range(2, n):
                a , b = b , a + b
            return b