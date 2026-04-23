'''
BOJ 17143 낚시왕

입력:
R C M
graph

구조:
가장 위 상어 잡고 상어 전부 이동
같은 칸이면 큰 상어만 남기기
'''

R, C, M = map(int, input().split())
graph = [[0] * C for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    graph[r-1][c-1] = [s,d,z]

ans = 0

for king in range(C):

    for r in range(R):
        if graph[r][king] != 0:
            ans += graph[r][king][2]
            graph[r][king] = 0
            break

    new = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if graph[r][c] == 0:
                continue

            s, d, z = graph[r][c]

            nr = r
            nc = c

            if d == 1 or d == 2:
                if R > 1:
                    s = s % (2 * (R - 1))
                else:
                    s = 0

                for _ in range(s):
                    if d == 1:
                        if nr == 0:
                            d = 2
                            nr += 1
                        else:
                            nr -= 1
                    else:
                        if nr == R - 1:
                            d = 1
                            nr -= 1
                        else:
                            nr += 1

            else:
                if C > 1:
                    s = s % (2 * (C - 1))
                else:
                    s = 0

                for _ in range(s):
                    if d == 4:
                        if nc == 0:
                            d = 3
                            nc += 1
                        else:
                            nc -= 1
                    else:
                        if nc == C - 1:
                            d = 4
                            nc -= 1
                        else:
                            nc += 1

            if new[nr][nc] == 0:
                new[nr][nc] = [graph[r][c][0], d, z]
            else:
                if new[nr][nc][2] < z:
                    new[nr][nc] = [graph[r][c][0], d, z]
    graph = new
print(ans)