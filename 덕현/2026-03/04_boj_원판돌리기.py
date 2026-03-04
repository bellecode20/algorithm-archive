'''
BOJ 17822 원판 돌리기

입력:
N, M, T
graph

구조:
x배수 원판 회전하고 인접 같은 수 지우기
없으면 평균 기준 조정
마지막은 합
'''

def remove_same():
    to_remove = [[False] * M for _ in range(N)]
    found = False

    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                continue

            v = graph[r][c]

            nc = (c + 1) % M
            if graph[r][nc] == v:
                to_remove[r][c] = True
                to_remove[r][nc] = True
                found = True

            if r + 1 < N and graph[r + 1][c] == v:
                to_remove[r][c] = True
                to_remove[r + 1][c] = True
                found = True

    if found:
        for r in range(N):
            for c in range(M):
                if to_remove[r][c]:
                    graph[r][c] = 0

    return found


N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    k %= M

    for i in range(x - 1, N, x):
        if d == 0:
            graph[i] = graph[i][-k:] + graph[i][:-k]
        else:
            graph[i] = graph[i][k:] + graph[i][:k]

    if not remove_same():
        total = 0
        cnt = 0

        for r in range(N):
            for c in range(M):
                if graph[r][c] != 0:
                    total += graph[r][c]
                    cnt += 1

        if cnt > 0:
            avg = total / cnt

            for r in range(N):
                for c in range(M):
                    if graph[r][c] == 0:
                        continue
                    if graph[r][c] > avg:
                        graph[r][c] -= 1
                    elif graph[r][c] < avg:
                        graph[r][c] += 1

ans = 0
for r in range(N):
    for c in range(M):
        ans += graph[r][c]

print(ans)