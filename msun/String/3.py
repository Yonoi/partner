"3. Longest Substring Without Repeating Characters"
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = defaultdict(int)
        queue = []
        n = len(s)
        ans = 0

        for i in range(n):
            if hash_table[s[i]] == 0:
                queue.append(s[i])
                ans = max(ans, len(queue))
                hash_table[s[i]] = 1
            else:
                while queue[0] != s[i]:
                    each = queue.pop(0)
                    hash_table[each] = 0
                queue.pop(0)
                queue.append(s[i])
        
        return ans
            


