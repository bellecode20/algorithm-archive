'''
BOJ 20437 문자열 게임 2

입력:
T
W
K

구조:
- graph를 문자별 인덱스 리스트(26개)로 구성
- 같은 문자 K개 묶음 구간 길이 계산
- 최소 / 최대 길이 갱신
- 없으면 -1
'''

T = int(input())

for _ in range(T):
    W = input().strip()
    K = int(input())

    graph = [[] for _ in range(26)]  # 문자별 위치 저장

    for i in range(len(W)):
        idx = ord(W[i]) - ord('a')
        graph[idx].append(i)

    mn = 10**9
    mx = -1

    for i in range(26):
        if len(graph[i]) < K:
            continue

        for j in range(len(graph[i]) - K + 1):
            length = graph[i][j + K - 1] - graph[i][j] + 1

            if length < mn:
                mn = length
            if length > mx:
                mx = length

    if mx == -1:
        print(-1)
    else:
        print(mn, mx)
