from collections import deque

def solution(stones, k):
    dq=deque()
    ans=float("inf")

    for i in range(len(stones)):
        while dq and stones[dq[-1]]<=stones[i]:
            dq.pop()
        dq.append(i)
        
        while dq[0]<=i-k:
            dq.popleft()
        if i>=k-1:
            ans=min(ans,stones[dq[0]])
        
    return ans