def solution(number, k):
    stack = []
    
    for num in number:

        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
                
        stack.append(num)
    
    # 만약 k가 남았다면 뒤를 잘라주는 처리
    return "".join(stack[:len(number)-k])