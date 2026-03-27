dx=[-1,1,0,0]
dy=[0,0,-1,1]

def go(n,x,y,d):
    cx,cy=x,y
    #자신의 방향에 따른 우선순위대로 갈 수 있는지 여부 판단
    mine_x,mine_y,mine_d=-1,-1,-1
    for i in directions[n-1][d]:    #n번째 상어의 d방향일때 우선순위
        nx=cx+dx[i]
        ny=cy+dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        
        if smell_memo[nx][ny][0]==-1:   #아무냄새 없는 빈칸일때
            return (nx,ny,i)
        elif smell_memo[nx][ny][0]==n and mine_x==-1:
            mine_x=nx
            mine_y=ny
            mine_d=i
    return (mine_x,mine_y,mine_d)



N, M, K= map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
smell_memo=[[[-1,-1] for _ in range(N)] for _ in range(N)]   #각 칸마다 상어번호, 뿌린냄새 남은 시간
current_d=[x-1 for x in map(int,input().split())]    #상어들의 현재 바라보고 있는 방향
directions = [[[x-1 for x in map(int, input().split())] for _ in range(4)] for _ in range(M)]   #위 아래 왼쪽 오른쪽/directions[0][0]은 0번째 상어의 방향이 위를 향할때의 우선순위 리스트
#0위 1아래 2왼 3오
shark_cnt=M

if M==1:
    print(0)
    exit()

#현재 위치에 냄새뿌리기
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            smell_memo[i][j][0]=arr[i][j]
            smell_memo[i][j][1]=K+1

time=0
while time<1001:
    time+=1
    #냄새 시간 감소
    for i in range(N):
        for j in range(N):
            if smell_memo[i][j][1]>0:
                smell_memo[i][j][1] -=1
                if smell_memo[i][j][1] == 0:
                    smell_memo[i][j]=[-1,-1]

    #각 상어의 이동할 위치 파악
    nxt={}#상어번호:(nx,ny,nd)
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                shark_num=arr[i][j]
                result=go(shark_num,i,j,current_d[shark_num-1])
                nxt[shark_num]=result
                arr[i][j]=0

    #정원초과된 칸은 번호 큰 상어 죽이기
    over={}
    for shark_num,(nx,ny,nd) in nxt.items():
        if (nx,ny) not in over:
            over[(nx,ny)]=shark_num
        else:
            if shark_num<over[(nx,ny)]:
                over[(nx,ny)]=shark_num
            shark_cnt-=1

    #이동 및 냄새뿌리기
    for (nx,ny),shark_num in over.items():
        arr[nx][ny]=shark_num
        current_d[shark_num-1]=nxt[shark_num][2]
        smell_memo[nx][ny]=[shark_num,K+1]
    
    if shark_cnt==1:
        print(time)
        exit()

print(-1)