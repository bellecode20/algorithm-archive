def solution(stones, k):
    temp=[stones[i] for i in range(k)]
    ans=max(temp)
    
    for i in range(k,len(stones)):
        temp.pop(0)
        temp.append(stones[i])
        mx=max(temp)
        if mx<ans:
            ans=mx
        
    return ans