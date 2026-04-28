import heapq

def solution(jobs):
    answer = 0
    hq = []
    heapq.heapify(hq)
    N = len(jobs)
    
    for i in range(N):
        jobs[i].append(i)
        
    print(jobs)  # [요청 시첨, 소요 시간, 작업 번호]
    jobs.sort()    
    
    cur_time = 0
    i = 0
    
    # heapq.heappush(hq, (jobs[0]))
    # print(f"hq: {hq}")
    while True:
        if i >= N:
            break
            
        if hq:
            data = heapq.heappop(hq)
            cur_time += data[1]  # 소요 시간
        
        start, duration, idx = jobs[i]
        next_i = i
        
        if cur_time >= start:
            for j in range(i, N):  # 같은 요청 시각인 애들은 다 큐에 넣기
                if start != jobs[j][1]: 
                    break
                heapq.heappush(hq, (jobs[j]))
                next_i += 1
            
        else:
            cur_time = jobs[i][0]    
        
        i = next_i
        
                
    
    return answer

print(solution([[0, 3], [1, 9], [3, 5]]))