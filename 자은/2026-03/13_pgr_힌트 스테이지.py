def solution(cost, hint):
    answer = int(1e9)
    n=len(cost)
    
    def stage(cur,total,hints): #스테이지, 총 비용, 획득한 힌트권들
        nonlocal answer,cost,hint,n
        
        cnt=hints.count(cur+1)   #현재 스테이지의 힌트권 개수
        if cnt<n:
            total+=cost[cur][cnt]   #힌트권 개수에 따른 해결비용
        elif cnt>=n:
            total+=cost[cur][-1]
            
        if cur==n-1:
            answer=min(answer,total)
            return
        
        #힌트를 안사는 경우
        stage(cur+1,total,hints)
        
        #힌트를 사는 경우
        if cur<len(hint):
            get_hint=[]
            for i in range(1,len(hint[cur])):
                get_hint.append(hint[cur][i])
            stage(cur+1,total+hint[cur][0],hints+get_hint)
        
    stage(0,0,[])
    return answer