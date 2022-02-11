class Solution:
    def simplifiedFractions(self, n: int) -> list:
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if self.gcd(i, j) == 1:
                    res.append(f"{j}/{i}")
        return res
    def gcd(self, x, y):
        if x % y == 0:
            return y
        return self.gcd(y, x % y)


if __name__ == "__main__":
    s = Solution()
    print(s.simplifiedFractions(4))