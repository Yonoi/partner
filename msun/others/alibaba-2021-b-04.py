A, B, a, b = list(map(int, input().split(' ')))
div = a / b
for i in range(1, B + 1):
    if i * div <= A:
        pass
    else:
        break
print(int((i - 1) * div), i - 1)