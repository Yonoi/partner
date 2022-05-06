while True:
    try:
        n, m = list(map(int, input().split()))
        a_lst, b_lst = [], []
        for i in range(n):
            a, b = list(map(int, input().split()))
            a_lst.append(a)
            b_lst.append(b)
    except EOFError:
        exit()
    
    tmp = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a_lst[i] + a_lst[j] > m:
                break 
            else:
                tmp = max(tmp, b_lst[i] + b_lst[j])
    print(tmp)

    