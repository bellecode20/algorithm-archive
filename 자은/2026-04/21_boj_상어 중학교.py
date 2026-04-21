from collections import deque
from copy import deepcopy

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def group(x,y,n):
    global big_blocks, bx, by, mx_r

    q=deque([(x,y)])
    rainbow=[[False]*N for _ in range(N)]   #무지개블록 중복으로 세는거 방지용
    visited[x][y]=n
    r_cnt=0   #무지개블록개수
    blocks=set()
    while q:
        cx,cy=q.popleft()
        blocks.add((cx,cy))

        for i in range(4):
            nx,ny=cx+dx[i],cy+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny]==-1:
                continue
            if not rainbow[nx][ny] and arr[nx][ny]==0:  #무지개블록일때
                r_cnt+=1  #무지개 블록 개수+1
                rainbow[nx][ny]=True
                q.append((nx,ny))
                continue
            if visited[nx][ny]: #이미 방문한 일반블록
                continue
            if arr[nx][ny]==n:  #같은 색일때
                visited[nx][ny]=n
                q.append((nx,ny))

    update=False
    if len(blocks)>len(big_blocks):update=True
    elif len(blocks)==len(big_blocks):
        if r_cnt>mx_r:
            update=True
        elif r_cnt==mx_r:
            if x>bx:update=True
            elif x==bx:
                if y>by:update=True

    if update:
        big_blocks=blocks
        bx,by=x,y
        mx_r=r_cnt


def gravity(x,y):
    cx,cy=x,y
    while cx<N-1 and arr[cx][cy]>=0 and arr[cx+1][cy]==EMPTY:
        arr[cx][cy],arr[cx+1][cy]=arr[cx+1][cy],arr[cx][cy]
        cx+=1

N, M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
score=0
EMPTY=M+1

while True:
    visited=[[False]*N for _ in range(N)]
    big_blocks=set()  #가장 큰 블록그룹
    bx=by=-1 #가장 큰 블록그룹의 기준블록
    mx_r=0   #가장 큰 블록그룹의 무지개블록 개수

    #가장 큰 그룹 찾기
    for i in range(N):
        for j in range(N):
            if 0<arr[i][j]<EMPTY and not visited[i][j]:
                group(i,j,arr[i][j])

    if len(big_blocks)<2:   #제일 큰 블록그룹의 블록개수가 2보다 적으면
        break   #종료

    #점수 획득
    score+=len(big_blocks)**2

    #가장 큰 블록그룹 제거
    for x,y in big_blocks:
        arr[x][y]=EMPTY

    #중력작용
    if N>1:
        for i in range(N-2,-1,-1):
            for j in range(N):
                if arr[i][j]==-1 or arr[i][j]==EMPTY:continue
                if 0<=arr[i][j]<=M and arr[i+1][j]==EMPTY:
                    gravity(i,j)

    #90도 반시계 회전
    arr_copy=[[EMPTY]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_copy[N-1-j][i]=arr[i][j]
    arr=deepcopy(arr_copy)

    #중력작용
    if N>1:
        for i in range(N-2,-1,-1):
            for j in range(N):
                if arr[i][j]==-1 or arr[i][j]==EMPTY:continue
                if 0<=arr[i][j]<=M and arr[i+1][j]==EMPTY:
                    gravity(i,j)
    
print(score)