def solution(want, number, dis):
    ans = 1
    
    def check(lst):
        nonlocal ans
        for i in range(len(want)):
            cnt=lst.count(want[i])
            if cnt!=number[i]:return False
        ans+=1
        return True
    
    buy=dis[:10]
    check(buy)
    
    if len(dis)>10:
        for i in range(10,len(dis)):
            out=buy.pop(0)
            buy=buy.append(dis[i])
            check(buy)
            
    return ans