from itertools import product
from copy import deepcopy
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def move(x,y,d):
    cx,cy=x,y
     
    while True:
        nx,ny=cx+dx[d],cy+dy[d]

        if nx<0 or nx>=N or ny<0 or ny>=N:
            break
         
        if board[nx][ny]==0:
            board[nx][ny]=board[cx][cy]
            board[cx][cy]=0
            cx,cy=nx,ny

        elif board[nx][ny]==board[cx][cy] and not visited[nx][ny]:
            board[nx][ny]+=board[cx][cy]
            board[cx][cy]=0
            visited[nx][ny]=True
            break
        else:
            break

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
answer=0

idx=[0,1,2,3]
for comb in product(idx,repeat=5):
    board=deepcopy(arr)
    turn=[]
    for d in comb:
        
        visited=[[False]*N for _ in range(N)]

        if d==0 or d==3:
            for i in range(N):
                for j in range(N):
                    if board[i][j]:
                        move(i,j,d)
        elif d==1 or d==2:
            for i in range(N-1,-1,-1):
                for j in range(N-1,-1,-1):
                    if board[i][j]:
                        move(i,j,d)
        
    answer=max(answer,max(max(lst) for lst in board))

print(answer)