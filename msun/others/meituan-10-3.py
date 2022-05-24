import heapq
T = int(input())
while T > 0:
    N = int(input())
    init_state = list(map(int, list(input())))
    length = len(init_state)
    M = int(input())
    candidates = list(input())

    heap0 = []
    heap1 = []

    for i, num_person in enumerate(init_state, start=1):
        if num_person == 0:
            heapq.heappush(heap0, i)
        if num_person == 1:
            heapq.heappush(heap1, i)
    
    for candidate in candidates:
        table_idx_0 = heap0[0] if heap0 else 0
        table_idx_1 = heap1[0] if heap1 else 0

        if candidate == 'M':
            table_idx = 'f1' if table_idx_1 else 'f0'
        
        if candidate == 'F':
            table_idx = 'f0' if table_idx_0 else 'f1'

        if table_idx == 'f1':
            heapq.heappop(heap1)
            print(table_idx_1)
        else:
            table_idx_1 = heapq.heappop(heap0)
            heapq.heappush(heap1, table_idx_1)
            print(table_idx_0)

    T -= 1
