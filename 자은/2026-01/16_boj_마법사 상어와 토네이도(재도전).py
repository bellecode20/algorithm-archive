dx = [0, 1, 0, -1] # 왼, 아래, 오, 위
dy = [-1, 0, 1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x = y = N // 2
d = 0
go = 1
move_cnt = 0
sand_out = 0

# 방향별 모래 비율 좌표 (r, c, 비율)
# d=0(왼쪽) 기준 설계도를 미리 만들어두면 편합니다.
def get_p_info(direction):
    if direction == 0: # 왼쪽
        return [(-1,1,0.01),(1,1,0.01),(-2,0,0.02),(2,0,0.02),(0,-2,0.05),(-1,0,0.07),(1,0,0.07),(-1,-1,0.1),(1,-1,0.1)], (0, -1)
    elif direction == 1: # 아래
        return [(-1,-1,0.01),(-1,1,0.01),(0,-2,0.02),(0,2,0.02),(2,0,0.05),(0,-1,0.07),(0,1,0.07),(1,-1,0.1),(1,1,0.1)], (1, 0)
    elif direction == 2: # 오른쪽
        return [(-1,-1,0.01),(1,-1,0.01),(-2,0,0.02),(2,0,0.02),(0,2,0.05),(-1,0,0.07),(1,0,0.07),(-1,1,0.1),(1,1,0.1)], (0, 1)
    else: # 위
        return [(1,-1,0.01),(1,1,0.01),(0,-2,0.02),(0,2,0.02),(-2,0,0.05),(0,-1,0.07),(0,1,0.07),(-1,-1,0.1),(-1,1,0.1)], (-1, 0)

finish = False
while not finish:
    # 2번 방향을 꺾으면 go가 1 늘어남 (1,1, 2,2, 3,3...)
    for _ in range(2):
        # 현재 방향(d)으로 go만큼 이동
        for _ in range(go):
            nx, ny = x + dx[d], y + dy[d]
            
            # 모래 이동 로직
            total_sand = arr[nx][ny]
            arr[nx][ny] = 0
            spread_sum = 0
            
            p_list, alpha_offset = get_p_info(d)
            for dr, dc, p in p_list:
                sand = int(total_sand * p)
                if 0 <= nx+dr < N and 0 <= ny+dc < N:
                    arr[nx+dr][ny+dc] += sand
                else:
                    sand_out += sand
                spread_sum += sand
            
            # 알파 칸 처리
            ax, ay = nx + alpha_offset[0], ny + alpha_offset[1]
            alpha_sand = total_sand - spread_sum
            if 0 <= ax < N and 0 <= ay < N:
                arr[ax][ay] += alpha_sand
            else:
                sand_out += alpha_sand
            
            x, y = nx, ny
            if x == 0 and y == 0:
                finish = True
                break
        
        if finish: break
        d = (d + 1) % 4 # 방향 전환
    go += 1 # 두 번 꺾었으니 거리 증가

print(sand_out)