#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=23291&ru=/practice/29311ff7404d44e0b07077f4201418f5&qru=/ta/coding-interviews/question-ranking
# 
# @param str string字符串 
# @return string字符串一维数组
#
class Solution:
    def Permutation(self , str: str) -> List[str]:
        # write code here
        if len(str) <= 1:
            return str
        result = []
        for i in range(len(str)):
            first_str = str[i]
            for j in self.Permutation(str[:i] + str[i+1:]):
                temp = first_str + j 
                if temp not in result:
                    result.append(temp)
        return result

