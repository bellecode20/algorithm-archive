def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        if not stack:
            stack.append((prices[i], i))
            continue
            
            
        while stack and stack[-1][0] > prices[i]:  # 가격이 떨어진 경우
            p, idx = stack.pop()
            answer[idx] = i - idx
            
        stack.append((prices[i], i))

            
    while stack:  # 끝까지 가격이 안 떨어진 경우
        p, idx = stack.pop()
        answer[idx] = n - 1 - idx
    
    return answer