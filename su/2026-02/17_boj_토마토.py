# 풀이 57분
# 입력 초기화하는 부분 정리하기
# 변수명 잘못쓰지 않게 더 길게 선언해야 할 것 같음 (nr, nc, nh 부분)

from collections import deque

M, N, H = map(int, input().split())
board = []
tomato = []
total = 0

for h in range(H):
    box = []
    for n in range(N):
        line = list(map(int, input().split()))
        for m in range(M):
            if line[m] == 1:
                tomato.append((n, m, h, 0))
            if line[m] in [0, 1]:  # 토마토인 경우 총 개수 카운트
                total += 1
        box.append(line)
    board.append(box)


visited = [[[0] * M for _ in range(N)] for _ in range(H)]
queue = deque(tomato)

for i in range(len(tomato)):
    r, c, h, _ = tomato[i]
    visited[h][r][c] = 1
    
cnt = 0
answer = int(1e9)
pos = [(-1, 0, 0), (0, 1, 0), (1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)]  # row, col, height


def is_outside(cur, target):
    if cur < 0 or cur >= target:
        return True
    return False


while queue:
    row, column, floor, depth = queue.popleft()
    cnt += 1

    if cnt == total:
        answer = depth
        break
    
    for i in range(6):
        r, c, h = pos[i]
        # print(f"세로{r}, 가로{c}, 층수{h}")
        nr, nc, nh = row + r, column + c, h + floor
        if is_outside(nr, N) or is_outside(nc, M) or is_outside(nh, H):
            continue
        if visited[nh][nr][nc]:
            continue
        if board[nh][nr][nc] == -1:
            continue
        
        if board[nh][nr][nc] == 0:
            board[nh][nr][nc] = 1

        visited[nh][nr][nc] = 1
        queue.append((nr, nc, nh, depth + 1))

print(answer if answer != int(1e9) else -1)