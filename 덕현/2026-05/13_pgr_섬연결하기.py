'''
프로그래머스 섬 연결하기

입력:
n
costs

구조:
MST? 그거 문제
SWEA 섬문제랑 비슷
정렬하고 부모해가지고 작은거부터 보기
'''

def solution(n, costs):
    parent = []

    for i in range(n):
        parent.append(i)

    costs.sort(key=lambda x: x[2])

    answer = 0
    cnt = 0

    for a, b, cost in costs:
        while parent[a] != a:
            a = parent[a]

        while parent[b] != b:
            b = parent[b]

        if a == b:
            continue

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

        answer += cost
        cnt += 1

        if cnt == n - 1:
            break

    return answer