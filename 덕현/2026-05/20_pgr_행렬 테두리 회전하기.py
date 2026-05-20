'''
프로그래머스 77485 행렬 테두리 회전하기

입력:
rows columns queries

구조:
query 돌면서 회전
최솟값 저장하고 answer 출력
'''


def rotate(graph, x1, y1, x2, y2):
    temp = graph[x1][y1]
    ans = temp

    for r in range(x1, x2):
        graph[r][y1] = graph[r + 1][y1]

        if graph[r][y1] < ans:
            ans = graph[r][y1]

    for c in range(y1, y2):
        graph[x2][c] = graph[x2][c + 1]

        if graph[x2][c] < ans:
            ans = graph[x2][c]

    for r in range(x2, x1, -1):
        graph[r][y2] = graph[r - 1][y2]

        if graph[r][y2] < ans:
            ans = graph[r][y2]

    for c in range(y2, y1, -1):
        graph[x1][c] = graph[x1][c - 1]

        if graph[x1][c] < ans:
            ans = graph[x1][c]

    graph[x1][y1 + 1] = temp

    return ans


def solution(rows, columns, queries):
    answer = []
    graph = []

    num = 1
    for r in range(rows):
        arr = []

        for c in range(columns):
            arr.append(num)
            num += 1

        graph.append(arr)

    for query in queries:
        x1, y1, x2, y2 = query

        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        num = rotate(graph, x1, y1, x2, y2)
        answer.append(num)

    return answer