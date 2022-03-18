class Solution:
    def longestWord(self, words: List[str]) -> str:
        n = len(words)
        words.sort(key=lambda x: (-len(x), x), reverse=True)

        for i in range(n-1):
            if words[i][:-1] != words[i+1] and words[i][:-1] == '':
                return 
                
        else:
            return ''  

