from collections import deque

T=int(input())

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[-1,-2,-2,-1,1,2,2,1]

for _ in range(T):
    I=int(input())
    x,y=map(int,input().split())
    gx,gy=map(int,input().split())

    if x==gx and y==gy:print(0)
    else:
        q=deque([(x,y,0)])
        visited=[[False]*I for _ in range(I)]
        result=float("inf")
        finish=False
        while q:
            cx,cy,cnt=q.popleft()

            for i in range(8):
                nx,ny=cx+dx[i],cy+dy[i]
                if nx<0 or nx>=I or ny<0 or ny>=I or visited[nx][ny]:
                    continue
                if nx==gx and ny==gy:
                    result=cnt+1
                    finish=True
                    break
                visited[nx][ny]=True
                q.append((nx,ny,cnt+1))
            
            if finish:break
        print(result)