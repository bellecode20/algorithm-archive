from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(land):
    answer = 0
    oil=[0]*len(land[0])
    
    def group(x,y):
        cnt=0
        cols=set()
        q=deque([(x,y)])
        visited[x][y]=True
        
        while q:
            cx,cy=q.popleft()
            cnt+=1
            cols.add(cy)
            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                if nx<0 or nx>=len(land) or ny<0 or ny>=len(land[0]):continue
                if visited[nx][ny] or not land[nx][ny]:continue
                visited[nx][ny]=True
                q.append((nx,ny))
        
        for c in cols:oil[c]+=cnt
    
    visited=[[False]*len(land[0]) for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] and not visited[i][j]:
                group(i,j)
    answer=max(oil)
    return answer