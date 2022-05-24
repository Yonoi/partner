mod = int(1e9+7)
nums = int(input())
while nums > 0:
    A, B, n = list(map(int, input().split(' ')))
    
    res_n = 0
    res_n_1 = A % mod
    res_n_2 = 2 % mod
    if n == 1:
        print(res_n_1)
        continue
    else:
        i = 2
        while i <= n:
            res_n = (A * res_n_1 - B * res_n_2) % mod
            res_n_1, res_n_2 = res_n, res_n_1
            i += 1
        print(res_n)
    nums -= 1