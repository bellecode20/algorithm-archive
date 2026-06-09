def solution(order):
    ans = 0
    belt=[]
    cur=1
    idx=0
    while cur<=len(order):
        belt.append(cur)
        
        while belt[-1]==order[idx]:
            ans+=1
            idx+=1
            belt.pop()
            if not belt:break
        cur+=1
    return ans