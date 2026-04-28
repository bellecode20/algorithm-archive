'''
프로그래머스 디스크 컨트롤러

입력:
jobs

구조:
정렬 박고 우선순위 큐
총 걸린 시간 누적
'''

import heapq

def solution(jobs):
    jobs.sort()

    n = len(jobs)
    heap = []

    time = 0
    idx = 0
    cnt = 0
    total = 0

    while cnt < n:

        while idx < n:
            if jobs[idx][0] <= time:
                heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
                idx += 1
            else:
                break

        if heap:
            work, start = heapq.heappop(heap)
            time += work
            total += time - start
            cnt += 1
        else:
            time = jobs[idx][0]

    return total // n