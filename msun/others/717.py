class Solution:
    def isOneBitCharacter(self, bits: list) -> bool:
        res = True
        i, length = 0, len(bits) - 1
        while i < length:
            if bits[i] == 0:
                i += 1
            elif bits[i:i+2] in [[1, 0], [1, 1]] and i + 2 <= length:
                i += 2
            else:
                i += 1
                res = False
        return res

if __name__ == '__main__':
    s = Solution()
    bits = [0, 1, 1, 1, 0]
    print(s.isOneBitCharacter(bits))


