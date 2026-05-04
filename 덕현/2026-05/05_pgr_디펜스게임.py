'''
프로그래머스 디펜스 게임

입력:
n
k
enemy

구조:
걍 우선순위 큐 써서 뽑기
큰거뽑으려면 걍 음수 쓰기
'''

import heapq

def solution(n, k, enemy):
    heap = []

    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(heap, -enemy[i])

        if n < 0:
            if k > 0:
                big = -heapq.heappop(heap)
                n += big
                k -= 1
            else:
                return i

    return len(enemy)