dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y,num,cnt):
    global max_sum, debug
    if cnt==3:
        if num>max_sum:
            max_sum=num
            # debug=path[:]
        return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M or visited[nx][ny]:
            continue
        else:
            visited[nx][ny]=1
            dfs(nx,ny,num+arr[nx][ny],cnt+1)
            visited[nx][ny]=0

N,M =map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
max_sum=0
visited=[[0]*M for _ in range(N)]
debug=[]

#배열을 돌면서 한칸당 4칸이 될때까지 뻗어나가면서 전부 확인
    #칸수를 세가면서 해야됨. 4칸이 되면 종료
    #자신의 칸의 정수를 더해가면서 해야됨.

for i in range(N):
    for j in range(M):
        visited[i][j]=1
        dfs(i,j,arr[i][j],0)
        visited[i][j]=0

# ㅜ모양 도형은 dfs로 안되니까 따로 체크
for i in range(N):
    for j in range(M):
        #총 4가지 버전

        #가운데 기준 왼쪽(x,y-1),오른쪽(x,y+1),아래(x+1,y)가 범위를 벗어나지 않았을 경우
        if 0<=j-1<M and 0<=j+1<M and 0<=i+1<N:
            calculate=arr[i][j]+arr[i][j-1]+arr[i][j+1]+arr[i+1][j]
            max_sum=max(max_sum,calculate)

        #위쪽, 왼쪽, 아래가 범위를 벗어나지 않았을 경우
        if 0<=i-1<N and 0<=j-1<M and 0<=i+1<N:
            calculate=arr[i][j]+arr[i-1][j]+arr[i][j-1]+arr[i+1][j]
            max_sum=max(max_sum,calculate)

        #위쪽, 왼쪽, 오른쪽이 범위를 벗어나지 않았을 경우
        if 0<=i-1<N and 0<=j-1<M and 0<=j+1<M:
            calculate=arr[i][j]+arr[i-1][j]+arr[i][j-1]+arr[i][j+1]
            max_sum=max(max_sum,calculate)

        #위쪽, 오른쪽 아래가 범위를 벗어나지 않았을 경우
        if 0<=i-1<N and 0<=j+1<M and 0<=i+1<N:
            calculate=arr[i][j]+arr[i-1][j]+arr[i][j+1]+arr[i+1][j]
            max_sum=max(max_sum,calculate)

print(debug)
print(max_sum)
