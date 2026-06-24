'''
pgr 131130 혼자놀기의 달인

입력:
cards
'''


def solution(cards):
    answer = 0
    n = len(cards)

    visited = [0] * n
    arr = []

    for i in range(n):
        if visited[i] == 1:
            continue

        cnt = 0
        now = i

        while visited[now] == 0:
            visited[now] = 1
            cnt += 1
            now = cards[now] - 1
        arr.append(cnt)

    arr.sort(reverse=True)

    if len(arr) < 2:
        return 0

    answer = arr[0] * arr[1]

    return answer