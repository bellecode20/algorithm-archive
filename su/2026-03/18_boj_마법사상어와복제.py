import sys
input = sys.stdin.readline
from copy import deepcopy

N = 4
M, S = map(int, input().split())

# board[r][c] = 그 칸에 있는 물고기들의 방향 리스트
board = [[[] for _ in range(N)] for _ in range(N)]

# 물고기 방향: ←, ↖, ↑, ↗, →, ↘, ↓, ↙
fish_dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  #  ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 

# 상어 방향: 상, 좌, 하, 우
shark_dirs = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

for _ in range(M):
    fx, fy, d = map(int, input().split())
    board[fx - 1][fy - 1].append(d - 1)

sx, sy = map(int, input().split())
shark = (sx - 1, sy - 1)

# smell[r][c] = 남아있는 냄새 시간
smell = [[0] * N for _ in range(N)]


def move_fish(board, shark, smell):
    new_board = [[[] for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for d in board[r][c]:
                moved = False

                # 현재 방향부터 반시계로 45도씩 8번 시도
                for k in range(8):
                    nd = (d - k) % 8
                    nr = r + fish_dirs[nd][0]
                    nc = c + fish_dirs[nd][1]

                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if (nr, nc) == shark:
                        continue
                    if smell[nr][nc] > 0:
                        continue

                    new_board[nr][nc].append(nd)
                    moved = True
                    break

                if not moved:
                    new_board[r][c].append(d)

    return new_board


def move_shark(board, shark, smell):
    best_path = []
    best_eat = -1

    def dfs(r, c, depth, eaten, path, visited):
        nonlocal best_path, best_eat

        if depth == 3:
            if eaten > best_eat:
                best_eat = eaten
                best_path = path[:]
            return

        for d in range(4):  # 상, 좌, 하, 우 순서
            nr = r + shark_dirs[d][0]
            nc = c + shark_dirs[d][1]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            add = 0
            first_visit = (nr, nc) not in visited

            if first_visit:
                add = len(board[nr][nc])
                visited.add((nr, nc))

            path.append((nr, nc))
            dfs(nr, nc, depth + 1, eaten + add, path, visited)
            path.pop()

            if first_visit:
                visited.remove((nr, nc))

    dfs(shark[0], shark[1], 0, 0, [], set())

    # 선택된 경로대로 이동하며 물고기 제거 + 냄새 남기기
    for r, c in best_path:
        if board[r][c]:          # 물고기가 있었던 칸만 냄새 생성
            board[r][c] = []
            smell[r][c] = 3

    return best_path[-1]


for _ in range(S):
    # 1. 복제 마법 시전
    copied = deepcopy(board)

    # 2. 물고기 이동
    board = move_fish(board, shark, smell)

    # 3. 상어 이동
    shark = move_shark(board, shark, smell)

    # 4. 냄새 감소
    for r in range(N):
        for c in range(N):
            if smell[r][c] > 0:
                smell[r][c] -= 1

    # 5. 복제 완료
    for r in range(N):
        for c in range(N):
            board[r][c].extend(copied[r][c])

answer = 0
for r in range(N):
    for c in range(N):
        answer += len(board[r][c])

print(answer)