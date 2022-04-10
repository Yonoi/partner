class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        alphabet = [chr(each) for each in range(97, 124)]
        morse = [".-", "-...", "-.-.", "-..", ".",
                "..-.", "--.", "....", "..", ".---",
                "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-",
                "..-", "...-", ".--", "-..-", "-.--",
                "--.."]
        d = dict(zip(alphabet, morse))
        ans = set()

        encrypt = lambda x: ''.join([d[s] for s in list(x)])
        for word in words:
            ans.add(encrypt(word))
        
        print(len(ans))
            