# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        window = []
        for i, ch in enumerate(s):
            if ch not in window:
                window.append(ch)
            else:
                while ch in window:
                    window.pop(0)
                window.append(ch)
            ans = max(len(window), ans)
        return ans