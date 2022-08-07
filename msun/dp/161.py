"161. One Edit Distance"
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        if abs(m - n) > 1: 
            return False
        elif abs(m - n) == 1:
            if m < n:
                m, n = n, m
                s, t = t, s
            pm, pn = 0, 0
            while pm < m and pn < n:
                if s[pm] == t[pn]:
                    pm += 1
                    pn += 1
                else:
                    pm += 1
                
                if pm - pn > 1:
                    return False
            return True
        else:
            diff = 0
            pm, pn = 0, 0
            while pm < m and pn < n:
                if s[pm] != t[pn]:
                    diff += 1
                pm += 1
                pn += 1
            return True if diff == 1 else False
