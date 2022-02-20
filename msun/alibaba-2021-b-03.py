T = int(input())
while T > 0:
    res = 0
    n = int(input())
    a = list(map(int, input().split(' ')))
    
    minimum = min(a)
    res += sum(a[1:])
    res += (n - 2) * minimum
    print(res)
    T -= 1