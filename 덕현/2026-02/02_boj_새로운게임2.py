'''
BOJ 17837 새로운 게임 2

입력:
N, K
board (0:흰, 1:빨, 2:파)
K개 말

구조:
- i부터 위에 있는 말들 같이 이동
- 다음 칸이 범위 밖 or 파면 방향 반대로 바꾸고 1번 더 시도 // 같으면 이동 안함
- 흰: 그대로 쌓기
- 빨: 이동하는 덩어리 순서 뒤집어서 쌓기
- 무조건 말 4개 이상 쌓이면 그 턴 출력, 아니면 -1
- 말 정보 pieces[i]
- 칸마다 말 쌓임 stacks[r][c]
- 1~1000까지 가능
'''

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 우좌상하
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def rev_dir(d):
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    return 3

pieces = []
stacks = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    pieces.append([r, c, d])
    stacks[r][c].append(i)

done = False
answer = -1

for turn in range(1, 1001):
    for i in range(K):
        r, c, d = pieces[i]

        nr = r + dr[d]
        nc = c + dc[d]

        if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
            d = rev_dir(d)
            pieces[i][2] = d

            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                continue

        cell = stacks[r][c]
        idx = 0
        while cell[idx] != i:
            idx += 1

        moving = cell[idx:]
        stacks[r][c] = cell[:idx]

        if board[nr][nc] == 1:
            moving.reverse()

        dest = stacks[nr][nc]
        for p in moving:
            pieces[p][0] = nr
            pieces[p][1] = nc
            dest.append(p)

        if len(dest) >= 4:
            done = True
            answer = turn
            break

    if done:
        break

print(answer)
