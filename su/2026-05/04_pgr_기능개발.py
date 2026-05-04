'''
day 계산 수정 필요

'''

from collections import deque
import heapq

def solution(progresses, speeds):
    answer = []
    progresses = [0] + progresses
    speeds = [0] + speeds
    
    memo = [0] * len(progresses)
    N = len(progresses)
    queue = deque([])
    waiting = []
    heapq.heapify(waiting)

    memo[0] = 1
    # print(memo)
    
    for i in range(1, N):
        queue.append((i, progresses[i]))
        
    day = 1
    answer = []
    while queue:
        i, percent = queue.popleft()
        next_per = percent + speeds[i]
        # print(f"i: {i}, next_per: {next_per}\n")
        
        if next_per >= 100:
            heapq.heappush(waiting, i)
        else:
            queue.append((i, next_per))
        
        cnt = 0
        while waiting and memo[waiting[-1] - 1] == 1:
            idx = heapq.heappop(waiting)
            memo[idx - 1] = 1
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
            
    day += 1

    return answer

print(solution([93, 30, 55], [1, 30, 5]))