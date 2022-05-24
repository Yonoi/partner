n = int(input())
neg_list = list(map(int, input().split(' ')))
neg_list.sort()

res = 0
for i in range(1, n + 1):
    res += abs(neg_list[i-1] - i)

print(res)