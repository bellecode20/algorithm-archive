from copy import deepcopy

dx=[-1,-1,0,1,1,1,0,-1]#↑, ↖, ←, ↙, ↓, ↘, →, ↗
dy=[0,-1,-1,-1,0,1,1,1]\

def fish(n,arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0]==n:
                return i,j,arr[i][j][1] #해당 물고기의 좌표랑 방향

def dfs(x,y,direction, fish_sum,arr):
    global max_result

    max_result=max(max_result,fish_sum)

    #1번 16번 물고기까지 차례대로 이동
    for i in range(1,17):
        fx, fy, fd = fish(i, arr)
        if fd == -1:    #물고기가 없을 때
            continue
        for j in range(8):
            d = (fd+j)%8    #해당 물고기의 방향에서 반시계 방향으로 45도씩
            nx = fx+dx[d]
            ny = fy+dy[d]

            if 0<=nx<4 and 0<=ny<4 and (nx,ny)!=(x,y):  #해당방향으로 갈 수 있으면
                arr[fx][fy][1]=d
                arr[fx][fy],arr[nx][ny]=arr[nx][ny],arr[fx][fy] #위치바꾸기
                break

    #상어
    for k in range(1,4):    #1칸, 2칸, 3칸씩 뻗어나가기
        nx = x+dx[direction]*k
        ny = y+dy[direction]*k

        if 0<=nx<4 and 0<=ny<4 and arr[nx][ny][1] !=-1:
            n=arr[nx][ny][0]
            d=arr[nx][ny][1]

            arr[nx][ny][1]=-1   #먹기
            arr_copy = deepcopy(arr)

            dfs(nx,ny,d,fish_sum+n,arr_copy)

            arr[nx][ny][1]=d


arr = [[[0]*2 for _ in range(4)] for _ in range(4)]
for i in range(4):
    lst = list(map(int,input().split()))
    for j in range(4):
        arr[i][j] = [lst[j*2], lst[j*2+1]-1]    #물고기번호, 방향

max_result=0 #상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 담을 변수
first_direction=arr[0][0][1]
arr[0][0][-1]=-1    #맨처음 물고기 먹기

dfs(0,0,first_direction,arr[0][0][0],arr)

print(max_result)