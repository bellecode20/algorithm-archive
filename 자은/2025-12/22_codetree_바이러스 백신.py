from collections import deque

dx=[-1,0,1,0]   #위 오른쪽 아래 왼쪽
dy=[0,1,0,-1]

def bfs(H_lst):
    q=deque()
    visited=[[0]*N for _ in range(N)]

    for x,y in H_lst:
        q.append((x,y))
        visited[x][y]=1 #처음은 1초로 일단 방문체크(나중에 1초 빼주기)
    
    V_cnt=Virus_Cnt #바이러스 개수 복사해두기

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:  #배열을 벗어나면
                continue
            elif arr[nx][ny]==1 or visited[nx][ny]: #벽이거나 이미 방문했다면
                continue
            q.append((nx,ny))   
            visited[nx][ny]=visited[cx][cy]+1
            if arr[nx][ny]==0:  #바이러스라면
                V_cnt-=1    #바이러스 없애기
                if V_cnt==0:    #바이러스가 다 사라졌다면
                    return visited[nx][ny]-1    #기록된 시간-1 리턴
    return float("inf") #바이러스가 다 사라지지 않았다면


def dfs(n,start,H_lst):
    global time

    if n==M: #M개를 뽑으면
        time = min(time,bfs(H_lst)) #bfs돌린것중에 최소시간
        return
    
    for i in range(start, len(Hospital_lst)):
        dfs(n+1, i+1, H_lst+[Hospital_lst[i]])

N, M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

Virus_Cnt=0 #총 바이러스 개수
Hospital_lst=[] #병원 좌표 리스트

for i in range(N):
    for j in range(N):
        if arr[i][j]==0:    #바이러스 개수 세기
            Virus_Cnt+=1
        elif arr[i][j]==2:  #병원들 좌표 찾기
            Hospital_lst.append((i,j))  

if Virus_Cnt==0:    #바이러스가 없으면 답은 0초
    time=0
else:
    time=float("inf")
    dfs(0,0,[])
    if time==float("inf"):
        time=-1
print(time)