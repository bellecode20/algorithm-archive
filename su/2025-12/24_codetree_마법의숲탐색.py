# 접근 방식
# 보드판에 패딩-1을 설정
# 조건에 따라 남쪽, 서쪽, 동쪽 방향으로 골렘 이동
# 정령 이동: bfs로 최대 행 찾기

# 골렘 이동하는 과정에서 기존 골렘을 덮어쓰는 에러 발생하는 중
# 보드판 확인하는 로직 점검 필요

# 입력 텍스트 파일 실행 코드
# import sys
# from pathlib import Path
# BASE_DIR = Path(__file__).parent
# sys.stdin = open(BASE_DIR / "input.txt", "r")
# input = sys.stdin.readline


from pprint import pprint
from collections import defaultdict
from collections import deque

R, C, K = map(int, input().split())

exit_info = defaultdict(list)
PADDING = 3
board = [[-1] * (C + 2 * PADDING) for _ in range(R + 2 * PADDING)]
temp_board = [[-1] * (C + 2 * PADDING) for _ in range(R + 2 * PADDING)]

dr = [-1, 0, 1, 0]  # 북동남서
dc = [0, 1, 0, -1]
answer = 0

for r in range(PADDING, PADDING + R):
    for c in range(PADDING, PADDING + C):
        board[r][c] = 0


def can_move_south(row, col, golem_id):  # 남쪽 이동
    check_south = [(1, -1), (2, 0), (1, 1)]
    for i in range(3):
        nr, nc = row + check_south[i][0], col + check_south[i][1]
        if board[nr][nc] != 0:
            return False

    return True

def can_move_west(row, col, golem_id):  # 서쪽 이동 
    check_west = [(-1, -1), (0, -2), (1, -1), (1, -2), (2, -1)]
    for i in range(5):
        nr, nc = row + check_west[i][0], col + check_west[i][1]
        if board[nr][nc] != 0:
            return False
    return True


def can_move_east(row, col, golem_id):  # 동쪽 이동
    check_east = [(-1, 1), (0, 2), (1, 1), (1, 2), (2, 1)]

    for i in range(5):
        nr, nc = row + check_east[i][0], col + check_east[i][1]
        if board[nr][nc] != 0:
            return False
    return True


def place_golem(row, col, k):
    global board
    board[row][col] = k
    for i in range(4):
        board[row + dr[i]][col + dc[i]] = k

def move_fairy(start_r, start_c, golem_id):
    global answer
    queue = deque([(start_r, start_c)])
    max_row = start_r
    visited = defaultdict(bool)
    while queue:
        fr, fc = queue.popleft()
        is_exit = (fr, fc) == exit_info[golem_id]
        current_golem = board[fr][fc]
        max_row = max(max_row, fr)
        for i in range(4):
            nr, nc = fr + dr[i], fc + dc[i]
            if visited[(nr, nc)] == True:
                continue
            if board[nr][nc] <= 0:  # 빈 칸이나 벽
                continue
            # 같은 골렘이거나, 출구를 통해 다른 골렘으로
            if board[nr][nc] == current_golem or is_exit:
                queue.append((nr, nc))
                visited[(nr, nc)] = True
    
    return max_row - PADDING + 1  # 실제 행 번호로 변환

# 골렘마다 탐색 시작
for k in range(1, K + 1):
    c, d = map(int, input().split())  # 골렘 출발 열, 골렘 출구 방향 정보
    c = PADDING + c - 1
    r = PADDING + 1  # 정령 row
    while True:
        if can_move_south(r, c, k):
            r += 1
        elif can_move_west(r, c, k):
            r += 1
            c -= 1
            d = (d - 1) % 4  # 출구가 반시계방향으로 이동한다.
        elif can_move_east(r, c, k):
            r += 1
            c += 1       
            d = (d + 1) % 4  # 출구가 시계방향으로 이동한다.
        else:
            break

    if r < PADDING + 1:  # 숲을 벗어나는 경우
        for i in range(PADDING, PADDING + R):
            for j in range(PADDING, PADDING + C):
                board[i][j] = 0
        exit_info = defaultdict(list)
        continue

    exit_row, exit_col = r + dr[d], c + dc[d]

    # 배치하기 전 골렘 모든 칸 확인 필요
    place_golem(r, c, k)
    exit_info[k] = (exit_row, exit_col)
    max_row = move_fairy(r, c, k)
    answer += max_row

print(answer)  # 인덱스 처리