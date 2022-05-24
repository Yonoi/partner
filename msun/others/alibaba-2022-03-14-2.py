from collections import Counter
class Solution:
    def swap_characters(self, s: str):
        n = len(s)
        total_num = n * (n - 1) / 2 + 1
        the_same_characters = sum([each[1] - 1 for each in Counter(s).items() if each[1] > 1])
        return int(total_num - the_same_characters)

if __name__ == '__main__':
    s = Solution()
    string = 'hello'
    print(s.swap_characters(string))