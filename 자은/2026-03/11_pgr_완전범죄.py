def solution(info, n, m):
    answer = 121
    memo={}
    
    def steal(cnt,cn,cm):
        nonlocal n,m,answer
        
        if (cnt,cn,cm) in memo:return
        if cn>=answer:return
        if cnt>len(info):return
    
        if cnt==len(info):
            answer=min(answer,cn)
            return
        
        if cn+info[cnt][0]<n:
            steal(cnt+1,cn+info[cnt][0],cm)
        if cm+info[cnt][1]<m:
            steal(cnt+1,cn,cm+info[cnt][1])
        
        memo[(cnt,cn,cm)]=True
        
    steal(0,0,0)
    if answer==121:
        answer=-1
    
    return answer