def solution(word):
    answer = 0
    alpha="AEIOU"
    cnt=0
    
    def solve(temp):
        nonlocal cnt, answer
        
        if temp==word:
            answer=cnt
            return
        
        if len(temp)>4:
            return
        
        for a in alpha:
            cnt+=1
            solve(temp+a)
            
    solve("")
        
    return answer