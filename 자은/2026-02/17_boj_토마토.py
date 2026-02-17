from collections import deque

dx=[0,0,-1,1,0,0]
dy=[0,0,0,0,-1,1]
dz=[-1,1,0,0,0,0]

M, N, H=map(int,input().split())
tomato_info=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited=[[[0]*M for _ in range(N)] for _ in range(H)]
empty=0
cnt=0
q=deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato_info[h][i][j]==1:
                q.append((h,i,j))
                visited[h][i][j]=1
            elif tomato_info[h][i][j]==-1:
                empty+=1
                visited[h][i][j]=-1
            elif tomato_info[h][i][j]==0:
                cnt+=1

if len(q)==M*N*H or empty==M*N*H:
    print(0)
else:
    while q:
        cz,cx,cy,=q.popleft()
        
        for i in range(6):
            nz,nx,ny=cz+dz[i],cx+dx[i],cy+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M or nz<0 or nz>=H or visited[nz][nx][ny]:
                continue
            if tomato_info[nz][nx][ny]==-1:
                continue
            visited[nz][nx][ny]=visited[cz][cx][cy]+1
            cnt-=1
            q.append((nz,nx,ny))

    if cnt==0:
        print(visited[cz][cx][cy]-1)
    else:
        print(-1)