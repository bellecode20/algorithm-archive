def solution(A, B):
    ans = 0
    A.sort()
    B.sort()
    
    a,b=0,0
    while b<len(B):
        
        if A[a]<B[b]:
            a+=1
            b+=1
            ans+=1
            continue
        
        while b<len(B) and A[a]>=B[b]:
            b+=1
        
    return ans