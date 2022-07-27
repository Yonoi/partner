"592. Fraction Addition and Subtraction"
from functools import reduce
class Solution:

    def gcd(self, a: int, b: int):
        if a < b:
            b, a = a, b
        if b != 0:
            return self.gcd(b, a % b)
        else:
            return a

    def fractionAddition(self, expression: str) -> str:
        if expression[0] == '-':
            expression = '0/1' + expression
        else:
            expression = '0/1+' + expression
        operators = []

        fractions = sum([each.split('-') for each in expression.split('+')], [])
        for operator in expression:
            if operator in ['+', '-']:
                operators.append(operator)
        numerators = [int(each.split('/')[0]) for each in fractions]
        denominators = [int(each.split('/')[1]) for each in fractions]
        common_multiple = reduce(lambda x, y: x * y, denominators)
        
        res_deno = common_multiple
        res_nume = numerators[0]

        for index, op in enumerate(operators):
            if op == '+':
                res_nume += (numerators[index + 1] * common_multiple / denominators[index + 1])
            else:
                res_nume -= (numerators[index + 1] * common_multiple / denominators[index + 1])
        
        op = ''
        if res_nume < 0:
            res_nume = abs(res_nume)
            op = '-'

        gcd_num = self.gcd(res_nume, res_deno)
        res = op + str(int(res_nume / gcd_num)) + '/' + str(int(res_deno / gcd_num))
        return res

if __name__ == '__main__':
    expression = "1/3-1/2"
    s = Solution()
    print(s.fractionAddition(expression))

            
            