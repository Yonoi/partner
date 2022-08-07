while True:
    try:
        T = int(input())
        for _ in range(T):
            x, y = list(map(int, input().split(' ')))
            ans = 0
            ans = int((x + y) / 3)
            ans = min(x, y, ans)
            print(ans)
    except:
        break
    
