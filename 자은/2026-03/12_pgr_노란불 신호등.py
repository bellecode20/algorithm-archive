def lcm(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            return i
    
def solution(signals):
    answer = -1
    n=len(signals)
    
    cycle=[sum(lst) for lst in signals] #각 신호등 주기
    
    lm=cycle[0]
    for i in range(1,len(cycle)):   #주기들의 최소공배수 구하기
        lm=lcm(lm,cycle[i])
    
    for time in range(1,lm+1):
        cnt=0
        
        for i in range(n):
            
            #(현재시간대를 현재신호등의 주기길이로 나누었을때)나머지가 초록불의 시간범위보다 같거나 작다면 초록불임
            if time%cycle[i]<=signals[i][0]:   #초록불
                break
                
            #나머지가 해당 신호등의 노랑불의 시간범위 안에 있으면 노랑불임
            elif time%cycle[i]<=signals[i][0]+signals[i][1]:    #노란불
                cnt+=1
            else:   #그 외 빨강불
                break
            
        if cnt==n:  #모든 신호등이 현재 시간대에 노랑불이면
            answer=time
            break
    
    return answer