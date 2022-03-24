#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/0e26e5551f2b489b9f58bc83aa4b6c68?tpId=13&tqId=1374738&ru=%2Fpractice%2F1c82e8cf713b4bbeb2a5b31cf5b0417c&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&sourceUrl=
# 
# @param s string字符串 
# @return string字符串
#
class Solution:
    def replaceSpace(self , s: str) -> str:
        # write code here
        stack = []
        for i in s:
            if i == ' ':
                stack.append('%20')
            else:
                stack.append(i)
        return ''.join(stack)