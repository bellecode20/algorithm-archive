'''
프로그래머스 49191 순위

구조:
a승 a > b
i k 이기고, k j 이기면 i j 이김.
이걸 전부 퍼트려?
i가 다른애들이랑 정해져 있으면 순위 고정?
'''

def solution(n, results):
    graph = [[0]*(n + 1) for _ in range(n + 1)]

    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if i == k:
                continue
            if graph[i][k] != 1:
                continue
            for j in range(1, n + 1):
                if graph[k][j] == 1 and graph[i][j] == 0:
                    graph[i][j] = 1
                    graph[j][i] = -1

    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if i != j and graph[i][j] != 0:
                cnt += 1
        if cnt == n - 1:
            ans += 1

    return ans