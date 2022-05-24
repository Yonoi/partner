n = int(input())
each_angle = (n - 2) * 180 / n
i, res = 0, 0
flag = False
while True:
    new_angle = each_angle - i * (180 - each_angle)
    if 0 < new_angle < 90:
        res += 1
    if new_angle <= 0:
        break
    if int(new_angle) == 60:
        flag = True
    i += 1

res = (res * n - n / 3 * 2) if flag else res * n
print(int(res))