import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate_90(board, n):
    # 보드를 시계 방향으로 90도 회전
    new_board = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_board[c][n - 1 - r] = board[r][c]
    return new_board

def move_left(board, n):
    # 한 줄씩 왼쪽으로 밀기 (0 제외 -> 합치기 -> 다시 채우기)
    new_board = [[0] * n for _ in range(n)]
    
    for r in range(n):
        # 1. 0이 아닌 숫자만 뽑기
        temp = [val for val in board[r] if val != 0]
        
        # 2. 합치기 처리
        merged = []
        skip = False
        for i in range(len(temp)):
            if skip:
                skip = False
                continue
            if i + 1 < len(temp) and temp[i] == temp[i+1]:
                merged.append(temp[i] * 2)
                skip = True # 합쳐졌으므로 다음 숫자는 건너뜀
            else:
                merged.append(temp[i])
        
        # 3. 새로운 보드 행에 채워 넣기
        for c in range(len(merged)):
            new_board[r][c] = merged[c]
            
    return new_board

def solve(board, count):
    # 5번 이동하는 모든 경우의 수를 확인 (DFS)
    global max_val
    
    # 현재 보드에서 최대값 갱신
    for r in range(N):
        for c in range(N):
            max_val = max(max_val, board[r][c])
            
    if count == 5:
        return

    # 4방향으로 이동 시도
    for _ in range(4):
        # 1. 왼쪽으로 이동 실행
        moved_board = move_left(board, N)

        # 2. 재귀 호출
        solve(moved_board, count + 1)

        # 3. 보드를 90도 회전, 다음 루프에서 다른 방향 처리
        board = rotate_90(board, N)

max_val = 0
solve(board, 0)
print(max_val)