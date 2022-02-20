n, k = list(map(int, input().split(' ')))
m = n
inputs = []
while m > 0:
    inputs.append(list(map(int, input().split(' '))))
    m -= 1

res = 0
for i in range(n):
    for j in range(i + 1, n):
        if len(set([a + b for a, b  in zip(inputs[i], inputs[j])])) == 1:
            res += 1
print(res)
