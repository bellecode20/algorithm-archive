import sys

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

def rotate(r, c, s, board):
    # 0-index로 보정
    r -= 1
    c -= 1
    
    # s부터 1까지 각 껍질(layer)을 바깥쪽부터 회전
    for dist in range(1, s + 1):
        top, left = r - dist, c - dist
        bottom, right = r + dist, c + dist
        
        # 1. 가장 왼쪽 위 값을 임시 저장
        temp = board[top][left]
        
        # 2. 왼쪽 벽: 아래에서 위로 당기기
        for i in range(top, bottom):
            board[i][left] = board[i+1][left]
            
        # 3. 아래쪽 벽: 오른쪽에서 왼쪽으로 당기기
        for i in range(left, right):
            board[bottom][i] = board[bottom][i+1]
            
        # 4. 오른쪽 벽: 위에서 아래로 당기기
        for i in range(bottom, top, -1):
            board[i][right] = board[i-1][right]
            
        # 5. 위쪽 벽: 왼쪽에서 오른쪽으로 당기기
        for i in range(right, left, -1):
            board[top][i] = board[top][i-1]
            
        # 6. 임시 저장한 값을 시작점의 오른쪽 칸에 배치
        board[top][left+1] = temp

def get_array_value(board):
    return min(sum(row) for row in board)

def dfs(depth, history):
    global min_ans
    
    # 모든 연산의 순서가 결정된 경우
    if depth == K:
        # 배열 복사
        current_board = [row[:] for row in original_board]
        
        # 결정된 순서대로 회전 수행
        for idx in history:
            r, c, s = ops[idx]
            rotate(r, c, s, current_board)
        
        # 최솟값 갱신
        min_ans = min(min_ans, get_array_value(current_board))
        return

    # 순열 생성 (방문 표시 이용)
    for i in range(K):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, history + [i])
            visited[i] = False


N, M, K = map(int, input().split())
original_board = [list(map(int, input().split())) for _ in range(N)]
ops = [list(map(int, input().split())) for _ in range(K)]

min_ans = float('inf')
visited = [False] * K

# DFS 시작
dfs(0, [])

print(min_ans)