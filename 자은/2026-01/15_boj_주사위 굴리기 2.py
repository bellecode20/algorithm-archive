'''
주사위 아랫면 > 칸에 있는 정수 --> 시계방향으로 회전
주사위 아랫면 < 칸에 있는 정수 --> 반시계 방향으로 회전
주사위 아랫면 == 칸에 있는 정수 --> 변화X

북쪽면, 윗면, 남쪽면, 아랫면, 서쪽면, 동쪽면 = d1,d2,d3,d4,d5,d6

동쪽으로 이동 1
d2,d4,d5,d6 = d5,d6,d4,d2

남쪽으로 이동 2 
d1.d2.d3.d4 = d4,d1,d2,d3

서쪽으로 이동 3 
d2,d4,d5,d6 = d6,d5,d2,d4

북쪽으로 이동 0
d1,d2,d3,d4 = d2,d3,d4,d1

'''
from collections import deque

dx = [-1,0,1,0] #위 오른쪽 아래 왼쪽
dy = [0,1,0,-1]

def get_score(x,y):
    global B

    q=deque()
    q.append((x,y))
    visited = [[0]*M for _ in range(N)]
    visited[x][y]=1
    cnt = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx= cx+dx[i]
            ny= cy+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M or visited[nx][ny]:
                continue
            if Map[nx][ny]==B:
                cnt+=1
                visited[nx][ny]=1
                q.append((nx,ny))
    
    score = B*cnt
    return score

def move_dice(x,y):
    global d,d1,d2,d3,d4,d5,d6

    nx = x+dx[d]
    ny = y+dy[d]

    if nx<0 or nx >= N or ny<0 or ny>= M:
        d=(d+2)%4
        nx = x+dx[d]
        ny = y+dy[d]

    if d == 0 :
        d1,d2,d3,d4 = d2,d3,d4,d1
    elif d == 1:
        d2,d4,d5,d6 = d5,d6,d4,d2
    elif d == 2:
        d1,d2,d3,d4 = d4,d1,d2,d3
    elif d == 3:
        d2,d4,d5,d6 = d6,d5,d2,d4
    
    return nx, ny
    
N, M, K = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]

d=1 #동쪽으로 출발
d1,d2,d3,d4,d5,d6=2,1,5,6,4,3
x=y=total=0

for _ in range(K): #K만큼 주사위 이동
    
    x,y = move_dice(x,y)
    B=Map[x][y]
    total+=get_score(x,y)

    if d4 > B:
        d=(d+1)%4
    elif d4 < B:
        d=(d+3)%4

print(total)
