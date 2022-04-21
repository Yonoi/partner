# 824. Goat Latin
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()

        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for idx, word in enumerate(words):
            if word[0] in vowel:
                new_word = word + 'ma'
            else:
                new_word = word[1:] + word[0] + 'ma'

            words[idx] = new_word + 'a' * (idx + 1)
        
        return ' '.join(words)