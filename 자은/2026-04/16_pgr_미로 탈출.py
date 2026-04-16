from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(maps):
    
    def find(x,y,goal):
        visited=[[0]*len(maps[0]) for _ in range(len(maps))]
        q=deque([(x,y)])
        visited[x][y]=1
        while q:
            cx,cy=q.popleft()
            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                if nx<0 or nx>=len(maps) or ny<0 or ny>=len(maps[0]):continue
                if visited[nx][ny] or maps[nx][ny]=='X':continue
                if maps[nx][ny]==goal:    #목적지를 찾았다면
                    return visited[cx][cy]
                visited[nx][ny]=visited[cx][cy]+1
                q.append((nx,ny))
        return False
    
    answer = -1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                sx,sy=i,j
                break
            
    lever=find(sx,sy,'L') #레버까지 가는 시간
    if lever:   #레버를 찾았다면
        escape=find(lx,ly,'E')    #레버에서 출구까지 가는 시간
        if escape:answer=lever+escape   #출구를 찾았다면

    return answer