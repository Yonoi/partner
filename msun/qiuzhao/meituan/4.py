from collections import defaultdict
import math
while True:
    try:
        n, k = list(map(int, input().strip().split(" ")))
        lst = list(map(int, input().strip().split(" ")))
    except:
        break

    train_idx = []
    test_idx = []
    label_dict = defaultdict(list)

    for i in range(n):
        label_dict[lst[i]].append(i + 1)

    for i in range(1, k + 1):
        label_dict[i].sort()
        m = len(label_dict[i])
        m = math.ceil(m / 2)
        train_idx.extend(label_dict[i][0:m])
        test_idx.extend(label_dict[i][m:])

    train_idx.sort()
    test_idx.sort()

    print(" ".join([str(idx) for idx in train_idx]))
    print(" ".join([str(idx) for idx in test_idx]))