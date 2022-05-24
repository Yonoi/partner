class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x, y = 0, 0
        x_dict, y_dict = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
            else:
                try:
                    x_dict[secret[i]] += 1                    

                except KeyError:
                    x_dict[secret[i]] = 1
                
                try:
                    y_dict[guess[i]] += 1
                
                except KeyError:
                    y_dict[guess[i]] = 1

        for key, value in y_dict.items():
            try:
                y += min(x_dict[key], value)
                
            except KeyError:
                continue
        
        return f'{x}A{y}B' 
            

if __name__ == '__main__':
    s = Solution()
    secret = "2822013305"
    guess  = "5706322849"
    print(s.getHint(secret, guess))