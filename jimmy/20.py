#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/6fe361ede7e54db1b84adc81d09d8524?tpId=13&tqId=1375279&ru=/practice/8ee967e43c2c4ec193b040ea7fbb10b8&qru=/ta/coding-interviews/question-ranking
# 
# @param numbers int整型一维数组 
# @return int整型
#
class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        if not numbers:
            return -1
#         while numbers:
#             num = numbers.pop(0)
#             if num in numbers:
#                 return num
        R = set()
        for i in numbers:
            if i not in R:
                R.add(i)
            else:
                return i
        return -1
    