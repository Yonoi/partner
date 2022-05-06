while True:
    try:
        N = int(input())
        A, B = [], []
        for i in range(N):
            Ai, Bi = list(map(int, input().split()))
            A.append(Ai)
            B.append(Bi)
    except EOFError:
        exit()
    print(sum(B) + min(A))