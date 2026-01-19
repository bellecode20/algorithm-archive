from copy import deepcopy

dx=[0,-1,0,1]   #오른 위 왼 아래
dy=[1,0,-1,0]

def air_clean(x):
    y=0
    x2=x+1
    y2=0
    cx=x
    cy=0

    A[x][y]=0
    for i in range(4):
        while 0<=cx<x+1 and 0<=cy<C:
            nx=cx+dx[i]
            ny=cy+dy[i]
            if nx<0 or nx>=x+1 or ny<0 or ny>=C:
                break
            if A_copy[nx][ny] !=-1:
                A_copy[nx][ny]=A[cx][cy]
            cx=nx
            cy=ny

    A[x2][y2]=0
    for i in range(4,0,-1):
        j=i%4

        while x+1<=x2<R and 0<=y2<C:
            nx2=x2+dx[j]
            ny2=y2+dy[j]
            if nx2<x+1 or nx2>=R or ny2<0 or ny2>=C:
                break
            if A_copy[nx2][ny2] != -1:
                A_copy[nx2][ny2]=A[x2][y2]
            x2=nx2
            y2=ny2   

def dust_spread(x,y):
    shared_dust_amount=A[x][y]//5
    shared_cnt=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=R or ny<0 or ny>=C:
            continue
        if A[nx][ny]==-1:
            continue
        A_copy[nx][ny]+=shared_dust_amount
        shared_cnt+=1

    A_copy[x][y]-=shared_dust_amount*shared_cnt


R,C,T = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(R)]
dust_total=0
for i in range(R):
    if A[i][0]==-1:
        air_cleaner=i
        break

for _ in range(T):
    A_copy=deepcopy(A)
    for i in range(R):
        for j in range(C):
            if A[i][j] !=-1 and A[i][j]:
                dust_spread(i,j)
    A=deepcopy(A_copy)
    air_clean(air_cleaner)
    A=deepcopy(A_copy)

for i in range(R):
    for j in range(C):
        if A[i][j] != -1 and A[i][j]:
            dust_total+=A[i][j]

print(dust_total)

