from itertools import product
from copy import deepcopy
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def go(d,x,y):
    cx,cy=x,y

    while True:
        nx=cx+dx[d]
        ny=cy+dy[d]

        if nx<0 or nx>=N or ny<0 or ny>=N:
            break

        if board[nx][ny]==0:
            board[nx][ny]=board[cx][cy]
            board[cx][cy]=0
            cx,cy=nx,ny
        elif board[nx][ny]==board[cx][cy] and not visited[nx][ny]:
            board[nx][ny]=board[nx][ny]+board[cx][cy]
            board[cx][cy]=0
            visited[nx][ny]=True
            break
        else:
            break

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

n=[0,1,2,3]
mx=0

for perm in product(n,repeat=5):
    board=deepcopy(arr)
    for d in perm:

        visited=[[False]*N for _ in range(N)]

        if d==0:
            for i in range(1,N):
                for j in range(N):
                    if board[i][j]:
                        go(d,i,j)
        elif d==1:
            for i in range(N):
                for j in range(N-2,-1,-1):
                    if board[i][j]:
                        go(d,i,j)
        elif d==2:
            for i in range(N-2,-1,-1):
                for j in range(N):
                    if board[i][j]:
                        go(d,i,j)
        elif d==3:
            for i in range(N):
                for j in range(1,N):
                    if board[i][j]:
                        go(d,i,j)
        
    mx=max(mx,(max(max(lst) for lst in board)))

print(mx)