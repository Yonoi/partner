class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        extract_func = lambda x: [int(x.split('+')[0]), int(x.split('+')[1][:-1])]
        num1_real, num1_imag = extract_func(num1)
        num2_real, num2_imag = extract_func(num2)

        return f'{num1_real * num2_real - num1_imag * num2_imag}+{num1_real * num2_imag + num1_imag * num2_real}i'

if __name__ == '__main__':
    s = Solution()
    num1 = "0+0i"
    num2 = "0+0i"
    print(s.complexNumberMultiply(num1, num2))
        