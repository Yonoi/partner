#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=23261&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        if number < 3:
            return number
        else:
            a, b = 1, 2
            for i in range(2, number):
                a , b = b , a + b
            return b