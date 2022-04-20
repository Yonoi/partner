# 388. Longest Absolute File Path
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans = 0
        stack = []
        dir_file_lst = input.split('\n')
        for dir_file in dir_file_lst:
            level = dir_file.count('\t')
            if level == 0 and '.' not in dir_file:
                stack.append(dir_file)
            elif level == 0 and '.' in dir_file:
                ans = max(ans, len(dir_file))
            else:
                while len(stack) < level + 1:
                    stack.pop()
                stack.append(dir_file)
                if '.' in dir_file:
                    ans = max(ans, len('/'.join(stack)))

        return ans
        

