from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def boom(color,x,y):
    global finish

    q=deque()
    q.append((x,y))
    visited[x][y]=True
    boom_lst=[(x,y)]

    while q:
        cx,cy=q.popleft()
        
        for i in range(4):
            nx,ny=cx+dx[i],cy+dy[i]
            if nx<0 or nx>=12 or ny<0 or ny>=6 or visited[nx][ny]:
                continue
            if field[nx][ny]==color:
                visited[nx][ny]=True
                boom_lst.append((nx,ny))
                q.append((nx,ny))
    
    if len(boom_lst)>=4:
        finish=False
        for bx,by in boom_lst:
            field[bx][by]='.'
            empty.append((bx,by))

field=[list(input()) for _ in range(12)]
cnt=0

while True:
    finish=True
    visited=[[False]*6 for _ in range(12)]
    empty=[]

    for i in range(12):
        for j in range(6):
            if field[i][j]=='.' or visited[i][j]:
                continue
            boom(field[i][j],i,j)
    
    empty.sort(key=lambda x:(x[1],x[0]))
    for x,y in empty:
        for r in range(x,0,-1):
            field[r][y]=field[r-1][y]
        field[0][y]='.'
    
    if finish:break
    cnt+=1

print(cnt)