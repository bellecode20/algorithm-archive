dx = [0,-1,-1,-1,0,1,1,1]   # ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
dy = [-1,-1,0,1,1,1,0,-1]

def cloud_move(d,s):
    
    for x,y in cloud:
        nx= (x+dx[d]*s+N)%N
        ny= (y+dy[d]*s+N)%N
        basket[nx][ny]+=1
        water_increase_basket.add((nx,ny))

def water_copy_magic(x,y):
    
    for i in range(1,8,2):
        diagonal_x=x+dx[i]
        diagonal_y=y+dy[i]

        if diagonal_x<0 or diagonal_x>=N or diagonal_y<0 or diagonal_y>=N:
            continue
        
        if basket[diagonal_x][diagonal_y]:
            basket[x][y]+=1

#--------------------------------------------------------------

N, M = map(int,input().split())
basket = [list(map(int,input().split())) for _ in range(N)]
move_info=[list(map(int,input().split())) for _ in range(M)]
cloud=[(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
water_increase_basket=set()
water_total=0

for d, s in move_info:
    cloud_move(d-1,s)
    cloud=[]    #모든 구름 사라짐
    
    for x,y in water_increase_basket:
        water_copy_magic(x,y)
    
    
    for i in range(N):
        for j in range(N):
            if basket[i][j]>=2: #바구니에 저장된 물의 양이 2 이상일때
                if (i,j) not in water_increase_basket:  #구름이 사라졌던 칸이 아니라면
                    cloud.append((i,j))
                    basket[i][j]-=2
    water_increase_basket=set()    #물이 증가됐던 칸 기록 초기화            


for lst in basket:
    water_total+=sum(lst)

print(water_total)
