dx=[0,1,0,-1]   #왼 아래 오른 위
dy=[-1,0,1,0]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
x=y=N//2
d=move_cnt=0
go=1
go_cnt=0
sand_out=0

while True:

    nx=x+dx[d]
    ny=y+dy[d]
    go_cnt+=1

    if d == 0:
        p_info=[(-1,1,0.01),(1,1,0.01),(-2,0,0.02),(2,0,0.02),(0,-2,0.05),(-1,0,0.07),(1,0,0.07),(-1,-1,0.1),(1,-1,0.1)]
        ax,ay= nx,ny-1
    elif d == 1:
        p_info=[(-1,-1,0.01),(-1,1,0.01),(0,-2,0.02),(0,2,0.02),(2,0,0.05),(0,-1,0.07),(0,1,0.07),(1,-1,0.1),(1,1,0.1)]
        ax,ay= nx+1, ny
    elif d == 2:
        p_info=[(-1,-1,0.01),(1,-1,0.01),(-2,0,0.02),(2,0,0.02),(0,2,0.05),(-1,0,0.07),(1,0,0.07),(-1,1,0.1),(1,1,0.1)]
        ax,ay= nx, ny+1
    elif d == 3:
        p_info=[(1,-1,0.01),(1,1,0.01),(0,-2,0.02),(0,2,0.02),(-2,0,0.05),(0,-1,0.07),(0,1,0.07),(-1,-1,0.1),(-1,1,0.1)]
        ax, ay= nx-1,ny

    sand_minus=0
    for r,c,p in p_info:
        if 0<=nx+r<N and 0<=ny+c<N:
            arr[nx+r][ny+c]+=int(arr[nx][ny]*p)
        else:
            sand_out+=int(arr[nx][ny]*p)
        sand_minus+=int(arr[nx][ny]*p) #격자 밖으로 가든 안가든 해당 칸에서 해당 비율만큼 모래 뺌
        
    if 0<= ax <N and 0<= ay < N:
        arr[ax][ay]+= arr[nx][ny]-sand_minus
    else:
        sand_out+=arr[nx][ny]-sand_minus

    arr[nx][ny]=0
    x,y = nx,ny
    if x==0 and y ==0:
        break

    if go_cnt==go:
        d=(d+1)%4
        go_cnt=0
        move_cnt+=1
        if move_cnt==2:
            go+=1
            move_cnt=0

print(sand_out)