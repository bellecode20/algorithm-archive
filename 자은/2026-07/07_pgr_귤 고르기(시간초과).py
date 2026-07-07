def solution(k, tan):
    ans = 0
    t=set(tan)
    cnt=[]
    for i in t:cnt.append(tan.count(i))
    cnt.sort(reverse=True)
    
    total=0
    for i in cnt:
        ans+=1
        total+=i
        if total>=k:break
    return ans