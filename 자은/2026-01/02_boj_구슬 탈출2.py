"""
bfs로 풀기

빨간색이 이동가능할때
파란색도 이동가능하다면 이동
만약 파란색이 구멍에 도달하면 실패

이동은 벽을 만날때까지 한 방향으로 이동해야함

이동했을때 거리를 구해서 만약 두 구슬이 겹친다면 이동거리가 길었던(겹치는 위치에 도착하는게 늦었던)구슬이 한 칸 뒤로 가야함


"""
from collections import deque

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def move(x,y,d):

    dist=0
    while arr[x + dx[d]][y + dy[d]] != '#' and arr[x][y] != 'O':
        x=x+dx[d]
        y=y+dy[d]
        dist+=1

    return x,y,dist
    

def solve(x,y,b_x,b_y):
    global min_result
    q=deque([(x,y,b_x,b_y,0)])
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[x][y][b_x][b_y] = 1

    while q:
        rx,ry,bx,by,n = q.popleft()

        if n>=10:
            continue
        
        for i in range(4):

            nx,ny,r_dist=move(rx,ry,i)
            bnx,bny,b_dist=move(bx,by,i)

            if arr[bnx][bny]=='O':
                continue
            if arr[nx][ny]=='O':
                min_result=n+1
                return

            if (nx,ny)==(bnx,bny):  #만약 도달한 위치가 같다면
                if r_dist>b_dist: #빨간구슬이 파란구슬보다 늦게 도착했다면
                    nx=nx-dx[i]
                    ny=ny-dy[i]
                
                elif r_dist<b_dist:   #파란 구슬이 빨간구슬보다 늦게 도착했다면
                    bnx=bnx-dx[i]
                    bny=bny-dy[i]
            if not visited[nx][ny][bnx][bny]:
                visited[nx][ny][bnx][bny]=1
                q.append((nx,ny,bnx,bny,n+1))
            



N, M = map(int,input().split())
arr=[list(input().strip()) for _ in range(N)]

min_result=-1
b_x=b_y=r_x=r_y=o_x=o_y=0

for i in range(N):
    for j in range(M):
        if arr[i][j]=='B':
            b_x=i
            b_y=j
        elif arr[i][j]=='R':
            r_x=i
            r_y=j
        elif arr[i][j]=='O':
            o_x=i
            o_y=j


solve(r_x,r_y,b_x,b_y)
print(min_result)