def solution(order):
    stack = []
    cur = 1
    cnt = 0
    
    for box in order:
        while cur <= box:
            if cur == box:
                cnt += 1
                cur += 1
                break
            else:
                stack.append(cur)
                cur += 1
        
        while stack and stack[-1] == box:
            stack.pop()
            cnt += 1
            break
        else:
            if stack and stack[-1] != box:
                break
    
    return cnt