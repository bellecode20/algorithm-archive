from collections import Counter

def solution(topping):
    answer = 0
    me=set()
    bro=Counter(topping)
    
    for t in topping:
        me.add(t)
        bro[t]-=1
        if bro[t]==0:
            del bro[t]
        
        if len(me)==len(bro):
            answer+=1
    return answer