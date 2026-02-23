from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:return 0
    if begin==target:return 0
    
    q=deque()
    q.append((begin,0))
    
    while q:
        cw,cnt=q.popleft()
        
        if cw==target:
            answer=cnt
            break
        
        for word in words:
            diff=0
            for i in range(len(word)):
                if word[i]!=cw[i]:
                    diff+=1
            if diff==1:q.append((word,cnt+1))
                
    return answer