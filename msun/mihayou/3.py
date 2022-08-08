mod = int(10 ** 9 + 7)
import math
while True:
    try:
        n, k = list(map(int, input().strip().split(" ")))
    except:
        break
    
    k = min(k, math.ceil(n / 2))
    ans = 0
    for i in range(1, k + 1):
        ans += ((2 ** i) * 2) % mod
    ans += ((n - 2 * k) * (2 ** k) % mod)

    print(ans)
