'''
1번은 4가지 0/1/2/3
2번은 총 2가지 0,2/1,3
3번은 4가지 0,1/1,2/2,3/3.0
4번은 4가지 0,1,3/0,1,2/1,2,3/0,2,3
5번은 1가지 0,1,2,3
'''
from copy import deepcopy

dx=[-1,0,1,0] #위 오른 아래 왼
dy=[0,1,0,-1]

def watch(lst): #각 cctv의 번호,위치, 방향을 리스트에
    blind_spot_cnt=0
    arr_copy=deepcopy(arr)
    for x,y,directions in lst:
        for d in directions:
            nx,ny=x,y
            while True:
                nx+=dx[d]
                ny+=dy[d]

                if nx<0 or nx>=N or ny<0 or ny>=M or arr_copy[nx][ny]==6:
                    break
                if arr_copy[nx][ny]==0:
                    arr_copy[nx][ny]=-1
    
    for r in arr_copy:
        blind_spot_cnt+= r.count(0)
    return blind_spot_cnt

def solve(n,lst):
    global min_result

    if n==len(cctvs):
        min_result=min(min_result,watch(lst))
        return
    
    cctv_n,x,y=cctvs[n][0],cctvs[n][1],cctvs[n][2]
    for d in cctv_info[cctv_n]:
        solve(n+1,lst+[(x,y,d)])

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cctv_info= [[],[(0,),(1,),(2,),(3,)],[(0,2),(1,3)],[(0,1),(1,2),(2,3),(3,0)],[(0,1,3),(0,1,2),(1,2,3),(0,2,3)],[(0,1,2,3)]]
cctvs= []   #cctv번호, r좌표, c좌표
min_result=N*M

for i in range(N):
    for j in range(M):
        if 1<= arr[i][j] <=5:
            cctvs.append((arr[i][j], i,j))
solve(0,[])
print(min_result)
