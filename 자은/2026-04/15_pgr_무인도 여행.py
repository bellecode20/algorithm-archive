from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(maps):
    def island(x,y):
        q=deque([(x,y)])
        visited[x][y]=True
        cnt=int(maps[x][y])
        while q:
            cx,cy=q.popleft()
            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                if nx<0 or nx>=row or ny<0 or ny>=col or visited[nx][ny]:
                    continue
                if maps[nx][ny]=='X':
                    continue

                cnt+=int(maps[nx][ny])
                visited[nx][ny]=True
                q.append((nx,ny))
        return cnt
    
    answer = []
    row=len(maps)
    col=len(maps[0])
    visited=[[False]*col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and not visited[i][j]:
                total=island(i,j)
                answer.append(total)

    if len(answer)==0:answer.append(-1)
    else:answer.sort()
    
    return answer