from collections import deque
from copy import deepcopy

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def ice_cnt(x,y):
    cnt=1
    q=deque([(x,y)])
    visited[x][y]=1

    while q:
        cx,cy=q.popleft()

        for i in range(4):
            nx,ny= cx+dx[i],cy+dy[i]

            if nx<0 or nx>=2**N or ny<0 or ny>=2**N:
                continue
            if visited[nx][ny]:
                continue
            if not arr[nx][ny]:
                continue
            cnt+=1
            q.append((nx,ny))
            visited[nx][ny]=1
    return cnt

def ice_check(x,y):
    cnt=0
    for i in range(4):
        nx,ny= x+dx[i],y+dy[i]
        if nx<0 or nx>=2**N or ny<0 or ny>=2**N:
            continue
        if rotated90_lst[nx][ny]:
            cnt+=1
    if cnt>=3: return True
    else: return False

def rotate90(x,y):
    for i in range(R):
        for j in range(R):
            rotated90_lst[x+j][y+R-i-1]=arr[x+i][y+j]

N, Q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**N)]
L_lst=list(map(int,input().split()))
ice_sum=0
max_ice_cnt=0
visited=[[0]*(2**N) for _ in range(2**N)]

for q in range(Q):
    L=L_lst[q]
    R=2**L
    rotated90_lst=[[0]*(2**N) for _ in range(2**N)]

    for i in range(0,2**N,R):
        for j in range(0,2**N,R):
            rotate90(i,j)

    ice_minus_lst=[]
    for i in range(2**N):
        for j in range(2**N):
            if rotated90_lst[i][j]:
                T_or_F=ice_check(i,j)
                if T_or_F==False:
                    ice_minus_lst.append((i,j))

    for x,y in ice_minus_lst:
        rotated90_lst[x][y]-=1
    
    arr=deepcopy(rotated90_lst)
    
for i in range(2**N):
    for j in range(2**N):
        ice_sum+=arr[i][j]

for i in range(2**N):
    for j in range(2**N):
        if visited[i][j] or not arr[i][j]:
            continue
        max_ice_cnt=max(max_ice_cnt,ice_cnt(i,j))


print(ice_sum)
print(max_ice_cnt)

