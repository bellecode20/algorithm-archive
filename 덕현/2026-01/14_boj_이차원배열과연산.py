"""
BOJ 17140 이차원 배열과 연산

규칙:
- t초가 지날 때마다 R 연산 또는 C 연산 수행
- R 연산: 모든 행에 대해 (수, 등장횟수)로 정렬 후 [수,횟수,...]로 재구성
- C 연산: 모든 열에 대해 위와 동일하게 수행
- 정렬 기준: 등장횟수 오름차순, (동률이면) 수 오름차순
- 0은 무시
- 각 행/열 길이는 최대 100까지만 유지
- 배열 크기도 최대 100x100까지만 유지
- A[r][c] == k가 되면 최소 시간 출력, 100초 넘으면 -1

입력:
r, c, k
3x3 초기 배열

구조:
- r,c는 0-index로 변환
- 0~100초 반복:
    - 현재 A[r][c] == k면 t 출력
    - 행 수 >= 열 수면 R, 아니면 C
"""

def op_rows(graph):
    new_graph = []
    max_len = 0

    for row in graph:
        cnt = {}
        for x in row:
            if x == 0:
                continue
            cnt[x] = cnt.get(x, 0) + 1

        pairs = sorted(cnt.items(), key=lambda v: (v[1], v[0]))

        new_row = []
        for num, c in pairs:
            new_row.append(num)
            new_row.append(c)
            if len(new_row) >= 100:
                new_row = new_row[:100]
                break

        max_len = max(max_len, len(new_row))
        new_graph.append(new_row)

    if max_len > 100:
        max_len = 100

    for i in range(len(new_graph)):
        if len(new_graph[i]) < max_len:
            new_graph[i].extend([0] * (max_len - len(new_graph[i])))
        else:
            new_graph[i] = new_graph[i][:max_len]

    if len(new_graph) > 100:
        new_graph = new_graph[:100]

    return new_graph

def transpose(graph):
    if not graph:
        return []
    r = len(graph)
    c = len(graph[0])
    t = []
    for j in range(c):
        col = []
        for i in range(r):
            col.append(graph[i][j])
        t.append(col)
    return t

r, c, k = map(int, input().split())
r -= 1
c -= 1

graph = [list(map(int, input().split())) for _ in range(3)]

ans = -1
for t in range(101):
    if 0 <= r < len(graph) and 0 <= c < len(graph[0]) and graph[r][c] == k:
        ans = t
        break

    if len(graph) >= len(graph[0]):
        graph = op_rows(graph)
    else:
        graph = transpose(graph)
        graph = op_rows(graph)
        graph = transpose(graph)

    if len(graph) > 100:
        graph = graph[:100]
    if graph and len(graph[0]) > 100:
        graph = [row[:100] for row in graph]

print(ans)
