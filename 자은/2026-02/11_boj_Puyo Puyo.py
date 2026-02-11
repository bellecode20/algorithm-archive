from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def find(x,y):
    global finish

    q=deque([(x,y)])
    visited[x][y]=1
    color=field[x][y]
    boom=[(x,y)]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i], cy+dy[i]
            if nx<0 or nx>=12 or ny<0 or ny>=6 or visited[nx][ny]:
                continue
            if field[nx][ny]==color:
                q.append((nx,ny))
                visited[nx][ny]=1
                boom.append((nx,ny))
    if len(boom)>=4:
        finish=False
        for r,c in boom:
            field[r][c]='.'
            empty.append((r,c))

field=[list(input().rstrip()) for _ in range(12)]
turn=0

while True:
    finish=True
    visited=[[0]*6 for _ in range(12)]
    empty=[]

    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                find(i,j)
    
    if finish:break

    empty.sort(key=lambda x: (x[1],x[0]))
    for x,y in empty:
        for r in range(x,0,-1):
            field[r][y]=field[r-1][y]
        field[0][y]='.'
    turn+=1

print(turn)
