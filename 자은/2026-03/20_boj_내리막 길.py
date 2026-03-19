dx=[-1,0,1,0]
dy=[0,1,0,-1]

M, N=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(M)]
memo=[[0]*N for _ in range(M)]
memo[0][0]=1

heights=[]
for i in range(M):
    for j in range(N):
        heights.append((arr[i][j],i,j))
heights.sort(reverse=True)

for h,x,y in heights:

    for d in range(4):
        nx,ny=x+dx[d],y+dy[d]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if arr[nx][ny]>=arr[x][y]:
            continue
        memo[nx][ny]+=memo[x][y]

print(memo[M-1][N-1])
