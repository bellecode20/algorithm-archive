'''
BOJ 2304 창고 다각형

입력:
N
L, H

구조:
기둥 위치 정렬
최대 높이 구간 찾기(왼쪽 max, 오른쪽 max)
왼 > 오 : 최고 높이 갱신하면서 면적 더하기
오 > 왼 : 최고 높이 갱신하면서 면적 더하기
마지막에 (최대구간 폭) * 최대높이 더하기
'''

N = int(input())
graph = []
for _ in range(N):
    L, H = map(int, input().split())
    graph.append((L, H))

graph.sort()

max_h = 0
for x, h in graph:
    if h > max_h:
        max_h = h

left = 0
right = 0

for i in range(N):
    if graph[i][1] == max_h:
        left_max = i
        break

for i in range(N - 1, -1, -1):
    if graph[i][1] == max_h:
        right_max = i
        break

ans = 0

cur_h = graph[0][1]
cur_x = graph[0][0]
for i in range(1, left + 1):
    x, h = graph[i]
    if h >= cur_h:
        ans += (x - cur_x) * cur_h
        cur_h = h
        cur_x = x

cur_h = graph[-1][1]
cur_x = graph[-1][0]
for i in range(N - 2, right - 1, -1):
    x, h = graph[i]
    if h >= cur_h:
        ans += (cur_x - x) * cur_h
        cur_h = h
        cur_x = x

ans += (graph[right][0] - graph[left][0] + 1) * max_h

print(ans)
