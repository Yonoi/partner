nums = int(input())
while nums > 0:
    n = int(input())
    x_lst = list(map(int, input().split(' ')))
    y_lst = list(map(int, input().split(' ')))
    
    res = 1
    xy_lst = sorted([(xi, yi) for xi, yi in zip(x_lst, y_lst)], key=lambda x: (x[0], -x[1]))
    max_x, max_y = xy_lst[0][0], xy_lst[0][1]
    for i in range(1, len(xy_lst)):
        if xy_lst[i][0] > max_x and xy_lst[i][1] > max_y:
            res += 1
            max_x, max_y = xy_lst[i][0], xy_lst[i][1]
    nums -= 1
    print(res)