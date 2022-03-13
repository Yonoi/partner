class Solution:
    def validUtf8(self, data: list) -> bool:
        n = len(data)
        if n == 1:
            return  '{:0>8}'.format(bin(data[0])[2:])[0] == '0' 
        
        i = 0
        while i < n:
            idx = '{:0>8}'.format(bin(data[i])[2:]).find('0')
            print(idx)
            if idx == 0:
                pass
            elif idx in [2, 3, 4]:
                j = 1
                while j < idx:
                    if '{:0>8}'.format(bin(data[i + j])[2:])[0:2] != '10':
                        return False
                    j += 1
                else:
                    i += (idx - 1)
            else:
                return False
            i += 1
        return True

if __name__ == '__main__':
    s = Solution()
    data = [240,162,138,147,145]
    print(s.validUtf8(data))