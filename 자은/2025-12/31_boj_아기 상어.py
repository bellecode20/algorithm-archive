# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치

from collections import deque

dx= [-1, 0, 1, 0]   # 위 왼 아래 오른
dy= [0, -1, 0, 1]

def find_fish(start_x,start_y,shark):
    fish_position=[]

    for i in range(N):
        for j in range(N):
            if 0<arr[i][j]<shark: #물고기가 아기상어보다 작을때

                visited=[[0]*N for _ in range(N)]
                q=deque()
                q.append([start_x,start_y,0])
                visited[start_x][start_y]=1
                distance=-1

                while q:    #아기상어부터 해당 물고기 위치까지 최소 거리구하기
                    cx, cy, dist = q.popleft()
                    visited[cx][cy]=1
                    if cx==i and cy==j:
                        distance=dist
                    for k in range(4):
                        nx=cx+dx[k]
                        ny=cy+dy[k]

                        if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]:
                            continue
                        if arr[nx][ny]>shark:
                            continue
                        q.append([nx,ny,dist+1])
                if distance != -1: 
                    fish_position.append((i,j,distance))    #물고기 위치랑 해당 물고기까지의 최소거리
    if fish_position:
        sorted_fish = sorted(fish_position, key=lambda x: (x[2],x[0],x[1]))
        return sorted_fish[0]   #먹을 수 있는 물고기 중에 거리가 가장 가까운 물고기의 좌표랑 거리 값 return
    else:
        return False   #먹을 수 있는 물고기가 없을때



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
shark=2
time=0
eating=0

for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            start_x=i
            start_y=j
            break

while True:
    arr[start_x][start_y]=0
    if find_fish(start_x,start_y,shark):
        next_x,next_y,distance=find_fish(start_x,start_y,shark)
        arr[next_x][next_y]=0
        time+=distance
        eating+=1
        if eating==shark:
            eating=0
            shark+=1

        start_x,start_y=next_x,next_y
        
    else:
        break


print(time)