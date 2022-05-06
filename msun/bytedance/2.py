def panduan(l):
    for i in range(len(l)):
        a = l[i]
        for idx, ch in enumerate(l):
            if a == ch[:len(a)] and not idx == i:
                return "YES"
    return "NO"

if __name__ == "__main__":
    n = int(input())
    for k in range(n):
        t = int(input())
        l = []
        for j in range(t):
            l.append(input())
        res = panduan(l)
        print(res)