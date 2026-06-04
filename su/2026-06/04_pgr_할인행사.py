def solution(want, number, discount):
    answer = 0
    n = len(want)
    
    for i in range(len(discount)):
        if discount[i] not in want:
            continue
            
        temp = number[:]
        for j in range(i, i + 10):
            if j >= len(discount):
                break
            
            if discount[j] not in want:
                continue
                
            idx = want.index(discount[j])
            temp[idx] -= 1
        
        
        all_zero = True
        for k in range(n):
            if temp[k] != 0:
                all_zero = False
                break
                
        if all_zero:
            answer += 1 
            
        
    return answer