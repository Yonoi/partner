#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c?tpId=13&tqId=23258&ru=%2Fpractice%2F94a4d381a68b47b7a8bed86f2975db46&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&sourceUrl=
# 
# @param str string字符串 
# @return int整型
#
class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        # write code here
        flag = 0
        length = len(str)
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                if str[i] == str[j]:
                    break
                if j == length - 1:
                    flag = 1
            if flag == 1:
                return i
        if j == length -1:
            return j
        else:
            return -1