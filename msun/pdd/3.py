
while True:
    pd = lambda x : x == x[::-1]
    try:
        T = int(input())
        for t in range(T):
            N = int(input())
            strings = ''
            flag = False
            for i in range(N):
                string = input()
                strings += string
                if pd(string) or pd(strings):
                    flag = True
            if flag:
                print("YES")
            else:
                print("NO")
    except EOFError:
        exit()