from collections import Counter
while True:
    try:
        n = int(input())
        lst = list(map(int, input().split(' ')))
    except:
        break

    prefix_left = [0] * (n + 1)
    prefix_right = [0] * (n + 1)

    for i in range(n):
        if lst[i] >= 0:
            prefix_left[i + 1] = prefix_left[i] + 1
        else:
            prefix_left[i + 1] = prefix_left[i]
        
        if lst[n - i - 1] <= 0:
            prefix_right[n - i - 1] = prefix_right[n - i] + 1
        else:
            prefix_right[n - i - 1] = prefix_right[n - i]
    ans = min([prefix_left[i] + prefix_right[i] for i in range(n + 1)])
    print(ans)