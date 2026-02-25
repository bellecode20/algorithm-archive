from collections import deque

def solution(n, edge):
    answer = 0
    v=[[] for _ in range(n+1)]
    for a,b in edge:
        v[a].append(b)
        v[b].append(a)
        
    q=deque()
    q.append(1)
    visited=[False]*(n+1)
    visited[1]=True
    dist=[0]*(n+1)
    while q:
        c=q.popleft()
        
        for nn in v[c]:
            if visited[nn]:continue
            dist[nn]=dist[c]+1
            visited[nn]=True
            q.append(nn)
    mx=max(dist)
    answer=dist.count(mx)
    return answer