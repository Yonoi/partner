#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return string字符串
#
class Solution:
    def compress(self , str):
        stack = []
        letter = ''

        for ch in str:
            if ch == ']':
                array_str = ''
                letter = ''
                while letter != '[':
                    array_str += letter
                    letter = stack.pop()
                array_str = array_str[::-1].split('|')
                decompress_str = int(array_str[0]) * array_str[1]

                stack.extend(list(decompress_str))
            
            else:
                stack.append(ch)
            print(stack)
        return ''.join(stack)

if __name__ == '__main__':
    s = Solution()
    strings = "HG[3|B[2|CA]]F[3|B]"
    print(s.compress(strings))
    