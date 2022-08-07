from collections import Counter
from collections import defaultdict
while True:
    try:
        n = int(input())
        pos = list(map(int, input().strip().split(' ')))
        neg = list(map(int, input().strip().split(' ')))
    
    except:
        break
    
    ans = n + 1
    half = n // 2 + 1
    same_dict = defaultdict(int)

    for i in range(n):
        if pos[i] == neg[i]:
            same_dict[pos[i]] += 1

    pos_count = Counter(pos)
    neg_count = Counter(neg)

    for key in neg_count.keys():
        neg_count[key] -= same_dict[key]

    for key, value in pos_count.items():
        if value >= half:
            ans = 0
            break
        try:
            if value + neg_count[key] >= half:
                ans = min(ans, half - value)
        except:
            pass
    
    for key, value in neg_count.items():
        if value >= half:
            ans = half
            break
    ans = ans if ans != (n + 1) else -1
    print(ans)
