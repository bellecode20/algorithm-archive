from collections import deque

n, W, L = map(int,input().split())
trucks=list(map(int,input().split()))

t=idx=0
bridge=deque()
for _ in range(W):
    bridge.append(0)

while idx<n:
    bridge.popleft()
    if sum(bridge)+trucks[idx]<=L:
        bridge.append(trucks[idx]) 
        idx+=1
    else: bridge.append(0)
    t+=1

while bridge:
    bridge.popleft()
    t+=1
print(t)