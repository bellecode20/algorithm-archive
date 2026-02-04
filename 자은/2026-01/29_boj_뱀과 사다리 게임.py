from collections import deque

def go():
    q=deque([(1,0)])
    visited=[False]*101
    visited[1]=True
    while q:
        p, cnt=q.popleft()
        if p==100: return cnt
        for i in range(1,7):
            np=p+i
            if np>100:continue
            if np==100: return cnt+1
            if item_go[np]:np=item_go[np]
            if visited[np]:continue
            visited[np]=True
            q.append((np,cnt+1))

N, M =map(int,input().split())
item_go=[0]*101
for _ in range(N):
    x,y=map(int,input().split())
    item_go[x]=y
for _ in range(M):
    u,v=map(int,input().split())
    item_go[u]=v

result=go()
print(result)