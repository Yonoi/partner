from collections import Counter
while True:
    try:
        N = int(input())
        A = list(map(int, input().split()))
    except EOFError:
        exit()
    
    new_lst = [abs(A[i] - A[i-1]) for i in range(1, N)]
    new_set = set(new_lst)
    counter = Counter(new_lst)

    if len(counter) != N-1:
        print("NO")
        max_repeats = max(counter.values())
        minimum, maximum = min(new_lst), max(new_lst)
        not_exists = 0
        for i in range(minimum, maximum+1):
            if i not in new_set:
                not_exists += 1
        print(max_repeats, not_exists)
    else:
        minimum, maximum = min(new_lst), max(new_lst)
        not_exists = 0
        for i in range(minimum, maximum+1):
            if i not in new_set:
                not_exists += 1
        if not_exists == 0:
            print("YES")
            print(minimum, maximum)
        else:
            print("NO")
            max_repeats = max(counter.values())
            print(max_repeats, not_exists)

