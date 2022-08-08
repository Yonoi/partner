from functools import reduce
from decimal import Decimal
mod = int(10 ** 9 + 7)
while True:
    try:
        n, k = list(map(int, input().strip().split(" ")))
        A = list(map(int, input().strip().split()))
    except:
        break
    
    ans = 0
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i

    for i in range(k, n + 1):
        ans += (reduce(lambda x, y: x * y, [each for each in range(i - k, k + 1)]) * A[i]) % mod
    
    print(int(ans % mod))