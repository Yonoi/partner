class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'a':0, 'b':0, 'l':0, 'o':0, 'n':0}
        
        for s in text:
            try:
                d[s] += 1
            except KeyError:
                pass
        
        d['l'] //= 2
        d['o'] //= 2

        return min(d.values())

if __name__ == '__main__':
    s = Solution()
    text = "nlaebolko"
    print(s.maxNumberOfBalloons(text))