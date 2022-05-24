class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        res = list(s)

        i = n - 1
        j = 0
        while i >= 0:
            if res[j].isalpha() and s[i].isalpha():
                res[j] = s[i]
                i -= 1
                j += 1
            if not s[i].isalpha():
                i -= 1
            if not res[j].isalpha():
                j += 1
            if i == -1:
                break

        return ''.join(res)