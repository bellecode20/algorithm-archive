'''
BOJ 14719 빗물

입력:
H, W
graph

구조:
- 가로 한 칸씩 왼쪽 최대, 오른쪽 최대 찾기
- 왼오의 최솟값 찾고 내 높이빼서 더해주기
- 그래ㄷ서 다 보면서 더하기
'''

H, W = map(int, input().split())
graph = list(map(int, input().split()))

ans = 0

for i in range(1, W - 1):
    left = 0
    for j in range(i, -1, -1):
        if graph[j] > left:
            left = graph[j]

    right = 0
    for j in range(i, W):
        if graph[j] > right:
            right = graph[j]

    water = min(left, right) - graph[i]
    if water > 0:
        ans += water

print(ans)
