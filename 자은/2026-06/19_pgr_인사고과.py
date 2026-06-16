def solution(scores):
    ans = 0
    n=len(scores)
    me=scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))    
    
    mx=scores[0][1]
    for a,b in scores:
        if me[0]<a and me[1]<b:return -1
        
        if b>=mx:
            mx=b
            if a+b>sum(me):
                ans+=1
    return ans+1