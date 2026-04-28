import heapq

def solution(jobs):
    answer = 0
    hq = []
    # 1. 요청 시간 기준으로 오름차순 정렬
    jobs.sort()
    
    N = len(jobs)
    cur_time, i, count = 0, 0, 0
    
    # 모든 작업을 처리할 때까지 반복
    while count < N:
        # 2. 현재 시간(cur_time) 이전에 요청된 모든 작업을 힙에 삽입
        while i < N and jobs[i][0] <= cur_time:
            # (소요시간, 요청시간) 순으로 넣어야 소요시간 짧은 순으로 정렬됨
            heapq.heappush(hq, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if hq:
            # 3. 힙에서 소요시간이 가장 짧은 작업 꺼내서 처리
            duration, start = heapq.heappop(hq)
            cur_time += duration
            answer += (cur_time - start)
            count += 1
        else:
            # 4. 현재 시간에 처리할 작업이 없다면 다음 작업의 요청 시간으로 점프
            cur_time = jobs[i][0]
            
    return answer // N


print(solution([[0, 3], [1, 9], [3, 5]])) # 결과: 8


def solution2(jobs):
    answer = 0
    hq = []
    # 요청 시각 기준으로 정렬
    jobs.sort()
    
    N = len(jobs)
    cur_time = 0
    i = 0
    finished_count = 0
    
    while finished_count < N:
        # 1. 현재 시간(cur_time) 이전에 요청된 모든 작업을 힙에 삽입
        while i < N and jobs[i][0] <= cur_time:
            # (소요시간, 요청시각) 순으로 push
            heapq.heappush(hq, (jobs[i][1], jobs[i][0]))
            i += 1
            
        if hq:
            # 2. 힙에서 가장 짧은 작업 꺼내서 처리
            duration, start = heapq.heappop(hq)
            cur_time += duration
            answer += (cur_time - start)
            finished_count += 1
        else:
            # 3. 힙이 비어있다면, 다음 작업 요청 시각으로 시간 점프
            if i < N:
                cur_time = jobs[i][0]
                
    return answer // N

print(solution2([[0, 3], [1, 9], [3, 5]])) # 결과: 8