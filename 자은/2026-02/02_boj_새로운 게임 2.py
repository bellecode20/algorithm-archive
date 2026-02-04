dx=[0,0,-1,1]   #오른 왼 위 아래 | 0 1 2 3
dy=[1,-1,0,0]

def white(num,x,y,nx,ny):
    idx=horses_p[x][y].index(num)
    for i in range(idx,len(horses_p[x][y])):
        n=horses_p[x][y][i]
        horses_p[nx][ny].append(n)
        horses[n][0],horses[n][1]=nx,ny
    cnt=len(horses_p[x][y])-idx
    for _ in range(cnt):
        horses_p[x][y].pop()

def red(num,x,y,nx,ny):
    idx=horses_p[x][y].index(num)
    for i in range(len(horses_p[x][y])-1,idx-1,-1):
        n=horses_p[x][y][i]
        horses_p[nx][ny].append(n)
        horses[n][0],horses[n][1]=nx,ny
    cnt=len(horses_p[x][y])-idx
    for _ in range(cnt):
        horses_p[x][y].pop()

N, K = map(int,input().split())
bord = [[-1]*(N+2)]+[([-1]+list(map(int,input().split())) +[-1])for _ in range(N)]+[[-1]*(N+2)]
horses_p=[[[] for _ in range(N+2)] for _ in range(N+2)] 
horses =[0]+[list(map(int,input().split())) for _ in range(K)]
for i in range(1,K+1):
    horses[i][2]-=1
    x,y,d= horses[i]
    horses_p[x][y].append(i)
turn=0
finish=False

while turn<=1000:
    for i in range(1,K+1):
        x,y,d = horses[i]
        nx,ny=x+dx[d],y+dy[d]

        if nx<1 or nx>=N+1 or ny<1 or ny>=N+1 or bord[nx][ny]==2:  

            #이동방향 반대로 변경
            if d%2==0:d+=1  #오른,위--> 왼,아래
            else:d-=1   #왼,아래 --> 오른,위
            nx,ny=x+dx[d],y+dy[d]   #이동하려는 칸을 반대칸으로
            horses[i][2]=d  #변경한 방향은 저장해두기
            if nx<1 or nx>=N+1 or ny<1 or ny>=N+1 or bord[nx][ny]==2:
                continue
        if bord[nx][ny]==0: #이동하려는 칸이 흰색이면
            white(i,x,y,nx,ny)
        elif bord[nx][ny]==1:   #이동하려는 칸이 빨간색이면
            red(i,x,y,nx,ny)

        if len(horses_p[nx][ny])>=4:
            finish=True
            break
    turn+=1
    if finish:
        break
    
if turn>1000:
    print(-1)
else:
    print(turn)




