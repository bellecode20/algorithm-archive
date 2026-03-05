'''
1. 모든 물고기 복제예약
2. 모든 물고기 한 칸 이동(냄새있는칸, 상어가 있는칸, 격자 벗어나면 이동 불가능)
    이동이 불가능하면 이동가능할때까지 반시계 45도 회전
    회전해도 이동 못하면 이동안함
3. 물고기를 가장 많이 아웃시킬 수 있는 방향으로 상어 3칸 이동(상하좌우로 이동 가능)
    3칸 이동중에 격자 벗어나는 방향은 불가능
    이동 중 물고기 있으면 그 물고기 아웃
    아웃된 물고기는 냄새남김
4. 두판 전의 물고기 냄새는 사라짐
5. 물고기 복제 완

'''

dx=[0,-1,-1,-1,0,1,1,1] #←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
dy=[-1,-1,0,1,1,1,0,-1]

def fish_go(x,y,d):
    cnt=0
    while cnt<8:
        nx,ny=x+dx[d],y+dy[d]

        if nx<0 or nx>=4 or ny<0 or ny>=4 or smell[nx][ny] or (nx,ny)==(sx,sy):
            d=(d-1)%8
            cnt+=1 
            continue
        
        arr[nx][ny]+=1
        new_info.append([nx,ny,d])
        return
    arr[x][y]+=1
    new_info.append([x,y,d])


def shark_go(sx,sy):
    global new_info, arr, smell

    s_d=[2,0,6,4]
    max_eat=-1
    best_path=[]

    def find_path(x,y,path,eat_cnt,visited):
        nonlocal max_eat, best_path

        if len(path)==3:
            if eat_cnt>max_eat:
                max_eat=eat_cnt
                best_path=path[:]
            return
        
        for d in s_d:
            nx,ny=x+dx[d],y+dy[d]
            if nx<0 or nx>=4 or ny<0 or ny>=4:
                continue
            if (nx,ny) not in visited:
                find_path(nx,ny,path+[(nx,ny)],eat_cnt+arr[nx][ny],visited+[(nx,ny)])
            else:
                find_path(nx,ny,path+[(nx,ny)],eat_cnt,visited+[(nx,ny)])
    find_path(sx,sy,[],0,[])

    eaten=set()
    cx,cy=sx,sy
    for r,c in best_path:
        if arr[r][c]>0:
            smell[r][c]=3
            eaten.add((r,c))
        cx,cy=r,c

    new_info=[f for f in new_info if (f[0],f[1]) not in eaten]
    
    return cx,cy

    
M, S=map(int,input().split())   #물고기 수, 연습 횟수
info=[]
for _ in range(M):
    fx,fy,fd=map(int,input().split())
    info.append([fx-1,fy-1,fd-1])
sx,sy=map(int,input().split())
sx,sy=sx-1,sy-1
smell=[[0]*4 for _ in range(4)]

for s in range(S):
    arr=[[0]*4 for _ in range(4)]
    new_info=[]

    #모든 물고기 한칸 이동
    for x,y,d in info:
        fish_go(x,y,d)
  
    #상어 이동
    sx,sy=shark_go(sx,sy)

    #물고기 냄새
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j]-=1
    #물고기 복제
    info=new_info+info

print(len(info))
