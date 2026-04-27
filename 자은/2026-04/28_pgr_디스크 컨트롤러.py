import heapq

def solution(jobs):
    answer = 0
    jobs.sort()
    
    wait=[]
    sm=0    #반환시간 합
    time=0  #현재시각
    idx=0   #대기줄에 넣을 인덱스
    cnt=0   #완료된 작업개수
    
    while cnt<len(jobs):
        
        while idx<len(jobs) and jobs[idx][0]<=time:
            s,l=jobs[idx]
            heapq.heappush(wait,(l,s))
            idx+=1
        
        if wait:
            l,s=heapq.heappop(wait)
            time+=l
            sm+=(time-s)
            cnt+=1
        else:
            time=jobs[idx][0]
    
    answer=sm//len(jobs)
    
    return answer