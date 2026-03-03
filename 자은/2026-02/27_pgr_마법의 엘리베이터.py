def solution(storey):
    answer = 0
    
    while storey!=0:
        c=storey%10
        
        if c>5:
            answer+=10-c
            storey+=10
        elif c==5:
            n=(storey//10)%10
            if n>=5:
                answer+=10-c
                storey+=10
            else:
                answer+=c
        else:
            answer+=c
        storey//=10
        
    return answer