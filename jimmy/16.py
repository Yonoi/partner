#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3?tpId=13&tqId=23287&ru=/practice/54275ddae22f475981afa2244dd448c6&qru=/ta/coding-interviews/question-ranking
# 
# @param str string字符串 
# @return string字符串
#
class Solution:
    def ReverseSentence(self , str: str) -> str:
        # write code here
        return ' '.join(reversed(str.split(' ')))

