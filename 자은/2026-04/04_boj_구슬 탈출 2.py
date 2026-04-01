dx=[-1,0,1,0]
dy=[0,1,0,-1]

def go(x,y,d):
    back=-1
    for cnt in range(1,10):
        nx,ny=x+dx[d]*cnt,y+dy[d]*cnt
        if arr[nx][ny]=='#':
            return cnt+back
        if arr[nx][ny]=='O':
            return cnt
        if arr[nx][ny] in ('B','R'):
            back-=1


def dfs(turn, rx,ry,bx,by):
    global answer

    if (turn,rx,ry,bx,by) in visited:
        return
    visited.add((turn,rx,ry,bx,by))

    if turn>10:
        return

    for i in range(4):
        r_cnt=go(rx,ry,i)
        b_cnt=go(bx,by,i)

        if r_cnt==0 and b_cnt==0:
            continue

        nrx,nry=rx+dx[i]*r_cnt,ry+dy[i]*r_cnt
        nbx,nby=bx+dx[i]*b_cnt,by+dy[i]*b_cnt

        if arr[nbx][nby]=='O':
            continue

        if arr[nrx][nry]=='O':
            answer=min(answer,turn)
            return
        
        arr[rx][ry],arr[bx][by]='.','.'
        arr[nrx][nry],arr[nbx][nby]='R','B'

        dfs(turn+1,nrx,nry,nbx,nby)

        arr[nrx][nry],arr[nbx][nby]='.','.'
        arr[rx][ry],arr[bx][by]='R','B'


N, M=map(int,input().split())
arr=[list(input()) for _ in range(N)]
answer=11

for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            rx,ry=i,j
        elif arr[i][j]=='B':
            bx,by=i,j

visited=set()
dfs(1,rx,ry,bx,by)

if answer>10:
    print(-1)
else:
    print(answer)