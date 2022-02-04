class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = {}
        for key in set(s):
            count_dict[key] = 0
        
        for key in s:
            count_dict[key] += 1

        res = ''
        for key, value in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
            res += key * value
        
        return res

if __name__ == "__main__":
    s = Solution()
    string = "Aabb"
    print(s.frequencySort(string))