from collections import Counter
while True:
    try:
        N = int(input())
        H, T = [], []
        for i in range(N):
            h, t = list(map(int, input().split()))
            H.append(h)
            T.append(t)
    except EOFError:
        exit()
    counter = Counter(H)
    heightest = max(H)
    if counter[heightest] > (N / 2):
        print(0)
    else:
        ans = 0
        flag = False
        H_T = [[h, t] for h, t in zip(H, T)]
        H_T = sorted(H_T, key=lambda x: x[1], reverse=True)
        while len(H_T) != 1:
            h_t = H_T.pop()
            ans += h_t[1]
            H = [each[0] for each in H_T]
            T = [each[1] for each in H_T]
            counter = Counter(H)
            heightest = max(H)
            if counter[heightest] > (len(H) / 2):
                flag = True
        if flag:
            print(ans)
        else:
            print(0)

