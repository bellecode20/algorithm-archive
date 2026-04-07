def solve(lst):
    mx_sm=lst[0]
    cur=lst[0]
    
    for i in range(1,len(lst)):
        cur=max(lst[i],cur+lst[i])
        mx_sm=max(mx_sm,cur)
    return mx_sm

def solution(sequence):
    answer = 0
    plus=sequence[:]
    minus=sequence[:]
    
    for i in range(len(sequence)):
        if i%2==0:
            minus[i]*=-1
        if i%2==1:
            plus[i]*=-1
    answer=max(solve(plus),solve(minus))
    
    return answer