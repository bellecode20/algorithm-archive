import heapq

N, M = map(int,input().split())
record = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C=map(int,input().split())
    record[A].append((B,C))
    record[B].append((A,C))

min_d=[float("inf")]*(N+1)
min_d[1]=0
q=[(0,1)]
while q:
    d, cn= heapq.heappop(q)
    if min_d[cn]<d:continue
    for nn, w in record[cn]:
        cost = d+w
        if cost < min_d[nn]:
            min_d[nn] = cost
            heapq.heappush(q,(cost,nn))

print(min_d[N])