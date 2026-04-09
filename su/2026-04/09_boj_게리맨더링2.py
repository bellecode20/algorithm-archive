N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)
answer = INF


def calculate(x, y, d1, d2):
    # 구역 번호 저장 (0: 미정, 1~5: 선거구)
    board = [[0] * N for _ in range(N)]

    # 경계선(5번 선거구) 표시
    for i in range(d1 + 1):
        board[x + i][y - i] = 5
        board[x + d2 + i][y + d2 - i] = 5

    for i in range(d2 + 1):
        board[x + i][y + i] = 5
        board[x + d1 + i][y - d1 + i] = 5

    # 경계 내부 채우기 (5번 선거구)
    for r in range(x + 1, x + d1 + d2):
        fill = False
        for c in range(N):
            if board[r][c] == 5:
                fill = not fill
            elif fill:
                board[r][c] = 5

    # 나머지 선거구
    for r in range(x + d1):
        for c in range(y + 1):
            if board[r][c] == 5: break
            board[r][c] = 1

    for r in range(x + d2 + 1):
        for c in range(N - 1, y, -1):
            if board[r][c] == 5: break
            board[r][c] = 2

    for r in range(x + d1, N):
        for c in range(y - d1 + d2):
            if board[r][c] == 5: break
            board[r][c] = 3

    for r in range(x + d2 + 1, N):
        for c in range(N - 1, y - d1 + d2 - 1, -1):
            if board[r][c] == 5: break
            board[r][c] = 4


    # 인구 계산
    population = [0] * 5
    for r in range(N):
        for c in range(N):
            population[board[r][c] - 1] += A[r][c]

    return max(population) - min(population)


for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 >= N:
                    continue
                if y - d1 < 0 or y + d2 >= N:
                    continue

                answer = min(answer, calculate(x, y, d1, d2))

print(answer)