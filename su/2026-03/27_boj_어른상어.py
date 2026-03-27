from pprint import pprint

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def search_next_dir():
    
    for shark_num in range(1, M+1):
        # 없는 상어
        cur_dir = shark_dir[shark_num]
        if cur_dir == 0:
            continue
        
        # 냄새 없는 칸 찾기
        for next_dir in dir_priority[shark_num][cur_dir]:
            r, c = shark_pos[shark_num]
            nr = r + dr[next_dir]
            nc = c + dc[next_dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if smell_graph[nr][nc] == 0:
                break

        # 그게 없다면 내 냄새 찾기
        else:
            for next_dir in dir_priority[shark_num][cur_dir]:
                r, c = shark_pos[shark_num]
                nr = r + dr[next_dir]
                nc = c + dc[next_dir]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if smell_graph[nr][nc][0] == shark_num:
                    break

        shark_dir[shark_num] = next_dir

def move_shark():
    global shark_count

    for shark_num in range(1, M+1):
        dir = shark_dir[shark_num]
        if dir == 0:
            continue

        r, c = shark_pos[shark_num]
        nr = r+dr[dir]
        nc = c+dc[dir]

        shark_graph[r][c] = 0
        if shark_graph[nr][nc]:
            shark_pos[shark_num] = 0
            shark_dir[shark_num] = 0
            shark_count -= 1
            continue

        shark_pos[shark_num] = (nr, nc)
        shark_graph[nr][nc] = shark_num

def update_smell():
    for r in range(N):
        for c in range(N):
            if smell_graph[r][c] == 0:
                continue
            
            smell_graph[r][c][1] -= 1
            if smell_graph[r][c][1] == 0:
                smell_graph[r][c] = 0

            
    for shark_num in range(1, M+1):
        if shark_pos[shark_num] == 0:
            continue
        
        r, c = shark_pos[shark_num]
        smell_graph[r][c] = [shark_num, K]
    
        



# N : 맵 크기
# M : 상어 수
# K : 냄새 지속 시간
N, M, K = map(int, input().split())
shark_count = M

shark_graph = [list(map(int, input().split())) for _ in range(N)]
# dir_priority[상어 번호][현재 방향] = [다음 방향 탐색 순서]
dir_priority = [[-1 for _ in range(5)] for _ in range(M+1)]
shark_dir = [0] + list(map(int, input().split()))

# i : 상어 번호
# j : 현재 방향
for i in range(1, M+1):
    for j in range(1, 5):
        dir_priority[i][j] = list(map(int, input().split()))


shark_pos = [0]*(M+1)
smell_graph = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        shark_num = shark_graph[r][c]
        if shark_num != 0:
            shark_pos[shark_num] = (r, c)
            smell_graph[r][c] = [shark_num, K]

for answer in range(1, 1001):
    # 1. 모든 상어의 이동 경로를 찾기(shark_dir 갱신)
    search_next_dir()

    # 2. 상어 다음 위치 이동
    move_shark()

    # 3. 냄새 맵 반영
    update_smell()

    if shark_count == 1:
        print(answer)
        exit()

print(-1)


# - 현재 맵 : shark_graph
# - 상어의 위치 : shark_pos
# - 상어의 방향 : shark_dir
# - 남은 상어의 수 : M
# - 냄새 맵 : smell_graph

# 이동 & 쫓아내기
# ㄱ. 모든 상어의 이동 경로를 찾기 -> shark_dir
#    -> dict 키 : 좌표(튜플)), 밸 : 상어의 번호 모음(리스트)
# ㄴ. 상어 다음 위치 이동 > shark_graph, shark_pos, M
# ㄷ. 냄새 맵 반영 > smell_graph