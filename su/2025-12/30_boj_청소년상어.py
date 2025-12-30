# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

from copy import deepcopy

def pprint(board):
    for r in range(N):
        print(board[r])
    print("\n")

N = 4
graph = [[0] * N for _ in range(N)]
fishes = [0] * (N ** 2 + 1)
pos = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
SHARK = -1
answer = 0

for r in range(N):
    line = list(map(int, input().split()))
    column = 0
    for idx in range(0, N * 2, 2):
        a, b = line[idx], line[idx + 1]
        graph[r][column] = [a, b - 1]
        fishes[a] = [r, column]
        column += 1

sr, sc = 0, 0
start_fish = graph[sr][sc][0]
fishes[start_fish] = []
graph[sr][sc] = [SHARK, graph[sr][sc][1]]

def move_fish(graph, fishes):
    moved_graph = deepcopy(graph)
    moved_fish = deepcopy(fishes)
    
    for idx in range(1, N ** 2 + 1):
        if not moved_fish[idx]:
            continue
        fr, fc = moved_fish[idx]
        _, fish_dir = moved_graph[fr][fc]

        turn = 0
        while turn < 8:
            new_dir = (fish_dir + turn) % 8
            nr, nc = fr + pos[new_dir][0], fc + pos[new_dir][1]
            
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                turn += 1
                continue
            if moved_graph[nr][nc] and moved_graph[nr][nc][0] == SHARK:
                turn += 1
                continue
            
            # 이동 가능한 방향 찾음
            fish_dir = new_dir
            moved_graph[fr][fc][1] = new_dir  # 방향 갱신
            
            if not moved_graph[nr][nc]:  # 빈 칸인 경우
                moved_graph[nr][nc] = moved_graph[fr][fc]
                moved_graph[fr][fc] = []
                moved_fish[idx] = [nr, nc]
            else:  # 다른 물고기와 swap
                swaped_idx = moved_graph[nr][nc][0]
                moved_graph[nr][nc], moved_graph[fr][fc] = moved_graph[fr][fc], moved_graph[nr][nc]
                moved_fish[idx], moved_fish[swaped_idx] = moved_fish[swaped_idx], moved_fish[idx]
            
            break  # 이동 완료
            turn += 1
    
    return moved_graph, moved_fish

def dfs(graph, fishes, shark_pos, score):
    global answer
    
    moved_graph, moved_fish = move_fish(graph, fishes)
    sr, sc = shark_pos
    _, shark_dir = moved_graph[sr][sc]

    Flag = False
    for turn in range(1, 4):  # 1, 2, 3칸
        new_graph = deepcopy(moved_graph)
        new_fish = deepcopy(moved_fish)
        
        nr, nc = sr + pos[shark_dir][0] * turn, sc + pos[shark_dir][1] * turn
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        if not new_graph[nr][nc]:  # 빈칸
            continue
            
        Flag = True
        eaten = new_graph[nr][nc][0]
        new_fish[eaten] = []
        new_graph[nr][nc][0] = SHARK
        new_graph[sr][sc] = []  # 기존 위치 빈칸
        dfs(new_graph, new_fish, [nr, nc], score + eaten)

    if not Flag:  # 더 이상 상어가 이동 못할 때
        answer = max(answer, score)
        return

dfs(graph, fishes, [0, 0], start_fish)
print(answer)
