n, x, y = list(map(int, input().split(' ')))
scores = list(map(int, input().split(' ')))

scores.sort()

found = False
for idx, m in enumerate(scores):
    if x <= (idx + 1) <= y and x <= (n - idx - 1) <= y:
        found = True
        break
res = m if found else -1
print(res)
