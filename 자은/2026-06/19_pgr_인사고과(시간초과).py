def solution(s):
    answer = 0
    n=len(s)
    out=[False]*n
    
    for i in range(n-1):
        a,b=s[i]
        for j in range(i+1,n):
            c,d=s[j]
            if a>c and b>d:
                out[j]=True
            elif a<c and b<d:
                out[i]=True
    if out[0]:return -1
    
    me=sum(s[0])
    bonus=[]
    for i in range(n):
        if not out[i]:
            bonus.append(sum(s[i]))
    bonus.sort(reverse=True)
    answer=bonus.index(me)
    
    return answer+1