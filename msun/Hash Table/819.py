# 819. Most Common Word
from typing import List
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        replace_dict = {'!':'', '?':'', '\'':'', ',':'', ';':'', '.':''}

        def replace_all(text, d):
            for k, v in d.items():
                text = text.replace(k, v)
            return text

        paragraph = replace_all(paragraph, replace_dict).lower().split()
        counter = Counter(paragraph)

        ans = []
        maximum = 0    
        for key, value in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            if maximum <= value and key not in banned:
                maximum = value
                ans.append(key)
        return ans